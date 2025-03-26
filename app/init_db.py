import asyncio
from app.db.session import engine
from app.db.base import Base
from app.models import user

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(lambda sync_conn:
            Base.metadata.create_all(bind=sync_conn)
        )


if __name__ == "__main__":
    asyncio.run(init_models())
