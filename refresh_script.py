
import time

from selenium import webdriver


options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary =r"C:\Users\tienl\OneDrive\Desktop\Python_stuff\tien_virtual_env\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_binary, chrome_options=options)
driver.get('http://google.com')



while True:
    time.sleep(10)
    driver.refresh()
    
driver.quit()

