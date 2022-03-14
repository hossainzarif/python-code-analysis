
from selenium import webdriver

driver = webdriver.Chrome()
link="https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"
driver.get(link)

element = driver.find_elements_by_xpath("//input[@type='radio']")

lenth = len(element)

for button in element:
    if(button.is_selected()):
        lenth = lenth-1



print(lenth)