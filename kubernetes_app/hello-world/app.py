import uvicorn
from fastapi import FastAPI
from routes.test_route import router
from fastapi.responses import HTMLResponse


app = FastAPI()
app.include_router(router)



@app.get("/", status_code=200, name="root")
def get_root():
    content=f"""
        <html>
        <head><title>sample app</title></head>
        <body>
        <h1>sample app</h1>
        """
    content+=f"""
        <p><a href='https://localhost:5000/docs'>Swagger UI</a></p>
        """

    return HTMLResponse(content=content)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
