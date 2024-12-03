import httpx
import pandas as pd
from io import BytesIO
from uuid import uuid4
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from enum import Enum
import uvicorn

app = FastAPI(title="Data Processor API", version="1.0.0", description="API for processing datasets.")


DB_SERVICE_URL = "http://db-service-service:8080"
# DB_SERVICE_URL = "http://192.168.49.2:32020"


class AnonymizationType(str, Enum):
    HideEMail = "HideEMail"
    HideRandomSymbols = "HideRandomSymbols"
    ApplyHash = "ApplyHash"


class TransformationType(str, Enum):
    Uppercase = "Uppercase"
    Lowercase = "Lowercase"
    StripSpaces = "StripSpaces"
    Capitalize = "Capitalize"


# Helper function to download dataset from URL
async def download_dataset(url: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # Ensure the request is successful
            return pd.read_csv(BytesIO(response.content))  # Assuming CSV for simplicity
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error downloading dataset: {str(e)}")


# Helper function to return a DataFrame as an in-memory file
def dataframe_to_memory_file(df: pd.DataFrame, file_format: str = "csv"):
    memory_file = BytesIO()
    if file_format == "csv":
        df.to_csv(memory_file, index=False)
    elif file_format == "json":
        df.to_json(memory_file, orient="records")
    else:
        raise HTTPException(status_code=400, detail="Unsupported file format. Only CSV and JSON are supported.")
    memory_file.seek(0)
    return memory_file


# Helper function to post dataset to URL
async def post_dataset_to_url(df: pd.DataFrame, file_name: str, file_format: str = "csv"):
    memory_file = dataframe_to_memory_file(df, file_format=file_format)
    try:
        target_url = f"{DB_SERVICE_URL}/upload/"
        async with httpx.AsyncClient() as client:
            response = await client.post(target_url, files={"file": (f"{file_name}", memory_file, "application/octet-stream")})
            response.raise_for_status()  # Raise exception for unsuccessful response
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"Failed to post dataset: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error posting dataset to target URL: {str(e)}")


@app.post("/data-processor/cleanse")
async def cleanse(dataset_url: str, ):
    try:
        # Download the dataset from the URL
        df = await download_dataset(dataset_url)

        # Remove rows with missing values and duplicates
        cleansed_data = df.dropna().drop_duplicates()

        # Post the cleansed data to the target URL
        post_response = await post_dataset_to_url(cleansed_data, dataset_url.split('/')[-1])

        # Return the cleansed data as a CSV file
        file_in_memory = dataframe_to_memory_file(cleansed_data, file_format="csv")

        return post_response
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during cleansing: {str(e)}")


@app.post("/data-processor/merge")
async def merge(dataset_a_url: str, dataset_b_url: str, merge_field_name: str):
    try:
        # Download both datasets from their respective URLs
        df_a = await download_dataset(dataset_a_url)
        df_b = await download_dataset(dataset_b_url)

        # Ensure the merge field exists in both datasets
        if merge_field_name not in df_a.columns or merge_field_name not in df_b.columns:
            raise HTTPException(
                status_code=400, detail=f"Merge field '{merge_field_name}' not found in one of the datasets."
            )

        # Merge the datasets on the specified field
        merged_data = pd.merge(df_a, df_b, on=merge_field_name, how="inner")

        # Post the merged data to the target URL
        post_response = await post_dataset_to_url(merged_data, dataset_a_url.split('/')[-1])

        file_in_memory = dataframe_to_memory_file(merged_data, file_format="csv")

        return post_response
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during merge: {str(e)}")


@app.post("/data-processor/anonymize")
async def anonymize(dataset_url: str, anonymization_params: AnonymizationType, column_name: str):
    try:
        # Download the dataset from the URL
        df = await download_dataset(dataset_url)

        # Check if the specified column exists
        if column_name not in df.columns:
            raise HTTPException(status_code=400, detail=f"Column '{column_name}' not found in the dataset.")

        # Apply anonymization based on the specified type
        if anonymization_params == AnonymizationType.HideEMail:
            # Mask email addresses
            df[column_name] = df[column_name].replace(
                to_replace=r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", 
                value="hidden@example.com", 
                regex=True
            )
        elif anonymization_params == AnonymizationType.HideRandomSymbols:
            # Replace non-alphanumeric characters with "*"
            df[column_name] = df[column_name].replace(to_replace=r"[^\w\s]", value="*", regex=True)

        # Post the anonymized data to the target URL
        post_response = await post_dataset_to_url(df, dataset_url.split('/')[-1])

        # Return the anonymized data as a CSV file
        file_in_memory = dataframe_to_memory_file(df, file_format="csv")

        return post_response
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during anonymization: {str(e)}")


@app.post("/data-processor/transform")
async def transform(dataset_url: str, transformation_type: TransformationType, transformation_column_name: str):
    try:
        # Download the dataset from the URL
        df = await download_dataset(dataset_url)

        # Ensure the column exists
        if transformation_column_name not in df.columns:
            raise HTTPException(status_code=400, detail=f"Column '{transformation_column_name}' not found in the dataset.")

        # Apply the specified transformation
        if transformation_type == TransformationType.Uppercase:
            df[transformation_column_name] = df[transformation_column_name].str.upper()
        elif transformation_type == TransformationType.Lowercase:
            df[transformation_column_name] = df[transformation_column_name].str.lower()
        elif transformation_type == TransformationType.StripSpaces:
            df[transformation_column_name] = df[transformation_column_name].str.strip()
        elif transformation_type == TransformationType.Capitalize:
            df[transformation_column_name] = df[transformation_column_name].str.capitalize()

        # Post the transformed data to the target URL
        post_response = await post_dataset_to_url(df, dataset_url.split('/')[-1])


        # Return the transformed data as a CSV file
        file_in_memory = dataframe_to_memory_file(df, file_format="csv")

        return post_response
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during transformation: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
