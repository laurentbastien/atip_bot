import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
from time import sleep
import requests
import re
from bs4 import BeautifulSoup
from time import sleep
path_to_chromedriver = '/path/to/cromedriver' 
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'https://open.canada.ca/en/search/ati'
browser.get(url)

#defence
#pageurl = "https://open.canada.ca/en/search/ati?ati%5B0%5D=ss_ati_organization_en%3ANational%20Defence&ajax_page_state%5Btheme%5D=od_bootstrap&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&page="
#CBSA
#pageurl = "https://open.canada.ca/en/search/ati?ajax_page_state%5Btheme%5D=od_bootstrap&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&ati%5B0%5D=ss_ati_organization_en%3ACanada%20Border%20Services%20Agency&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&page="
#CSIS
#pageurl = "https://open.canada.ca/en/search/ati?ajax_page_state%5Btheme%5D=od_bootstrap&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&ati%5B0%5D=ss_ati_organization_en%3ACanadian%20Security%20Intelligence%20Service&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&page="
#CSE
#pageurl = "https://open.canada.ca/en/search/ati?ajax_page_state%5Btheme%5D=od_bootstrap&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&ati%5B0%5D=ss_ati_organization_en%3ACommunications%20Security%20Establishment%20Canada&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&page="
#Global
#pageurl ="https://open.canada.ca/en/search/ati?ajax_page_state%5Btheme%5D=od_bootstrap&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&ati%5B0%5D=ss_ati_organization_en%3ACommunications%20Security%20Establishment%20Canada&ati%5B1%5D=ss_ati_organization_en%3AGlobal%20Affairs%20Canada&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&page="
#Indigenous affairs
#pageurl = "https://open.canada.ca/en/search/ati?ajax_page_state%5Btheme%5D=od_bootstrap&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&sort_by=year&ati%5B0%5D=ss_ati_organization_en%3ACrown-Indigenous%20Relations%20and%20Northern%20Affairs%20Canada&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&page="
#RCMP
#pageurl = "https://open.canada.ca/en/search/ati?ajax_page_state%5Btheme%5D=od_bootstrap&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&sort_by=year&ati%5B0%5D=ss_ati_organization_en%3ARoyal%20Canadian%20Mounted%20Police&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&page="
#correctional
#pageurl = "https://open.canada.ca/en/search/ati?ajax_page_state%5Btheme%5D=od_bootstrap&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&sort_by=year&ati%5B0%5D=ss_ati_organization_en%3ACorrectional%20Service%20of%20Canada&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&page="
#ENvironment and climate change
#pageurl = "https://open.canada.ca/en/search/ati?ajax_page_state%5Btheme%5D=od_bootstrap&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&sort_by=year&ati%5B0%5D=ss_ati_organization_en%3AEnvironment%20and%20Climate%20Change%20Canada&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&page="
#Department of Finance
#pageurl = "https://open.canada.ca/en/search/ati?ajax_page_state%5Btheme%5D=od_bootstrap&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&sort_by=year&ati%5B0%5D=ss_ati_organization_en%3ABusiness%20Development%20Bank%20of%20Canada&ati%5B1%5D=ss_ati_organization_en%3ACanada%20Foundation%20for%20Innovation&ati%5B2%5D=ss_ati_organization_en%3ADepartment%20of%20Finance%20Canada&page="
#Transport
#pageurl = "https://open.canada.ca/en/search/ati?ajax_page_state%5Btheme%5D=od_bootstrap&ajax_page_state%5Blibraries%5D=bootstrap/wet-boew&ajax_page_state%5Btheme_token%5D=&search_api_fulltext=&sort_by=year&ati%5B0%5D=ss_ati_organization_en%3ATransport%20Canada&page="

agencies = []
years = []
months = []
atiids = []
aticontents = []
pagenumber = []
counter = 0
agency_csv_file = "agency_name"

batchnumber = 1

currentdate = datetime.today().strftime('%Y-%m-%d')


