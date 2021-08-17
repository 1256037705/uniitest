from appium import webdriver

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# driver.find_element_by_name().click()

# mFocusedActivity: ActivityRecord{f79df71 u0 com.android.settings/.Settings t4}