import uvicorn
from fastapi import FastAPI

from appointment_mail_notifier.api import healthcheck_api

REST_API_HOST = "0.0.0.0"
REST_API_PORT = 8000

app = FastAPI()
app.include_router(healthcheck_api.router)


def run():
    uvicorn.run(
        "appointment_mail_notifier.api.main_api:app",
        host=REST_API_HOST,
        port=REST_API_PORT,
        reload=True,
    )
