import time
from selenium import webdriver
#get the we driver 
driver = webdriver.Chrome('/Users/quintotechnologiespvtltd/Documents/chromedriver/chromedriver')  # Optional argument, if not specified will search path.


driver.get('http://facebook.com');
email = driver.find_element_by_name('email')
password = driver.find_element_by_name('pass')
email.send_keys('userid')
password.send_keys('password')
driver.find_element_by_id('loginbutton').click()

driver.get('group url')
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
					print "============================="
time.sleep(5) # Let the user actually see something!
driver.quit()