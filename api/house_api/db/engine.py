from sqlmodel import SQLModel, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
import os
from dotenv import load_dotenv


abstr_file_path = os.path.abspath(__file__)
curr_file_path = os.path.dirname(abstr_file_path)
dotenv_path = os.path.join(os.path.dirname(curr_file_path), '.env')
load_dotenv()

DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{os.getenv('POSTGRES_USER')}:" 
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('DATABASE_HOST', 'db')}:"
    f"{os.getenv('DATABASE_PORT', '5432')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True
)

async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()


async def close_db():
    await engine.dispose()
