from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.routers import dependencies

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}