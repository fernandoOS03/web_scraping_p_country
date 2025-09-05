from playwright.async_api import async_playwright
from connection_to_sheet import sheet3
import asyncio
import json
import time

async def main():
    async with async_playwright() as p:
        navegador = await p.chromium.launch(headless=False)
        pagina = await navegador.new_page()
        
        await pagina.goto("https://www.retailgators.com/nutrition-data-scraping.php")
        # text = await pagina.locator("div.services-content-wrap h5").all_inner_texts()
        # description = await pagina.locator("div.services-content-wrap p").all_inner_texts()
        
        divs = await pagina.locator("div.services-content-wrap").all()
       
        data =[]
        for div in divs:         
            text = await div.locator('h5').all_inner_texts()
            description  = await div.locator('p').all_inner_texts()
            
            item = {
                "title": text[0],
                "description": description[0]
            }
            data.append(item)
        
        # Imprime el json en consola
        # json_data = json.dumps(data, ensure_ascii=False, indent=2)
        # print(json_data)
        
        with open('retail_gators.json', 'w',encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
              
        time.sleep(5)
        
        print("Datos guardados en retail_gators.json")
        await navegador.close()
        
        # ----------Enviar datos a Google Sheets----------

        #limpiamos la hoja
        sheet3.clear()
        
        #Agregamos las llaves como encabezados
        if data:
            encabezados = list(data[1].keys())
            sheet3.append_row(encabezados)
            
        for fila in data:
            sheet3.append_row(list(fila.values()))
            time.sleep(2)
        print("Datos enviados a Google Sheets")
        
asyncio.run(main())
    