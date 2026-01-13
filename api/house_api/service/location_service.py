# service/location_service.py

async def get_all_locations():
    """Получить все локации"""
    # Вызов repository
    pass

async def get_location_by_id(location_id: int):
    """Получить локацию по ID"""
    pass

async def get_locations_by_house_id(house_id: int):
    """Получить все локации для дома"""
    # SELECT * FROM locations WHERE house_id = ?
    pass

async def create_location(data):
    """Создать локацию"""
    # Проверить, существует ли дом с house_id
    # Создать локацию
    pass

async def update_location(location_id: int, data):
    """Обновить локацию"""
    pass

async def delete_location(location_id: int):
    """Удалить локацию"""
    pass