from fastapi import APIRouter, Depends
from fastapi import status as http_status

from full.core.models import StatusMessage
from full.fast.routers.helper import Staff
from full.fast.dependencies import get_staff
from full.fast.schemas import Create, Patch, Read
from core.db import async_engine
import models
router = APIRouter(
    prefix="/staff",
    tags=["staff"],
    responses={404: {"description": "Not Found"}}
)

models.Base.metadata.create_all(bind=async_engine)

@router.post(
    "",
    response_model=Read,
    status_code=http_status.HTTP_201_CREATED
)
async def create_st(
        data: Create,
        sts: Staff = Depends(get_staff)
):
    st = await sts.create(data=data)

    return st


@router.get(
    "/{st_id}",
    response_model=Read,
    status_code=http_status.HTTP_200_OK
)
async def get_st_by_id(
        st_id: str,
        sts: Staff = Depends(get_staff)
):
    st = await sts.get(st_id=st_id)

    return st


@router.patch(
    "/{st_id}",
    response_model=Read,
    status_code=http_status.HTTP_200_OK
)
async def patch_st_by_id(
        st_id: str,
        data: Patch,
        sts: Staff = Depends(get_staff)
):
    st = await sts.patch(st_id=st_id, data=data)

    return st


@router.delete(
    "/{st_id}",
    response_model=StatusMessage,
    status_code=http_status.HTTP_200_OK
)
async def delete_st_by_uuid(
        st_id: str,
        sts: Staff = Depends(get_staff)
):
    status = await sts.delete(st_id=st_id)

    return {"status": status, "message": "Deleted!"}
