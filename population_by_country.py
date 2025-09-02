import asyncio
from playwright.async_api import async_playwright
import json
from connection_to_sheet import sheet
import time
# class CLASS_NAME(TemplateView):
#     template_name = "TEMPLATE_NAME"


async def main():
    #Primer se inicia playwright
    async with async_playwright() as p:
        
        #Abrir el navegador 
        browser = await p.chromium.launch(headless=False) #True para no ver la ventana   
        page = await browser.new_page()
        
        # Ir a la pagina web
        await page.goto("https://www.worldometers.info/world-population/population-by-country/")
    
        encabezados = await page.locator("table.datatable thead tr th").all_inner_texts()
        
        #obtener las filas de la tabla  
        filas =  page.locator("table.datatable tbody tr")
        numero_filas = await filas.count()
        
        datos = []
        
        for i in range(numero_filas):
            celdas = await filas.nth(i).locator("td").all_inner_texts()
            fila_dic = dict(zip(encabezados,celdas))
            datos.append(fila_dic)
        
        with open("population_by_world.json","w", encoding= "utf-8") as f:
            json.dump(datos,f,ensure_ascii=False, indent=2)
            
        print("Datos guardados en Tabla.json")
              
        #Cerrar el navegador
        await browser.close()
        
        sheet.clear()
        sheet.append_row(encabezados)
        for fila in datos:
            sheet.append_row(list(fila.values()))
            time.sleep(5)  # Pausa para evitar exceder el límite de solicitudes
    
        
#ejecutar        
asyncio.run(main())


