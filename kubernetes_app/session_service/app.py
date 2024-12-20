import uvicorn
import httpx
import requests
from io import BytesIO
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pydantic.json_schema import SkipJsonSchema
from typing import List, Optional, Dict
from uuid import uuid4


dataset_a_url = "https://s666vla.storage.yandex.net/rdisk/73881565a366ba8794a2a93be0cb511773965618b089ed1c5e8f5adee6c42e1f/674f2d6f/GORH-WLDFTp3elLhwAv8recGK_lQ-p9MpCAzIZd89OUHtGCzD2nLBgYKSQW_MXxwX7yvhHLXLsH-hJm_DvUoiQ==?uid=0&filename=dataset_a.csv&disposition=attachment&hash=bJtznY6WJOocHUXbvZzVpCiaIo2LEQCmut9NNFOxT7sPxhxlAoRxPCvla96JpKV9q/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=text%2Fplain&owner_uid=1489006053&fsize=52&hid=72b8455668ee2f367d93ffcc383cb5f7&media_type=spreadsheet&tknv=v2&ts=6285fe702f9c0&s=04427bee1826d30cfbbabe42534dda3eed9408ac0153f5ec96fbd6afc4ff43ab&pb=U2FsdGVkX188ixIoil2We54HIqjCEzgr2Wn9du1jmh82LuYEQ9CdhVRaX3O2HK41WkULb52-bpooeQy-Px3y9cV8Yn7Rh-AKYD5eCPtKL5Y"
dataset_b_url = "https://s50vlx.storage.yandex.net/rdisk/e4e0699f65100fc7dffc7a47e0560337369fef20b212d9f59fdcd142a3aef56c/674f2e83/GORH-WLDFTp3elLhwAv8rQmlKbLQHYt1UW7_-y6QksNtf7YILfar6sFVC7XWPuFsTuZn9j8OdKgMdnjqsMJKWg==?uid=0&filename=dataset_b.csv&disposition=attachment&hash=kUOS5fDnBXOdl8JdecnPw0KicRXsG/1Qink7LW6ZKeVPohlEfEPxnWItCS%2BfDnIpq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=text%2Fplain&owner_uid=1489006053&fsize=85&hid=dbb3ca65a882e72e6c1ca8295aa9497d&media_type=spreadsheet&tknv=v2&ts=6285ff77666c0&s=2953d76e1644fd9afaac04b081b33763b01c1285d512005e80b0c6125213726f&pb=U2FsdGVkX1-4yacjNiy0K5l_GaiwTeF6Q80AqyZtMK7AIdSd68iheXW3kdT-KOajidIvuy19NH04U8lk5uCS0D1J4uE0pTvklaOusDXZFwc"

DB_SERVICE_URL = "http://db-service-service:8080"
EMAIL_SERVICE_URL = "http://email-service:8080"
DATAPROCESSING_SERVICE_URL = "http://dataprocessing-service:8080"


DB_SERVICE_URL = "http://192.168.49.2:30461"
EMAIL_SERVICE_URL = "http://192.168.49.2:31649"
# DATAPROCESSING_SERVICE_URL = "http://192.168.49.2:30908"
DATAPROCESSING_SERVICE_URL = "http://localhost:8081"


app = FastAPI()


# Models
class Step(BaseModel):
    stepType: str

    dataset_a_s3_url: SkipJsonSchema[str] = Field(exclude=True, default=None)
    dataset_b_s3_url: SkipJsonSchema[Optional[str]] = Field(exclude=True, default=None)

    column_name: str
    step_param: Optional[str] = None


class DataProcessorSession(BaseModel):
    id: SkipJsonSchema[str] = Field(exclude=True, default=None)
    name: str
    dataset_a_download_url: str 
    dataset_b_download_url: str

    steps: List[Step]


class DataProcessorSessionResponse(BaseModel):
    id: str
    name: str
    steps: List[Step]




# In-memory storage
sessions: Dict[str, DataProcessorSession] = {}

# HTTP client for data processor interactions
dataprocessing_client = httpx.AsyncClient(
    base_url=DATAPROCESSING_SERVICE_URL
)  # Adjust base URL if needed

email_client = httpx.AsyncClient(
    base_url=EMAIL_SERVICE_URL
)  # Adjust base URL if needed

db_service_client = httpx.AsyncClient(
    base_url=DB_SERVICE_URL
)  # Adjust base URL if needed



# Helper function to post dataset to URL
async def post_dataset_to_url(file_url, file_name: str=""):
    try:

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(file_url)
                
                # Save file in memory as a BytesIO object
                memory_file = BytesIO(response.content)
                memory_file.seek(0)  # Reset the pointer to the beginning of the file

            except httpx.RequestError as e:
                print(f"Error downloading or uploading the file: {e}")
            except httpx.HTTPStatusError as e:
                print(f"HTTP error occurred: {e}")


        if not file_name:
            file_name = f'{uuid4()}.csv'

        target_url = f"{DB_SERVICE_URL}/upload/"
        async with httpx.AsyncClient() as client:
            response = await client.post(target_url, files={"file": (f"{file_name}", memory_file, "application/octet-stream")})
            response.raise_for_status()  # Raise exception for unsuccessful response
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"Failed to post dataset: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error posting dataset to target URL: {str(e)}")


