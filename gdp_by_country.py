import asyncio
from playwright.async_api import async_playwright
import json
from connection_to_sheet import sheet2
import time

async def main():
    #Inciamos playwright
    async with async_playwright() as p:
        #Abrimos el navegador
        browser = await p.chromium.launch(headless=False)
        page =await browser.new_page()
        
        #Navegamos a la pagina
        await page.goto("https://www.worldometers.info/gdp/gdp-by-country/")
        
        #obtener los encabezados
        
        encabezados = await page.locator("table.datatable thead tr th").all_inner_texts()
        
        filas = page.locator("table.datatable tbody tr")
        
        numero_filas = await filas.count()
        
        datos =[]
        
        for i in range(numero_filas):
            celdas = await filas.nth(i).locator("td").all_inner_texts()
            fila_dic = dict(zip(encabezados,celdas))
            datos.append(fila_dic)
        
        with open("gdp_by_country.json","a", encoding="utf-8") as f:
            json.dump(datos,f,ensure_ascii=False, indent=2)
            
        print("Datos guardados como gdp_by_country.json")
        
        await browser.close()
        
        sheet2.clear()
        sheet2.append_row(encabezados)
        
        for fila in datos:
          sheet2.append_row(list(fila.values()))
          time.sleep(3)  # Pausa para evitar exceder el límite de solicitudes
        
        

asyncio.run(main())