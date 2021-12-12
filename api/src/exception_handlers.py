from fastapi import status, Request, FastAPI
from starlette.responses import JSONResponse

from api.src.exceptions import InvalidOperationException
from api.src.utils import create_message_response


async def invalid_operation_exception_handler(request: Request, exc: InvalidOperationException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=create_message_response(exc.message))


def add_user_exception_handlers(app: FastAPI):
    app.add_exception_handler(InvalidOperationException, invalid_operation_exception_handler)
