#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[ ]:


drive=webdriver.Chrome()


# In[ ]:


drive.get('https://www.Shine.com/')


# In[ ]:


designation1=drive.find_element(By.CLASS_NAME,'form-control  ')
designation1.send_keys('Data Analyst')


# In[ ]:


location1=drive.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input')
location1.send_keys('Bangalore')


# In[ ]:


search1=drive.find_element(By.CLASS_NAME,'searchForm_btnWrap_advance__VYBHN')
search1.click()


# In[ ]:


job_title=[]
job_location=[]
company_name=[]
experience_req=[]


# In[ ]:


title_comp=driver.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div[5]/div/div[1]/div[1]/div/div[1]/div[12]/div[1]/div[1]/h2/a')
for i in title_comp[0:10]:
    title=i.text
    job_title.append(title)


# In[ ]:


location_comp=driver.find_elements(By.XPATH,'//a[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_comp[0:10]:
    location=i.text
    job_location.append(location)


# In[ ]:


name_comp=driver.find_elements(By.XPATH,'//a[@class="jobCard_jobCard_cName__mYnow"]')
for i in name_comp[0:10]:
    company=i.text
    company_name.append(company)


# In[ ]:


experience_comp=driver.find_elements(By.XPATH,'//a[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_comp[0:10]:
    experience=i.text
    experience_req.append(experience)


# In[ ]:


df =pd.DataFrame({'Title':job_title,'Location':job_location,'Name':company_name,'Experience':experience_req})
df


# In[ ]:


please am unable to get the correct class for the data scraping


# In[ ]:




