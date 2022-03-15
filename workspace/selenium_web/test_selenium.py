from selenium.webdriver import Chrome

def test_selenium():
    driver = Chrome()
    driver.get("http://www.baidu.com")
    el=driver.find_element("id","kw")
    el.send_keys("阿里")
    el.submit()
    driver.quit()
