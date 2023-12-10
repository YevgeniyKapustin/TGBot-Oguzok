import asyncio

from loguru import logger

from src.main import main

if __name__ == "__main__":
    logger.add('.log')
    asyncio.run(main())
