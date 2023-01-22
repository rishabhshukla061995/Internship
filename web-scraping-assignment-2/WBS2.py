#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install selenium')


# In[5]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import time

import warnings
warnings.filterwarnings("ignore")


# In[6]:


#Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data.


# In[7]:


driver=webdriver.Chrome(r"C:\Users\Public\Desktop/chromedriver\ 4\\chromedriver.exe")


# In[8]:


driver.get("http://www.naukri.com/")


# In[9]:


# Entering Designation and location as required in the question

designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Analyst')


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Banglore')


# In[10]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[10]:


# Create empty list first inorder to get the information from the naukri site

job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[11]:


# Scrapping Job titles from the given page

title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
# Scrapping Job Location

location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)

# Scarpping Company Name from the given page

Company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in Company_tags[0:10]:
    Company=i.text
    company_name.append(Company)

# Scrapping Job Experience from the page

experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    experience=i.text
    experience_required.append(experience)


# In[12]:


# Need to check the length before we create the data frame
print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[13]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,'Experience':experience_required})
df


# In[14]:


# Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.


# In[18]:


driver=webdriver.Chrome(r"C:\Users\Public\Desktop/chromedriver\ 4\\chromedriver.exe")


# In[19]:


driver.get("http://www.naukri.com/")


# In[20]:


# Entering Designation and location as required in the question

designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Banglore')


# In[21]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[22]:


# Create empty list first inorder to get the information from the naukri site

job_title=[]
job_location=[]
company_name=[]


# In[23]:


# Scrapping Job titles from the given page

title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
# Scrapping Job Location

location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)

# Scarpping Company Name from the given page

Company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in Company_tags[0:10]:
    Company=i.text
    company_name.append(Company)


# In[24]:


# Need to check the length before we create the data frame
print(len(job_title),len(job_location),len(company_name))


# In[25]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name})
df


# In[26]:


# In this question you have to scrape data using the filters available on the webpage as shown below: You have to use the location and salary filter. You have to scrape data for “Data Scientist” designation for first 10 job results. You have to scrape the job-title, job-location, company name, experience required. The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs


# In[35]:


driver=webdriver.Chrome(r"C:\Users\Public\Desktop/chromedriver\ 4\\chromedriver.exe")


# In[36]:


driver.get("http://www.naukri.com/")


# In[37]:


# Entering Designation and location as required in the question

designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


# In[38]:


# Submit Button
search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[39]:


# Filter Location "Delhi/NCR"
Location=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[2]/label/p/span[1]")
Location.click()


# In[40]:


# Filter Salary "3-6 lakhs"
Salary=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[6]/div[2]/div[2]/label/p/span[1]")
Salary.click()


# In[41]:


# Create empty list first inorder to get the information from the naukri site

job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[42]:


# Scrapping Job titles from the given page

title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
# Scrapping Job Location

location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)

# Scarpping Company Name from the given page

Company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in Company_tags[0:10]:
    Company=i.text
    company_name.append(Company)

# Scrapping Job Experience from the page

experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    experience=i.text
    experience_required.append(experience)


# In[45]:


# Need to check the length before we create the data frame
print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[47]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,'Experience':experience_required})
df


# In[6]:


# Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:


# In[11]:


driver.get("https://www.flipkart.com/")


# In[12]:


# Searching for the product
Product=driver.find_element(By.CLASS_NAME,"_3704LK")
Product.send_keys('sunglasses')


# In[14]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
search.click()


# In[15]:


# Getting the Brand details

Brand=driver.find_elements(By.XPATH,"//div[@class='_2WkVRV']")
Brand[0:2]


# In[16]:


len(Brand)


# In[17]:


Price=driver.find_elements(By.XPATH,"//div[@class='_30jeq3']")
Price[0:2]


# In[18]:


len(Price)


# In[19]:


pdetails=driver.find_elements(By.XPATH,"//a[@class='IRpwTa']")
pdetails[0:2]


