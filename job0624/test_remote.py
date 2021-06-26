import time
import pytest
import yaml
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.mark.skip
# 复用浏览器，拿到cookie
def test_remote_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = '127.0.0.1:9222'
    # 将opt传给webdriver.Chrome()
    driver = webdriver.Chrome(options=opt)
    # 访问企业微信登录后的首页
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    driver.find_element_by_id("menu_contacts").click()
    # 在复用的基础上获取cookie，并存入yaml文件中
    cookies = driver.get_cookies()
    with open("./datas/cookiedata.yml", "w", encoding="UTF-8") as f:
        yaml.safe_dump(cookies, f)
    # 注：在复用模式下quit是不起效的，因复用是在debug模式下进行的
    driver.quit()


# 以下是非复用模式的代码因无options，以下代码执行时会重新打开一个窗口
def test_login_add():
    driver = webdriver.Chrome()
    # 访问企业微信登录页
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    # 从yaml文件中读取cookie
    with open("./datas/cookiedata.yml", encoding="UTF-8") as f:
        cookie_data = yaml.safe_load(f)
    # 添加cookie
    for cookie in cookie_data:
        driver.add_cookie(cookie)
    # 访问企业微信登录成功后的首页，并点击 通讯录
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    driver.find_element_by_id("menu_contacts").click()
    time.sleep(5)
    # 判断用户是否存在，不存在进行添加
    try:
        ele = driver.find_element(By.XPATH, '//*[@id="member_list"]//*[@title="13831121001"]')
        if ele:
            print("该用户已存在！！")
    except NoSuchElementException:
        driver.find_element(By.CSS_SELECTOR, '.js_operationBar_footer .js_add_member').click()
        time.sleep(3)
        # 输入 用户名、帐号、
        driver.find_element_by_id("username").send_keys("姚姚")
        driver.find_element_by_id("memberAdd_acctid").send_keys("test005")
        driver.find_element_by_id("memberAdd_phone").send_keys("13831121001")
        driver.find_element_by_link_text("保存").click()
    time.sleep(3)
    driver.quit()
