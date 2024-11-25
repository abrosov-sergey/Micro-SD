import logging
from fastapi import Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import contains_eager
from sqlalchemy import select, func
from uuid import UUID
from datetime import datetime
from fastapi import APIRouter


router = APIRouter(prefix="/test", tags=["test"])


@router.get("/tour")
async def aboutTour():
    logging.info('wazzup')
    print('waxap')

    return Response(status_code=200)

