from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


opt = Options()
opt.add_argument("start-maximized")
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications": 1
})



driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.get("https://mail.google.com/mail/u/8/#inbox")
search = driver.find_element_by_name("identifier")
search.send_keys("Your mail id")
search.send_keys(Keys.RETURN)
driver.implicitly_wait(5)
search = driver.find_element_by_name("password")
search.send_keys("Your password")
search.send_keys(Keys.RETURN)
sleep(3)
mail=driver.find_element_by_xpath('//*[@id=":2d"]').click()
sleep(3)
try:
    service2 = driver.find_element_by_xpath('//*[@id=":p3"]/div[1]/a').click()
except:
    sleep(3)
    service2=driver.find_element_by_xpath('//*[@id=":p9"]/div[1]/a').click()



sleep(3)
try:
    microphone=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div/div[1]').click()
except:
    microphone1=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
camera=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div/div[1]').click()
join=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span').click()

