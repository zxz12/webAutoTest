from selenium import webdriver

from webtest.aw.CONSTANT import CONSTANT

driver = webdriver.Chrome(CONSTANT.CHROME_DRIVER_PATH)
x = driver.get_window_rect()
print(x)

print('test marge')
