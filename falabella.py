import asyncio
import time
import json
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        navegador = await p.chromium.launch(headless = False)
        page = await navegador.new_page()
        
        await page.goto("https://www.falabella.com.pe/falabella-pe")
        
        await page.locator("button.airship-btn-deny").click()
        
        await page.locator("#testId-HamburgerBtn-toggle > div.MarketplaceHamburgerBtn-module_icon__r2oRR").click()
        await page.locator("#scrollable-content > div > div.Taxonomy-module_HamburgerBtnWrapper__oNEG4 > div > div.TaxonomyDesktop-module_sidebar__1lDbW > div.TaxonomyDesktop-module_scrollWrapper__sZu3u > div:nth-child(1) > div:nth-child(2) > div").click()
        await page.locator("#scrollable-content > div > div.Taxonomy-module_HamburgerBtnWrapper__oNEG4 > div > div.SecondLevelCategories-module_secondLevelMenuContainer__I3RRy > div > div.SecondLevelCategories-module_subCategoryContent__c8yUJ > div > ul:nth-child(1) > li:nth-child(3) > a").click()
        
        #selecciona marca de telefono
        await page.locator("#topper-filtros-tienda > div:nth-child(1) > a > img").click()
        
        #selecciona modelo de telefono
        await page.locator("#topper-filtros-tienda > div:nth-child(1) > a > img").click()
        
        
        ##------------------Extraccion de data----------------
        
        cards = page.locator('div.jsx-3752256814')
        cantidad = await cards.count()
        print (f"hay {cantidad} tarjetas")
        
        data = []
        print("Extrayendo datos...")
        for i in range(cantidad):
            card = cards.nth(i)
            model = await card.locator("b").all_inner_texts()
            desciption = await card.locator("b.pod-subTitle").all_inner_texts()
            vendedor = await card.locator("b.pod-sellerText").all_inner_texts()
            precio_descuento  = await card.locator("li[data-event-price] span.copy10.primary.medium").inner_text()

            #precio_original = await card.locator("b.copy3").all_inner_texts()
           
            item = {
                "Modelo": model[0] if model else None,
                "Descripcion" : desciption[0] if desciption else None,
                "Vendedor" : vendedor[0] if vendedor else None,
                "Precio con Descuento" : precio_descuento[0] if precio_descuento else None,
                #"Precio Normal" : precio_original[0] if vendedor else None,
            }
            
            data.append(item)
           
        with open ("fabella.json","w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Armando Json...")
        
        print("Datos guardados en falabella.json")
        
        await navegador.close()

asyncio.run(main())

        


