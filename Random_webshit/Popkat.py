from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time as t

PATH = 'E:/drive/chromedriver.exe'

driver = webdriver.Chrome(PATH)
Cur_time = t.time()
driver.get('https://popcat.click/')

if t.time() - Cur_time < 3600:
    Script =  "var ev = new KeyboardEvent('keydown',{key:'d',ctrlKey:true});setInterval(function(){for(i = 0; i<800; i++){document.dispatchEvent(ev);}},0);"
    driver.execute_script(Script)
else:
    driver.close()