# In[20]:


len(pdetails)


# In[21]:


# Extracting Page 3 Deatils for Product
page3_Brand=[]
for i in Brand:
    Brand=i.text
    page3_Brand.append(Brand)
page3_Brand[0:2]


# In[22]:


# Extracting Page 3 details for Price
page3_Price=[]
for i in Price:
    Price=i.text
    page3_Price.append(Price)
page3_Price[0:2]


# In[23]:


# Extracting Page 3 details for Product Details
page3_pdetails=[]
for i in pdetails:
    pdetails=i.text
    page3_pdetails.append(pdetails)
page3_pdetails[0:2]


# In[28]:


# Making a Data Frame for page 3
page3 = pd.DataFrame({})
page3["page_Brand"]=page3_Brand[:24]
page3["page_Price"]=page3_Price[:24]
page3["page_pdetails"]=page3_pdetails[:24]
page3.head()


# In[67]:


# Final 100 Glasses DataFrame

flipkart_100_sunglasses = pd.concat([page1,page2,page3])
flipkart_100_sunglasses


# In[32]:


# Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone.


# In[33]:


driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb-includes-earpods-power-adapter/product-reviews/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKCTSVZAXUHGREPBFGI&marketplace=FLIPKART")


# In[34]:


all_button=driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]")
all_button.click()


# In[35]:


# Code for Rating

Rating=driver.find_elements(By.XPATH,"//div[@class='_3LWZlK _1BLPMq']")
Rating[0:2]


# In[36]:


page1_Rating=[]
for i in Rating:
    Rating = i.text
    page1_Rating.append(Rating)
page1_Rating


# In[37]:


# Getting the Review Summary

Review_summary =driver.find_elements(By.XPATH,"//p[@class='_2-N8zT']")
Review_summary[0:2]


# In[38]:


page1_Review_summary=[]
for i in Review_summary:
    Review_summarys = i.text
    page1_Review_summary.append(Review_summarys)
page1_Review_summary


# In[39]:


# Getting the Full Review

full_review=driver.find_elements(By.XPATH,"//div[@class='t-ZTKy']")
full_review[0:2]


# In[40]:


page1_full_review=[]
for i in full_review:
    full_reviews = i.text.replace("\n",".")
    page1_full_review.append(full_reviews)
page1_full_review


# In[41]:


# Creating Data Frame for PAGE 1

page1 = pd.DataFrame({})
page1["Rating"]=page1_Rating
page1["Review_summary"]=page1_Review_summary
page1["full_review"]=page1_full_review
page1


# In[42]:


# Going to the Page 2

next_button=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]/span")
next_button.click()


# In[43]:


# Rating frrom Page 2 

Rating=driver.find_elements(By.XPATH,"//div[@class='_3LWZlK _1BLPMq']")
Rating[0:2]


# In[44]:


page2_Rating=[]
for i in Rating:
    Rating = i.text
    page2_Rating.append(Rating)
page2_Rating


# In[45]:


# Getting the Review Summary from page 2

Review_summary =driver.find_elements(By.XPATH,"//p[@class='_2-N8zT']")
Review_summary[0:2]


# In[46]:


page2_Review_summary=[]
for i in Review_summary:
    Review_summarys = i.text
    page2_Review_summary.append(Review_summarys)
page2_Review_summary


# In[47]:


# Getting the Full Review from Page 2

full_review=driver.find_elements(By.XPATH,"//div[@class='t-ZTKy']")
full_review[0:2]


# In[48]:


page2_full_review=[]
for i in full_review:
    full_reviews = i.text.replace("\n",".")
    page2_full_review.append(full_reviews)
page2_full_review


# In[49]:


# Creating Data Frame for Page 2

page2 = pd.DataFrame({})
page2["Rating"]=page2_Rating
page2["Review_summary"]=page2_Review_summary
page2["full_review"]=page2_full_review
page2


