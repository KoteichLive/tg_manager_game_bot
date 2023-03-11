from aiogram.utils import executor
from bor_ import dp
from handlers import other
import asyncio

async def Time_(_):
   await asyncio.sleep(50)

other.register_other(dp)
print(1)

#if __name__ == '__main__':
executor.start_polling(dp)