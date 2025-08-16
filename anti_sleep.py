import schedule
import time
import asyncio
import asyncpg
from datetime import datetime
from decouple import config

ultima_execucao = None

async def wake_db_async():
    try:
        conn = await asyncpg.connect(
            database=config('DB_NAME'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            host=config('DB_HOST'),
            port=int(config('DB_PORT')),
        )
        result = await conn.fetchrow("SELECT NOW();")
        print(f"[{datetime.now()}] Banco acordado! Hora do servidor: {result['now']}")
        await conn.close()
    except Exception as e:
        print(f"Erro ao acordar o banco: {e}")

def wake_db():
    global ultima_execucao
    agora = datetime.now()

    if ultima_execucao is None or (agora - ultima_execucao).days >= 6:
        print(f"Acordando banco em {agora}...")
        asyncio.run(wake_db_async())
        global ultima_execucao
        ultima_execucao = agora
    else:
        print(f"Hoje ({agora.date()}) não precisa acordar ainda.")

schedule.every().day.at("09:00").do(wake_db)

while True:
    schedule.run_pending()
    time.sleep(86400)  # espera 24 horas antes de checar de novo