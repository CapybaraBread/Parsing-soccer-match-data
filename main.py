from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas 
custom_options = Options()
custom_options.add_argument("--start-maximized")
path_driver = Service('chromedriver.app')
driver = webdriver.Chrome(options=custom_options)
link = "https://www.flashscore.com.ua/"
driver.get(link)
class_name = "event__match--twoLine"
driver_m = driver.find_elements(By.CLASS_NAME,class_name)

match_results =[]
match_results_list = []
for element in driver_m:
    match_results = element
    match_results_list.append(match_results.text.splitlines())


columns_name = ["status", "team 1", "team 2", "goals 1", "goals 2"]

result = pandas.DataFrame(match_results_list,columns = columns_name)

result = result.loc[result['status']=='Завершен']

result.to_excel("Results.xlsx", index=False)








