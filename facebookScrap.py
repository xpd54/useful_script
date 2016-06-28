
import time
from selenium import webdriver
#get the web driver
driver = webdriver.Chrome('path to chromedriver')

driver.get('http://facebook.com');
email = driver.find_element_by_name('email')
password = driver.find_element_by_name('pass')
email.send_keys('your facebook id')
password.send_keys('your facebook password')
driver.find_element_by_id('loginbutton').click()
driver.get('link of group you wanna get the posts')
page = 0
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    page = page + 1
    print 'Page Number ',page
    if page == 'Number of time you wanna scroll and then get the content': #will come back with better solution
            break
    time.sleep(1)
postContent = driver.find_elements_by_id('contentArea')
for content in postContent:
        pageGroup = content.find_elements_by_id('pagelet_group_mall')
	for page in pageGroup:
		userContent = page.find_elements_by_class_name('_3ccb')
		for element in userContent:
			div = element.find_elements_by_css_selector("div[class='_5pbx userContent']")
			for tag in div:
				plist = tag.find_elements_by_tag_name('p')
				for text in plist:
					print text.get_attribute('innerText')
                                print '==============================='
time.sleep(5) # Let the user actually see something!
driver.quit()
