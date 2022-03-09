from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.shared.exceptions.bad_exception import BadRequestException
from src.shared.exceptions.precondition_failed_exception import PreconditionFailedException


def init_app(app: FastAPI):

    @app.exception_handler(BadRequestException)
    def bad_request_error(request: Request, error: BadRequestException):
        return JSONResponse(
            status_code=error.status_code,
            content={
                "response": error.status_code,
                "data": error.to_dict(),
                "message": error.message
            }
        )

    @app.exception_handler(PreconditionFailedException)
    def Precondition_failed_error(request: Request, error: PreconditionFailedException):
        return JSONResponse(
            status_code=error.status_code,
            content={
                "response": error.status_code,
                "data": error.to_dict(),
                "message": error.message
            }
        )