import re
import time 
from playwright.sync_api import sync_playwright
import config
if __name__ == '__main__':
    
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto('https://www.apple.com/la/iphone/', wait_until="networkidle")
        
        selector = "#feature-card-1 > button"
        page.wait_for_selector(selector, timeout=10000)
        page.click(selector)
        print(selector)
        time.sleep(10)
        #page.selector("body > div.container > div > div > div:nth-child(3) > a.btn.ic_download_win").click()
   
        
        print("Script Completed")
        
    
    
    
    
    
    