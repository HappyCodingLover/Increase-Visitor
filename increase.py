from selenium import webdriver

path = r'C:\\Chromedriver'
browser = webdriver.Chrome(executable_path = path)
browser.get('https://github.com/anaconda0905')
js = "location.reload();"
for i in range(0,100000):
    browser.execute_script(js)
    browser.implicitly_wait(1)
browser.close()