__author__ = 'WQ'
# *_*coding:utf-8 *_*
#appnium微信登录
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
server='http://localhost:4723/wd/hub'
TIMEOUT = 300
desired_caps={
    'platformName':'Android',
    'deviceName':'MI_6',
    'appPackage':'com.tencent.mm',
    'appActivity':'.ui.LauncherUI'
}


# MongoDB配置
MONGO_URL = 'localhost'
MONGO_DB = 'moments'
MONGO_COLLECTION = 'moments'

# 滑动点
FLICK_START_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 700

# 滑动间隔
SCROLL_SLEEP_TIME = 1

driver = webdriver.Remote(server,desired_caps)
wait=WebDriverWait(driver,TIMEOUT)


def login():
    login=wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/d75')))
    login.click()

    #qq登录
    cut=wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/c1t')))
    cut.click()
    qq=wait.until(EC.presence_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText')))
    qq.send_keys('1373734675')
    password=wait.until(EC.presence_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText')))
    password.send_keys('tjw5201314')

    ok=wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/c1u')))
    ok.click()
    '''
    手机号登录
    phone=wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/hz')))
    phone.send_keys('18872738629')
    next= wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/alr')))
    next.click()
    password=wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/hz')))
    password.send_keys('tjw5201314')
    ok= wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/alr')))
    ok.click()
    '''
    yes= wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/an3')))
    yes.click()


def friend():
    tab=wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@content-desc="当前所在页面,与wxid_0496004960212的聊天"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView[1]')))
    tab.click()
    friends= wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/aaf')))
    friends.click()



def crawl():
    """
        爬取
        :return:
        """
    while True:
        # 当前页面显示的所有状态
        items=wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@content-desc="当前所在页面,朋友圈"]')))
    # 上滑
    driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
    # 遍历每条状态
    for item in items:
        try:
            # 昵称
            nickname = item.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="当前所在页面,朋友圈"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView').get_attribute('text')
            # 正文
            content = find_element_by_xpath('//android.widget.FrameLayout[@content-desc="当前所在页面,朋友圈"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]').get_attribute('text')
            print(nickname, content)
            '''
            # 日期
            date = item.find_element_by_id('com.tencent.mm:id/crh').get_attribute('text')
            # 处理日期
            date = self.processor.date(date)
            print(nickname, content, date)
            data = {
                'nickname': nickname,
                'content': content,
                'date': date,
            }
            # 插入MongoDB
            self.collection.update({'nickname': nickname, 'content': content}, {'$set': data}, True)
            sleep(SCROLL_SLEEP_TIME)
            '''
        except TimeoutError:
            print('error')

if __name__ == '__main__':
    login()
    friend()
    crawl()