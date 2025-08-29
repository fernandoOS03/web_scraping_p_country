import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless = False)
        page = await browser.new_page()
        await page.goto("https://www.worldometers.info/world-population/population-by-country/")
        await page.wait_for_load_state("networkidle")
        
        #Espera a que la tabla este visible, esto para las paginas que sean dinamicas
        await page.wait_for_selector('body > div > div.container.min-h-\[500px\].grow.py-4 > div.prose.max-w-none.text-sm\/5.md\:text-base\/6.prose-table\:text-sm\/5.md\:prose-table\:text-base\/6.prose-headings\:font-medium.prose-headings\:mt-10.prose-h1\:text-4xl.prose-h1\:font-medium.prose-h1\:mb-8.prose-h2\:text-3xl.prose-h3\:text-2xl.prose-tr\:border-0.prose-thead\:border-0.prose-img\:mb-0.prose-a\:font-inherit.prose-li\:my-0\.5 > div:nth-child(3) > div')
        
        #Localizamos todas las filas de las tablas, incluyendo las cabeceras
        
        rows = await page.locator("body > div > div.container.min-h-\[500px\].grow.py-4 > div.prose.max-w-none.text-sm\/5.md\:text-base\/6.prose-table\:text-sm\/5.md\:prose-table\:text-base\/6.prose-headings\:font-medium.prose-headings\:mt-10.prose-h1\:text-4xl.prose-h1\:font-medium.prose-h1\:mb-8.prose-h2\:text-3xl.prose-h3\:text-2xl.prose-tr\:border-0.prose-thead\:border-0.prose-img\:mb-0.prose-a\:font-inherit.prose-li\:my-0\.5 > div:nth-child(3) > div > div.datatable-container > table > thead > tr > th.px-2.border-e.border-zinc-200.align-middle.text-center.font-semibold.border-b-3.py-1.datatable-ascending").all()
        
        all_data = []
        
        print("Automatizacion exitosa")
        
        await browser.close()

asyncio.run(main())