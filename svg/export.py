from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options, executable_path='c:/users/zzzzz/chromedriver.exe')
driver.get('file:///c:/users/zzzzz/its-pages-all-the-way-down/svg/more_cards.svg')
driver.set_page_load_timeout(10)
driver.set_window_size(4000,4000)
driver.get_screenshot_as_file('./poo.png')