# In[51]:


# Clicking on Page 3


next_button=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]/span")
next_button.click()


# In[52]:


# Rating frrom Page 3

Rating=driver.find_elements(By.XPATH,"//div[@class='_3LWZlK _1BLPMq']")
Rating[0:2]


# In[53]:


page3_Rating=[]
for i in Rating:
    Rating=i.text
    page3_Rating.append(Rating)
page3_Rating


# In[54]:


# Getting the Review Summary from page 3

Review_summary =driver.find_elements(By.XPATH,"//p[@class='_2-N8zT']")
Review_summary[0:2]


# In[55]:


page3_Review_summary=[]
for i in Review_summary:
    Review_summarys = i.text
    page3_Review_summary.append(Review_summarys)
page3_Review_summary


# In[56]:


# Getting the Full Review from Page 3

full_review=driver.find_elements(By.XPATH,"//div[@class='t-ZTKy']")
full_review[0:2]


# In[57]:


page3_full_review=[]
for i in full_review:
    full_reviews = i.text.replace("\n",".")
    page3_full_review.append(full_reviews)
page3_full_review


# In[58]:


# Creating Data Frame for Page 3

page3 = pd.DataFrame({})
page3["Rating"]=page3_Rating
page3["Review_summary"]=page3_Review_summary
page3["full_review"]=page3_full_review
page3


# In[59]:


# Clicking on Page 4


next_button=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]/span")
next_button.click()


# In[60]:


# Rating frrom Page 4

Rating=driver.find_elements(By.XPATH,"//div[@class='_3LWZlK _1BLPMq']")
Rating[0:2]


# In[61]:


page4_Rating=[]
for i in Rating:
    Rating=i.text
    page4_Rating.append(Rating)
page4_Rating


# In[62]:


# Getting the Review Summary from page 4

Review_summary =driver.find_elements(By.XPATH,"//p[@class='_2-N8zT']")
Review_summary[0:2]


# In[63]:


page4_Review_summary=[]
for i in Review_summary:
    Review_summarys = i.text
    page4_Review_summary.append(Review_summarys)
page4_Review_summary


# In[64]:


# Getting the Full Review from Page 4

full_review=driver.find_elements(By.XPATH,"//div[@class='t-ZTKy']")
full_review[0:2]


# In[65]:


page4_full_review=[]
for i in full_review:
    full_reviews = i.text.replace("\n",".")
    page4_full_review.append(full_reviews)
page4_full_review


# In[66]:


# Creating Data Frame for Page 4

page4 = pd.DataFrame({})
page4["Rating"]=page4_Rating
page4["Review_summary"]=page4_Review_summary
page4["full_review"]=page4_full_review
page4


# In[68]:


# Clicking on Page 5


next_button=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]/span")
next_button.click()


# In[69]:


# Rating frrom Page 5

Rating=driver.find_elements(By.XPATH,"//div[@class='_3LWZlK _1BLPMq']")
Rating[0:2]


# In[70]:


page5_Rating=[]
for i in Rating:
    Rating=i.text
    page5_Rating.append(Rating)
page5_Rating


# In[71]:


# Getting the Review Summary from page 5

Review_summary =driver.find_elements(By.XPATH,"//p[@class='_2-N8zT']")
Review_summary[0:2]


# In[72]:


page5_Review_summary=[]
for i in Review_summary:
    Review_summarys = i.text
    page5_Review_summary.append(Review_summarys)
page5_Review_summary


# In[73]:


# Getting the Full Review from Page 5

full_review=driver.find_elements(By.XPATH,"//div[@class='t-ZTKy']")
full_review[0:2]


# In[74]:


page5_full_review=[]
for i in full_review:
    full_reviews = i.text.replace("\n",".")
    page5_full_review.append(full_reviews)
page5_full_review


# In[75]:


# Creating Data Frame for Page 5

