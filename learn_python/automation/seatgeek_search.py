from selenium.webdriver import Chrome
# from selenium.webdriver.firefox.options import Options
browser = Chrome()
browser.get('https://seatgeek.com')
search_form = browser.find_element_by_id('search-input')
search_form.send_keys('yankees')
search_form.submit()
events = browser.find_elements_by_class_name('Desktop__Title')
# results.click()
print(events)
browser.close()
quit()
