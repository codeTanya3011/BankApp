from fastapi import APIRouter, Depends
from ..data_base import UnitOfWork, get_unit_of_work
from ..services import CreditService
from ..schemas.credit_schema import UserCreditsListResponse

credit_router = APIRouter(prefix="/user_credits", tags=["Credits"])


@credit_router.get("/{user_id}", response_model=UserCreditsListResponse)
async def get_user_credits(
    user_id: int,
    uow: UnitOfWork = Depends(get_unit_of_work)
):
    return await CreditService.get_user_credits(user_id=user_id, uow=uow)