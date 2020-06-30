from selenium import webdriver

my_url = 'https://www.steamstatus.io/'

driver = webdriver.Chrome(r'C:\Users\a864\Downloads\chromedriver_win32\chromedriver.exe')
driver.get(my_url)
storeStatus = driver.find_elements_by_xpath('//*[@id="statustables"]/div[1]/div/div[1]/div[2]')[0].text
communityStatus = driver.find_elements_by_xpath('//*[@id="statustables"]/div[1]/div/div[2]/div[2]')[0].text
webAPI = driver.find_elements_by_xpath('//*[@id="statustables"]/div[1]/div/div[3]/div[2]')[0].text
euWest = driver.find_elements_by_xpath('//*[@id="statustables"]/div[2]/div/div[6]/div[2]')[0].text

print('Steam Store Status:', storeStatus)
print('Steam Community Status:', communityStatus)
print('Steam Web API Status:', webAPI)
print('Steam EU West Server Status:', euWest)

driver.close()
