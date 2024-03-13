from core.configs import settings
from core. database import engine


async def create_tables() -> None:
    import models.__all_models
    print('Criando as tableas no banco de dados...')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabelas criadas cp, sucesso.')

if __name__ == '__main__':
    import asyncio
    
    #asyncio.run(create_tables())