try:
    for i in range(15):
        currentpagenumber = i 
        browser.get(pageurl+str(i))
        requets_per_page = len(browser.find_elements_by_partial_link_text("Req"))
        for i in range(requets_per_page):
            sleep(0.5)
            browser.find_elements_by_partial_link_text("Req")[i].click()
            try: 
                myurl = browser.current_url
                html = requests.get(myurl)
                page = html.text
                soup = BeautifulSoup(page, 'html.parser')
                pagen = soup.findAll("", {"class": "field-content"})
                #current page number
                pagenumber.append(currentpagenumber)
                #get ati number
                atinumber = str(pagen[3]).replace('<span class="field-content">',"")
                atinumber = atinumber.replace("</span>","")
                atiids.append(atinumber)
                #get ati description
                aticontent = str(pagen[4]).replace('<span class="field-content">',"")
                aticontent = aticontent.replace("</span>","")
                aticontents.append(aticontent)
                #agency
                agency = str(pagen[0]).replace('<span class="field-content">',"")
                agency = agency.replace("</span>","")
                agencies.append(agency)
                #year
                year = str(pagen[1]).replace('<span class="field-content">',"")
                year = year.replace("</span>","")
                years.append(year)
                #month
                month = str(pagen[2]).replace('<span class="field-content">',"")
                month = month.replace("</span>","")
                months.append(month)
                #get page number
                pagen = str(pagen[6]).replace('<span class="field-content">',"")
                pagen = pagen.replace("</span>","")
                pagen = int(pagen)            
                sleep(0.5)
                counter = counter+1
                print(counter)
                if pagen > 0:
                    select = Select(browser.find_element_by_xpath("//*[@id='edit-requestor-category']"))
                    select.select_by_visible_text('Media')
                    select = Select(browser.find_element_by_xpath("//*[@id='edit-delivery-method']"))
                    select.select_by_visible_text('Electronic Copy') 
                    inputElement = browser.find_element_by_xpath("//*[@id='edit-given-name']")
                    inputElement.send_keys('Your name')
                    inputElement = browser.find_element_by_xpath("//*[@id='edit-family-name']")
                    inputElement.send_keys('Last name')
                    inputElement = browser.find_element_by_xpath("//*[@id='edit-your-e-mail-address']")
                    inputElement.send_keys('Your email')
                    inputElement = browser.find_element_by_xpath("//*[@id='edit-your-telephone-number']")
                    inputElement.send_keys('Phone number')
                    inputElement = browser.find_element_by_xpath("//*[@id='edit-address-fieldset-address']")
                    inputElement.send_keys('Your address')               
                    inputElement = browser.find_element_by_xpath("//*[@id='edit-address-fieldset-city']")
                    inputElement.send_keys('Your city')
                    select = Select(browser.find_element_by_xpath("//*[@id='edit-address-fieldset-state-province-select']"))
                    select.select_by_visible_text('Your province') 
                    inputElement = browser.find_element_by_xpath("//*[@id='edit-address-fieldset-postal-code']")
                    inputElement.send_keys('Your postal code')
                    select = Select(browser.find_element_by_xpath("//*[@id='edit-address-fieldset-country']"))
                    select.select_by_visible_text('Canada') 
                    select = Select(browser.find_element_by_xpath("//*[@id='edit-consent']"))
                    select.select_by_visible_text('Yes') 
                    browser.find_element_by_xpath("//*[@id='edit-actions-submit']").click()        
                    browser.execute_script("window.history.go(-2)")
                else:
                    browser.execute_script("window.history.go(-1)")

            except IndexError:
                browser.execute_script("window.history.go(-1)")

    else:
        df = pd.DataFrame()
        df = pd.DataFrame(agencies)
        df["year"] = pd.DataFrame(years)
        df["month"] = pd.DataFrame(months)
        df["id"] = pd.DataFrame(atiids)
        df["content"] = pd.DataFrame(aticontents)
        df["page"] = pd.DataFrame(pagenumber)
        df.columns = ["agency","year","month","id","content","page"]
        csvfilename = "-batch-{}-{}.csv".format(batchnumber,agency_csv_file)
        df.to_csv(currentdate+csvfilename)

except Exception as error:
    print(error)






