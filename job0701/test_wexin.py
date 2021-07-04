from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeXin:
    def setup(self):
        # 打开手机端企业微信
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "hogwarts"
        caps["unicodeKeyBoard"] = "true"
        caps["resetKeyBoard"] = "true"
        caps["noReset"] = "true"
        caps["automationName"] = "uiautomator2"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_adduser(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 滚动查找 添加成员按钮，并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0))').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element_by_id('com.tencent.wework:id/b09').send_keys('糖糖')
        self.driver.find_element_by_id('com.tencent.wework:id/f7y').send_keys('13831123220')
        self.driver.find_element_by_id('com.tencent.wework:id/ad2').click()
        text_return = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "添加成功")]').text
        assert '添加成功' == text_return
        self.driver.find_element_by_id('com.tencent.wework:id/hbs').click()
        # 滚动查找 新添加的用户名
        user1 = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("糖糖").instance(0))').text
        assert '糖糖' == user1
