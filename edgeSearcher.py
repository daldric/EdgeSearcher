import time
from sqlalchemy import false, true
from selenium import webdriver
from selenium.webdriver.common.by import By
from msedge.selenium_tools import EdgeOptions

# shell commands to run the generated script
# cd ~/Downloads/coding/edgeSearcher
# export PATH=$PATH:~/Downloads/coding/edgeSearcher - this is for msedgedriver
# ./edgeSearcher 

edgeOptions = EdgeOptions()
edgeOptions.use_chromium = true
edgeOptions._ignore_local_proxy = false
edgeOptions.add_argument("user-data-dir=C:\\Users\\dillonaldrich\\AppData\\Local\\Microsoft\\Edge\\User Data")
edgeOptions.add_argument("profile-directory=Default")
driver = webdriver.Edge(options = edgeOptions)

driver.get('https://bing.com/')
searches = ['anakin skywalker', 'obi wan', 'luke skywalker', 'han solo', 'din jarin', 'ashoka', 'yoda', 'dooku', 'r2d2', 
    'chewbacca', 'leia', 'bd-1', 'k2so', 'cal kestis', 'palpatine', 'kit fisto', 'plo koon', 'mace windu', 'saw guerrera',
    'bo katan', 'grogu', 'boba fett', 'captain rex', 'darth maul', 'padme', 'c3p0', 'ki-adi-mundi', 'aayla secura', 
    'poggle the lesser', 'echo clone trooper']

for search in searches:
    searchBar = driver.find_element(By.ID, 'sb_form_q')
    searchBar.clear()
    searchBar.send_keys(search)
    searchBar.submit()
    time.sleep(1.5)
driver.quit()
time.sleep(1.5)

# mobile browser instance
mobile_emulation = {
     "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
     "userAgent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 Edg/92.0.902.78"
 }
edgeOptions.add_experimental_option("mobileEmulation", mobile_emulation)
mobileDriver = webdriver.Edge(options = edgeOptions)
mobileDriver.get('https://bing.com/')
mobileSearches = ['iroh', 'zuko', 'aang', 'katara', 'sokka', 'toph', 'the boulder atla', 'tai lee avatar', 'mai avatar', 'ozai',
    'momo atla', 'appa atla', 'azula atla', 'legend of korra', 'mako korra', 'tenzin', 'oogi korra', 'opal korra', 'nala korra', 'bolin korra']

for mobileSearch in mobileSearches:
    searchBar = mobileDriver.find_element(By.ID, 'sb_form_q')
    searchBar.clear()
    searchBar.send_keys(mobileSearch)
    searchBar.submit()
    time.sleep(1.5)
time.sleep(1.5)
mobileDriver.quit()