from enum import Enum
import uvicorn
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
import pandas as pd
import io

app = FastAPI(title="Data Processor API", version="1.0.0", description="API for processing datasets.")


class AnonymizationType(str, Enum):
    HideEMail = "HideEMail"
    HideRandomSymbols = "HideRandomSymbols"
    ApplyHash = "ApplyHash"


class TransformationType(str, Enum):
    Uppercase = "Uppercase"
    Lowercase = "Lowercase"
    StripSpaces = "StripSpaces"
    Capitalize = "Capitalize"


# Helper function to read uploaded dataset
def read_dataset(file: UploadFile):
    try:
        if file.filename.endswith(".csv"):
            return pd.read_csv(io.BytesIO(file.file.read()))
        elif file.filename.endswith(".json"):
            return pd.read_json(io.BytesIO(file.file.read()))
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format. Only CSV and JSON are supported.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading dataset: {str(e)}")


# Helper function to return a DataFrame as an in-memory file
def dataframe_to_memory_file(df: pd.DataFrame, file_format: str = "csv"):
    memory_file = io.BytesIO()
    if file_format == "csv":
        df.to_csv(memory_file, index=False)
    elif file_format == "json":
        df.to_json(memory_file, orient="records")
    else:
        raise HTTPException(status_code=400, detail="Unsupported file format. Only CSV and JSON are supported.")
    memory_file.seek(0)
    return memory_file


@app.post("/data-processor/cleanse")
async def cleanse(dataset: UploadFile):
    try:
        # Чтение загруженного набора данных
        df = read_dataset(dataset)

        # Удаление строк с пропущенными значениями и дубликатов
        cleansed_data = df.dropna().drop_duplicates()

        # Возвращаем очищенные данные в формате CSV с сохранением всех столбцов
        file_in_memory = dataframe_to_memory_file(cleansed_data, file_format="csv")

        return StreamingResponse(
            file_in_memory,
            media_type="application/octet-stream",
            headers={"Content-Disposition": 'inline; filename="cleansed_data.csv"'},
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during cleansing: {str(e)}")


@app.post("/data-processor/merge")
async def merge(dataset_a: UploadFile, dataset_b: UploadFile, merge_field_name: str):
    try:
        df_a = read_dataset(dataset_a)
        df_b = read_dataset(dataset_b)

        if merge_field_name not in df_a.columns or merge_field_name not in df_b.columns:
            raise HTTPException(
                status_code=400, detail=f"Merge field '{merge_field_name}' not found in one of the datasets."
            )

        merged_data = pd.merge(df_a, df_b, on=merge_field_name, how="inner")
        file_in_memory = dataframe_to_memory_file(merged_data, file_format="csv")

        return StreamingResponse(
            file_in_memory,
            media_type="application/octet-stream",
            headers={"Content-Disposition": 'inline; filename="merged_data.csv"'},
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during merge: {str(e)}")


@app.post("/data-processor/anonymize")
async def anonymize(dataset: UploadFile, anonymization_params: AnonymizationType, column_name: str):
    try:
        df = read_dataset(dataset)

        # Check if the specified column exists
        if column_name not in df.columns:
            raise HTTPException(status_code=400, detail=f"Column '{column_name}' not found in the dataset.")

        # Apply the anonymization logic to the specified column
        if anonymization_params == AnonymizationType.HideEMail:
            # Replace email addresses (e.g., example@mail.com) with a masked version
            df[column_name] = df[column_name].replace(
                to_replace=r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", 
                value="hidden@example.com", 
                regex=True
            )
        
        elif anonymization_params == AnonymizationType.HideRandomSymbols:
            # Replace all non-alphanumeric characters with "*"
            df[column_name] = df[column_name].replace(to_replace=r"[^\w\s]", value="*", regex=True)

        # Return the anonymized data as a CSV file
        file_in_memory = dataframe_to_memory_file(df, file_format="csv")

        return StreamingResponse(
            file_in_memory,
            media_type="application/octet-stream",
            headers={"Content-Disposition": 'inline; filename="anonymized_data.csv"'},
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during anonymization: {str(e)}")


@app.post("/data-processor/transform")
async def transform(
    dataset: UploadFile,
    transformation_type: TransformationType,
    transformation_column_name: str
):
    try:
        df = read_dataset(dataset)

        if transformation_column_name not in df.columns:
            raise HTTPException(status_code=400, detail=f"Column '{transformation_column_name}' not found in the dataset.")

        if transformation_type == TransformationType.Uppercase:
            df[transformation_column_name] = df[transformation_column_name].str.upper()
        elif transformation_type == TransformationType.Lowercase:
            df[transformation_column_name] = df[transformation_column_name].str.lower()
        elif transformation_type == TransformationType.StripSpaces:
            df[transformation_column_name] = df[transformation_column_name].str.strip()
        elif transformation_type == TransformationType.Capitalize:
            df[transformation_column_name] = df[transformation_column_name].str.capitalize()

        file_in_memory = dataframe_to_memory_file(df, file_format="csv")

        return StreamingResponse(
            file_in_memory,
            media_type="application/octet-stream",
            headers={"Content-Disposition": 'inline; filename="transformed_data.csv"'},
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during transformation: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1231)
