from fastapi import FastAPI
from app_credits.endpoints.plan_routes import plan_router
from app_credits.endpoints.credit_routes import credit_router
from sqlalchemy.exc import IntegrityError

from app_credits.exceptions import (
    AppException,
    NotFoundError,
    NotFoundUserError,
    ValidationError,
    DatabaseIntegrityError,
    AlreadyExistsError
)

from app_credits.exceptions.handlers_exc import (
    app_exception_handler,
    general_exception_handler,
    integrity_error_handler,
    not_found_exception_handler,
    not_found_user_error_handler,
    validation_exception_handler
)

app = FastAPI()

app.add_exception_handler(NotFoundUserError, not_found_user_error_handler)

app.add_exception_handler(NotFoundError, not_found_exception_handler)
app.add_exception_handler(ValidationError, validation_exception_handler)
app.add_exception_handler(AlreadyExistsError, app_exception_handler)

app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(IntegrityError, integrity_error_handler)
app.add_exception_handler(Exception, general_exception_handler)


app.include_router(plan_router)
app.include_router(credit_router)
