# check when “Software Testing Tutorials” is clicked, it redirects to
# https://www.pavantestingtools.com/ and there are 5 elements in top navbar of the
# website.



from selenium import webdriver
import webbrowser
driver = webdriver.Chrome()
link="https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"
driver.get(link)

element = driver.find_element_by_xpath("/html/body/form/div[2]/div[23]/div/a")
element.click()

current_link= driver.current_url

print(current_link)
driver.get(current_link)

nav = driver.find_elements_by_id("menu-primary-items")
# id=

lenth = len(nav)
print(lenth)
#
# for button in element:
#     if(button.is_selected()):
#         lenth = lenth-1


