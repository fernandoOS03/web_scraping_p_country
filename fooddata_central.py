import asyncio
from playwright.async_api import async_playwright
import json



async def main():
    
    async with async_playwright() as f:
        
        browser = await f.chromium.launch(headless = False)
        page = await browser.new_page()
        
        await page.goto("https://world.openfoodfacts.org/")
        
        await page.wait_for_selector("#products_match_all > li > a > div > div.list_product_name")
        card = await page.query_selector_all("#products_match_all > li > a > div > div.list_product_name")
        
        datos =[]
        
        for element in card:
            text = await element.inner_text()
            datos.append(text.strip())
            
        with open("fooddata_central.json","w", encoding= "utf-8") as f:
            json.dump(datos,f,ensure_ascii=False, indent=2)
        
        print("Datos guardados en fooddata_central.json")
        await browser.close()

asyncio.run(main())
            
        
