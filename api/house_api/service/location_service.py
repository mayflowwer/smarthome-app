from validation_models.location_model import CreateLocation, UpdateLocation
from db.engine import get_session
from sqlmodel import select
from db.db_models import Location
import json

async def get_all_locations():
    '''Get all locations'''
    session = get_session()
    query_stm = select(Location)
    location_objs = session.exec(query_stm)
    session.close()
    return json.dumps(location_objs)

async def get_location_by_id(location_id: int):
    """Получить локацию по ID"""
    session = get_session()
    query_stm = select(Location).where(Location.id == location_id)
    location_obj = session.exec(query_stm).first()
    session.close()
    return json.dumps(location_obj)

async def create_location(location: CreateLocation):
    '''Create location in db'''
    session = get_session()
    session.add(location)
    session.commit()
    session.close()

async def update_location(location_id: int, data: UpdateLocation):
    """Обновить локацию"""
    session = get_session()
    query_stm = select(Location).where(Location.id == location_id)
    location_obj = session.exec(query_stm).first()
    data_from_json_str = json.load(data)
    location_obj.name = data_from_json_str.name
    session.add(location_obj)
    session.commit()
    session.close()

async def delete_location(location_id: int):
    """Удалить локацию"""
    pass