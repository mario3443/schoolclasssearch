from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  

service = Service("chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://course.ncku.edu.tw/index.php?c=qry_all")

print("網頁標題：", driver.title)

driver.quit()
