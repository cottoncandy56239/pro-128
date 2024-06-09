from selenium import webdriver 
from selenium.webdriver.common.by import By  
from bs4 import BeautifulSoup  
import time 
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  
import request module

browser = webdriver.Chrome()

new_planets_data = []

def scrape_more_data(hyperlink):
    page = request.get(hyperlink)
    soup = BeautifulSoup(page.content, "html.parser")
    temp_list = []
    information_to_extract = ["Star Name:", "Radius:", "Mass:", "Distance Data:"]
    for info_name in information_to_extract:
        try:
            value = soup.find("div", text = info_name).find_next("span").text.strip()
            temp_list.append(value)
        except:
            temp_list.append("Unknown")

    new_planets_data.append(temp_list)
df_1 = pd.read_csv("data_scraping_1.csv")

for index, row in df_1.iterrows():
    print(row["hyperlink"])
    scrape_more_data(row["hyperlink"])
    print("Data Scraping Hyperlink{index+1} Completed")

header = ["star name: ", "radius: ", "mass: ", "distance_data: "]
new_df_1 = pd.DataFrame(new_planets_data, columns = headers)
new_df_1.to_csv('data_scraping_2.csv', index = True, index_label = "id")