from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import datetime
import urllib


import pytesseract
from PIL import Image

ID = 'C44051249'
password = 'HArry33316'

browser = webdriver.Chrome()

#找到作業系統
browser.get('https://course-query.acad.ncku.edu.tw/index.php?c=qry11215&i=X2BYMAIzVWgELwRyBWhWYANtUyZVaQNxVWtQb1QzATZXZgA3VzpbeVtpUTcKPFUmVWZQJgA4UWAGOVYxAGMELlBnUjoFMFJuUGFTbAZjVmsAL156UzwOa1JtA3cBLwN8VzECZAElBHdaaVFvCz1RMQBgDWEFPQIhAT5UM1U2UyBfclhvAmpVcARvBHIFaFZgA21TJlUxA3FVa1B7VGABPVdnADxXYFswW2JRPAp9VXdVP1AzADlRIwZnVmcAKQQhUFFSbgVvUndQO1MlBmtWZABuXitTOA55UhYDbAF7AydXbwJ4AT4Eb1pjUTQLN1E7ADENYwU3AmgBf1RzVTZTNV87WCgCZFU9BCcEbwUzVjwDMlMmVTsDIFVqUDdUOwE9V3YA41e8W5ZbtVGjCqtV41W2UL8A5FG0BrJWIABiBChQc1JzBTpSZFA6U3QGI1ZzAG9eaFM8Dm1SbQMuATUDP1dkAj4BPgRvWmJRPQtuUToAYQ1iBW8CaAE3VDtVZVM4XzNYMQJuVWgEZQQxBWJWagMqU3dVOgNiVWpQJFRuASVXbwBlVztbO1toUXs=')

time.sleep(2)
course = browser.find_element_by_xpath('//*[@id=\"main_content\"]/div[6]/table/tbody/tr[2]/td[4]')


#課程額滿則卡住
while( '額滿' in course.text ):
	time.sleep(5)
	browser.refresh()

browser.get('https://course.ncku.edu.tw/index.php?c=auth')

'''
用成功入口登入
browser.find_element_by_xpath("//*[@id=\"loginbg\"]/div/div/div[2]/a").click()

browser.find_element_by_xpath("//*[@id=\"userNameInput\"]").send_keys(ID);
browser.find_element_by_xpath("//*[@id=\"passwordInput\"]").send_keys(password);

browser.find_element_by_xpath("//*[@id=\"submitButton\"]").click()
'''

pic_path = 'screen.png'

verify = browser.find_element_by_xpath('//*[@id=\"loginbg\"]/div/div/div[4]/div[4]/span[2]/img')

#src = verify.get_attribute('src')
#嘗試取得src圖就會改
#urllib.request.urlretrieve(src, "captcha.png")


#用截圖的方式獲取驗證碼
browser.save_screenshot(pic_path)


img = Image.open('screen.png')
img = img.crop((910,624,973,648))#left top right bottom
#img.show()

#使用pytesseract做驗證碼文字辨識
pytesseract.pytesseract.tesseract_cmd = 'C://Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(img)
print(text)
print(text.isdigit())

text =  [x for x in text if x.isdigit()]

browser.find_element_by_xpath("//*[@id=\"user_id\"]").send_keys(ID);
browser.find_element_by_xpath("//*[@id=\"passwd\"]").send_keys(password);
browser.find_element_by_xpath("//*[@id=\"code\"]").send_keys(text);

browser.find_element_by_xpath("//*[@id=\"submit_by_acpw\"]").click()

#browser.close()

# 選課
#避免server擁擠 selenium 點不到物件產生 exception
while(1):
	try:
		browser.find_element_by_partial_link_text('第２階段一般暨志願課程').click()
		break
	except:
		time.sleep(5)

while(1):
	try:
		browser.find_element_by_xpath("//tr[2]//td[1]//a[1]").click()
		break
	except:
		time.sleep(5)


browser.switch_to.frame("mainframe")

browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[1]/input").send_keys('F7')
browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[2]/input").send_keys('119')
