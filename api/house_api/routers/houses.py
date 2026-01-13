from fastapi import APIRouter
import service.house_service as house_service
import models.house_model as models


router = APIRouter()

@router.get("/houses")
async def get_all_houses():
    return await house_service.get_all_houses()

@router.get("/houses/{house_id}")
async def get_house_by_id(house_id: int):
    return await house_service.get_house_by_id(house_id)

@router.post("/houses")
async def create_house(data : models.HouseCreate):
    return await house_service.create_house(data)

@router.patch("/houses/{house_id}")
async def update_house(house_id: int, data: models.HouseUpdate):
    return await house_service.update_house(house_id, data)

@router.delete("/houses/{house_id}")
async def delete_house(house_id: int):
    return await house_service.delete_house(house_id)