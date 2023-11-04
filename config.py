import asyncpg

db_pool = None


async def init_db_pool():
    global db_pool
    db_pool = await asyncpg.create_pool(
        database='database_name_3',
        user='postgres',
        password='qachonkelasan',
        host='localhost'
    )


async def close_db_pool():
    global db_pool
    if db_pool:
        await db_pool.close()


async def add_user(users_id, full_name, contact):
    try:
        async with db_pool.acquire() as conn:
            query = '''
            INSERT INTO beelene_bot (users_id, full_name, contact)
            VALUES ($1, $2, $3);
            '''
            await conn.execute(query, users_id, full_name, contact)
    except Exception as error:
        print(f'add:{error}')
        return None
