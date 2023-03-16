from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from full.core.db import get_async_session
from full.fast.routers.helper import Staff


async def get_staff(
        session: AsyncSession = Depends(get_async_session)
) -> Staff:
    return Staff(session=session)
