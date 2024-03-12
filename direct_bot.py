from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# Username and password of your linkedin account:
my_username = ''
my_password = ''


browser = webdriver.Chrome(options=options)

# Authorization:
def auth(username, password):
		browser.get('https://www.linkedin.com/')
		browser.implicitly_wait(3)

		input_username = browser.find_element(By.ID,'session_key')

		input_password = browser.find_element(By.ID,'session_password')
		
		
		input_username.send_keys(username)
		input_password.send_keys(password)
		input_password.send_keys(Keys.ENTER)

		browser.implicitly_wait(5)
		profile = browser.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[6]')
		profile.click()
		open_profile = browser.find_element(By.XPATH, '//*[@id="ember24"]/div[2]/div/div/div/div/div[1]/div[1]')
		open_profile.click()
		browser.implicitly_wait(3)
		nama = browser.find_element(By.CSS_SELECTOR, "h1.text-heading-xlarge").get_attribute("innerText")
		headline = browser.find_element(By.CSS_SELECTOR, "div.text-body-medium").get_attribute("innerText")
		location = browser.find_element(By.CSS_SELECTOR, "span.text-body-small.inline").get_attribute("innerText")

		print("Nama: {}".format(nama))
		print("Headline: {}".format(headline))
		print("Location: {}".format(location))

auth(my_username, my_password)