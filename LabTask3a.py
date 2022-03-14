
from selenium import webdriver

driver = webdriver.Chrome()
link="https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"
driver.get(link)

element = driver.find_element_by_id("RESULT_TextField-1")
element.send_keys("some text")
element_2 = driver.find_element_by_id("RESULT_TextField-2")
element_2.send_keys("some textajsdjkahsjkdhjakshdhasdhahdjk")
print(len(element_2.get_attribute("value")))
print(len(element.get_attribute("value")))

