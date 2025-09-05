import asyncio
from playwright.async_api import async_playwright
import time

async def main():
    
    async with async_playwright() as p:
        navegador = await p.chromium.launch(headless=False)
        pagina = await navegador.new_page()
        
        try:
            await pagina.goto("https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/safe-temperature-chart", wait_until="networkidle", timeout=30000)
                
            encabezados = await pagina.locator("table#tablefield-paragraph-2721-field_table-0 thead tr th").all_inner_texts()
            print(f'los encabezados son : {encabezados}')
        except Exception as e:
            print(f"Error al cargar la pagina:{e}")
        
        await navegador.close()

asyncio.run(main())
        
    
        