page5 = pd.DataFrame({})
page5["Rating"]=page5_Rating
page5["Review_summary"]=page5_Review_summary
page5["full_review"]=page5_full_review
page5


# In[76]:


# Clicking on Page 6


next_button=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]/span")
next_button.click()


# In[77]:


# Rating frrom Page 6

Rating=driver.find_elements(By.XPATH,"//div[@class='_3LWZlK _1BLPMq']")
Rating[0:2]


# In[78]:


page6_Rating=[]
for i in Rating:
    Rating=i.text
    page6_Rating.append(Rating)
    
page6_Rating


# In[79]:


page6_Rating.insert(9,'1')
page6_Rating


# In[80]:


# Getting the Review Summary from page 6

Review_summary =driver.find_elements(By.XPATH,"//p[@class='_2-N8zT']")
Review_summary[0:2]


# In[81]:


page6_Review_summary=[]
for i in Review_summary:
    Review_summarys = i.text
    page6_Review_summary.append(Review_summarys)
page6_Review_summary


# In[82]:


# Getting the Full Review from Page 6

full_review=driver.find_elements(By.XPATH,"//div[@class='t-ZTKy']")
full_review[0:2]


# In[84]:


page6_full_review=[]
for i in full_review:
    full_reviews = i.text.replace("\n",".")
    page6_full_review.append(full_reviews)
page6_full_review


# In[85]:


print(len(page6_Rating),len(page6_Review_summary),len(page6_full_review))


# In[86]:


# Creating Data Frame for Page 6

page6 = pd.DataFrame({})
page6["Rating"]=page6_Rating
page6["Review_summary"]=page6_Review_summary
page6["full_review"]=page6_full_review
page6


# In[87]:


# Clicking on Page 7


next_button=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]/span")
next_button.click()


# In[88]:


# Rating from Page 7

Rating=driver.find_elements(By.XPATH,"//div[@class='_3LWZlK _1BLPMq']")
Rating[0:2]


# In[89]:


# Rating from Page 7

Rating=driver.find_elements(By.XPATH,"//div[@class='_3LWZlK _1BLPMq']")
Rating[0:2]


# In[93]:


page7_Rating=[]
for i in Rating:
    Rating=i.text
    page7_Rating.append(Rating)
    
page7_Rating


# In[91]:


page7_Rating.insert(1,'1')
page7_Rating


# In[92]:


# Getting the Review Summary from page 7

Review_summary =driver.find_elements(By.XPATH,"//p[@class='_2-N8zT']")
Review_summary[0:2]


# In[94]:


page7_Review_summary=[]
for i in Review_summary:
    Review_summarys = i.text
    page7_Review_summary.append(Review_summarys)
page7_Review_summary


# In[95]:


# Getting the Full Review from Page 7

full_review=driver.find_elements(By.XPATH,"//div[@class='t-ZTKy']")
full_review[0:2]


# In[96]:


page7_full_review=[]
for i in full_review:
    full_reviews = i.text.replace("\n",".")
    page7_full_review.append(full_reviews)
page7_full_review


# In[97]:


print(len(page7_Rating),len(page7_Review_summary),len(page7_full_review))


# In[98]:


# Creating Data Frame for Page 7

page7 = pd.DataFrame({})
page7["Rating"]=page7_Rating
page7["Review_summary"]=page7_Review_summary
page7["full_review"]=page7_full_review
page7


# In[99]:


# Clicking on Page 8


next_button=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]/span")
next_button.click()


# In[100]:


# Rating frrom Page 8

Rating=driver.find_elements(By.XPATH,"//div[@class='_3LWZlK _1BLPMq']")
Rating[0:2]


# In[101]:


page8_Rating=[]
for i in Rating:
    Rating=i.text
    page8_Rating.append(Rating)
    
page8_Rating


# In[102]:


# Getting the Review Summary from page 8

