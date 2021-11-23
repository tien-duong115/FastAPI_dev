from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = r"C:\\Program Files\\Chrome\\chrome64_55.0.2883.75\\chrome.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:\Users\tienl\OneDrive\Desktop\Python_stuff\tien_virtual_env\chromedriver_win32\chromedriver.exe')
driver.get('http://google.com/')
print("Chrome Browser Invoked")
driver.quit()