# Endpoints
@app.post(
    "/data-processor-sessions",
    response_model=DataProcessorSessionResponse,
    status_code=201,
)
async def create_session(session: DataProcessorSession):
    session_id = str(uuid4())
    session.id = session_id
    sessions[session_id] = session
    return session


@app.get("/data-processor-sessions", response_model=List[DataProcessorSessionResponse])
async def get_sessions():
    return list(sessions.values())


@app.get(
    "/data-processor-sessions/{sessionId}", response_model=DataProcessorSessionResponse
)
async def get_session(sessionId: str):
    if sessionId not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    return sessions[sessionId]


@app.put(
    "/data-processor-sessions/{sessionId}", response_model=DataProcessorSessionResponse
)
async def update_session(sessionId: str, session: DataProcessorSession):
    if sessionId not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    updated_session = DataProcessorSessionResponse(
        id=sessionId, name=session.name, steps=session.steps
    )
    sessions[sessionId] = updated_session
    return updated_session


@app.delete(
    "/data-processor-sessions/{sessionId}", response_model=DataProcessorSessionResponse
)
async def delete_session(sessionId: str):
    if sessionId not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    session = sessions.pop(sessionId)
    return session


@app.post("/data-processor-sessions/{sessionId}/start", status_code=200)
async def start_session(sessionId: str):
    failed_somewhere = False

    if sessionId not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    session = sessions[sessionId]
    step_results = []

    dataset_a_url_s3 = await post_dataset_to_url(session.dataset_a_download_url)
    dataset_a_url_s3 = dataset_a_url_s3.get("url")
    dataset_b_url_s3 = await post_dataset_to_url(session.dataset_b_download_url)
    dataset_b_url_s3 = dataset_b_url_s3.get("url")

    # Process each step in the session
    for step in session.steps:
        if step.stepType == "Cleansing":
            try:
                # Send to the cleansing API
                cleanse_response = await dataprocessing_client.post(
                    "/data-processor/cleanse", params={"dataset": dataset_a_url_s3}
                )
                step_results.append(
                    {"stepType": step.stepType, "status": "Completed", "message": "okay"}
                )

            except Exception as e:
                step_results.append(
                    {"stepType": step.stepType, "status": "Error", "message": str(e)}
                )
                failed_somewhere = True

        elif step.stepType == "Anonymization":
            try:

                # Send to the anonymization API
                anonymize_response = await dataprocessing_client.post(
                    "/data-processor/anonymize",
                    params={
                        "dataset": dataset_a_url_s3,
                        "anonymization_params": step.step_param,
                        "column_name": step.column_name,
                    },
                )
                step_results.append(
                    {"stepType": step.stepType, "status": "Completed", "message": "okay"}
                )

            except Exception as e:
                step_results.append(
                    {"stepType": step.stepType, "status": "Error", "message": str(e)}
                )
                failed_somewhere = True

        elif step.stepType == "Transformation":
            try:

                # Send to the transformation API
                transform_response = await dataprocessing_client.post(
                    "/data-processor/transform",\
                    params={
                        "dataset": dataset_a_url_s3,
                        "transformation_type": step.step_param,
                        "transformation_column_name": step.column_name,
                    },
                )
                step_results.append(
                    {"stepType": step.stepType, "status": "Completed", "message": "okay"}
                )

            except Exception as e:
                step_results.append(
                    {"stepType": step.stepType, "status": "Error", "message": str(e)}
                )
                failed_somewhere = True

        elif step.stepType == "Merge":
            try:

                # Send to the merge API
                merge_response = await dataprocessing_client.post(
                    "/data-processor/merge",
                    
                    params={"merge_field_name": step.column_name,
                        "dataset_a_url": dataset_a_url_s3,
                        "dataset_b_url": dataset_b_url_s3,},
                )
                step_results.append(
                    {"stepType": step.stepType, "status": "Completed", "message": "okay"}
                )

            except Exception as e:
                step_results.append(
                    {"stepType": step.stepType, "status": "Error", "message": str(e)}
                )
                failed_somewhere = True

    step_results_str = str(step_results)
    if not failed_somewhere:
        email_notification = {
            "session_id": sessionId,
            "email": "awesomecosmonaut@gmail.com",
            "new_status_id": 4,
        }

    else:
        email_notification = {
            "session_id": sessionId,
            "email": "awesomecosmonaut@gmail.com",
            "new_status_id": 5,
        }

    upload_response = requests.post(
        f"{EMAIL_SERVICE_URL}/session/notify", data=email_notification
    )

    return {"sessionId": sessionId, "stepResults": step_results, "resultURL": dataset_a_url_s3}


# Run the application with: uvicorn app_name:app --reload

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
