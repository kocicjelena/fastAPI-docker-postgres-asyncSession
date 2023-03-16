from msilib.schema import Patch
from uuid import UUID

from fastapi import HTTPException
from fastapi import status as http_status
from sqlalchemy import delete, select
from full.fast.models import StaffBase
from full.fast.schemas import Create
from sqlmodel.ext.asyncio.session import AsyncSession




class Staff:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: Create) -> StaffBase:
        values = data.dict()

        st = StaffBase(**values)
        self.session.add(st)
        await self.session.commit()
        await self.session.refresh(st)

        return st

    async def get(self, st_id: str | int) -> StaffBase:
        statement = select(
            StaffBase
        ).where(
            StaffBase.id == st_id
        )
        results = await self.session.execute(statement=statement)
        st = results.scalar_one_or_none()  # type: StaffBase | None

        if st is None:
            raise HTTPException(
                status_code=http_status.HTTP_404_NOT_FOUND,
                detail="Your staff hasn't been found!"
            )

        return st

    async def patch(self, st_id: str | int, data: Patch) -> StaffBase:
        st = await self.get(st_id=st_id)
        values = data.dict(exclude_unset=True)

        for k, v in values.items():
            setattr(st, k, v)

        self.session.add(st)
        await self.session.commit()
        await self.session.refresh(st)

        return st

    async def delete(self, st_id: str | int) -> bool:
        statement = delete(
            StaffBase
        ).where(
            StaffBase.id == st_id
        )

        await self.session.execute(statement=statement)
        await self.session.commit()

        return True
