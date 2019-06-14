#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests 


url = "https://boston.craigslist.org/search/npo"


job_no = 0
while True:
    
    #Connection establishment and store the info in variable data
    response = requests.get(url)
    data = response.text
    
    #to pass the data in BeautifulSoup to extract the html tags
    soup = BeautifulSoup(data,'html.parser')
    jobs = soup.find_all('p',{'class':'result-info'})
    
    #For loop to iterate over the list of jobs on the webpage
    for job in jobs:
        title = job.find('a',{'class':'result-title'}).text
        location_tag = job.find('span',{'class':'result-hood'})
        location = location_tag.text[2:-1] if location_tag else "N/A"
        date = job.find('time', {'class': 'result-date'}).text
        link = job.find('a', {'class': 'result-title'}).get('href')
        job_response = requests.get(link)
        job_data = job_response.text
        job_soup = BeautifulSoup(job_data, 'html.parser')
        job_description = job_soup.find('section',{'id':'postingbody'}).text
        job_attributes_tag = job_soup.find('p',{'class':'attrgroup'})
        job_attributes = job_attributes_tag.text if job_attributes_tag else "N/A"
        job_no+=1
        print('Job Title:', title, '\nLocation:', location, '\nDate:', date, '\nLink:', link,"\n", job_attributes, '\nJob Description:', job_description,'\n---')
    url_tag = soup.find('a',{'title':'next page'})
    if url_tag.get('href'):
        url= 'https://boston.craigslist.org' + url_tag.get('href')
        print(url)
    else:
        break
        
print("Total Jobs:", job_no)





# In[ ]:




