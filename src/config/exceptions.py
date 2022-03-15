from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException

from src.shared.exceptions.bad_exception import BadRequestException
from src.shared.exceptions.precondition_failed_exception import PreconditionFailedException
from src.shared.exceptions.not_found_exception import NotFoundException
from src.shared.exceptions.unauthorized_exception import UnauthorizedException


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
    
    @app.exception_handler(NotFoundException)
    def Precondition_failed_error(request: Request, error: NotFoundException):
        return JSONResponse(
            status_code=error.status_code,
            content={
                "response": error.status_code,
                "data": error.to_dict(),
                "message": error.message
            }
        )
    
    @app.exception_handler(UnauthorizedException)
    def Unauthozied_error(request: Request, error: UnauthorizedException):
        return JSONResponse(
            status_code=error.status_code,
            content={
                "response": error.status_code,
                "data": error.to_dict(),
                "message": error.message
            }
        )
    
    @app.exception_handler(AuthJWTException)
    def jwt_error(request: Request, error: AuthJWTException):
        return JSONResponse(
            status_code=error.status_code,
            content={
                "response": error.status_code,
                "message": error.message
            }
        )