Review_summary =driver.find_elements(By.XPATH,"//p[@class='_2-N8zT']")
Review_summary[0:2]


# In[103]:


page8_Review_summary=[]
for i in Review_summary:
    Review_summarys = i.text
    page8_Review_summary.append(Review_summarys)
page8_Review_summary


# In[104]:


# Getting the Full Review from Page 8

full_review=driver.find_elements(By.XPATH,"//div[@class='t-ZTKy']")
full_review[0:2]


# In[105]:


page8_full_review=[]
for i in full_review:
    full_reviews = i.text.replace("\n",".")
    page8_full_review.append(full_reviews)
page8_full_review


# In[106]:


print(len(page8_Rating),len(page8_Review_summary),len(page8_full_review))


# In[107]:


# Creating Data Frame for Page 8

page8 = pd.DataFrame({})
page8["Rating"]=page8_Rating
page8["Review_summary"]=page8_Review_summary
page8["full_review"]=page8_full_review
page8


# In[108]:


# Clicking on Page 9


next_button=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]/span")
next_button.click()


# In[109]:


# Rating frrom Page 9

Rating=driver.find_elements(By.XPATH,"//div[@class='_3LWZlK _1BLPMq']")
Rating[0:2]


# In[110]:


page9_Rating=[]
for i in Rating:
    Rating=i.text
    page9_Rating.append(Rating)
    
page9_Rating


# In[111]:


# Getting the Review Summary from page 9

Review_summary =driver.find_elements(By.XPATH,"//p[@class='_2-N8zT']")
Review_summary[0:2]


# In[112]:


page9_Review_summary=[]
for i in Review_summary:
    Review_summarys = i.text
    page9_Review_summary.append(Review_summarys)
page9_Review_summary


# In[113]:


# Getting the Full Review from Page 9

full_review=driver.find_elements(By.XPATH,"//div[@class='t-ZTKy']")
full_review[0:2]


# In[114]:


page9_full_review=[]
for i in full_review:
    full_reviews = i.text.replace("\n",".")
    page9_full_review.append(full_reviews)
page9_full_review


# In[115]:


print(len(page9_Rating),len(page9_Review_summary),len(page9_full_review))


# In[116]:


# Creating Data Frame for Page 9

page9 = pd.DataFrame({})
page9["Rating"]=page9_Rating
page9["Review_summary"]=page9_Review_summary
page9["full_review"]=page9_full_review
page9


# In[117]:


# Clicking on Page 10


next_button=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]/span")
next_button.click()


# In[118]:


# Rating frrom Page 10

Rating=driver.find_elements(By.XPATH,"//div[@class='_3LWZlK _1BLPMq']")
Rating[0:2]


# In[119]:


page10_Rating=[]
for i in Rating:
    Rating=i.text
    page10_Rating.append(Rating)
    
page10_Rating


# In[120]:


page10_Rating.insert(9,'1')
page10_Rating


# In[121]:


# Getting the Review Summary from page 10

Review_summary =driver.find_elements(By.XPATH,"//p[@class='_2-N8zT']")
Review_summary[0:2]


# In[122]:


page10_Review_summary=[]
for i in Review_summary:
    Review_summarys = i.text
    page10_Review_summary.append(Review_summarys)
page10_Review_summary


# In[123]:


# Getting the Full Review from Page 10

full_review=driver.find_elements(By.XPATH,"//div[@class='t-ZTKy']")
full_review[0:2]


# In[124]:


page10_full_review=[]
for i in full_review:
    full_reviews = i.text.replace("\n",".")
    page10_full_review.append(full_reviews)
page10_full_review


# In[125]:


print(len(page10_Rating),len(page10_Review_summary),len(page10_full_review))


# In[126]:


# Creating Data Frame for Page 10

page10 = pd.DataFrame({})
page10["Rating"]=page10_Rating
page10["Review_summary"]=page10_Review_summary
page10["full_review"]=page10_full_review
page10

