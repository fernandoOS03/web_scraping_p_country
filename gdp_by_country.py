import _asyncio
from playwright.async_api import async_playwright
import json


async def mai():
    
    async with async_playwright() as p:
        browser = await p