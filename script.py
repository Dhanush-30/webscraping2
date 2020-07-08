#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def scrap(field,Location,Experience):
    import time
    import selenium
    import os
    from selenium import webdriver
    import pandas as pd
 
    chrome_options = webdriver.ChromeOptions()
    
    chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('headless')
    
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
    
  
    # monster
    

    urlm='https://www.monsterindia.com/srp/results?query='+field+'&locations='+Location+'&experienceRanges='+str(Experience)+'~'+str(Experience)+'&experience='+str(Experience)+'&searchId=81e909fa-3756-40af-be64-538c1eade7e1'


    driver.get(urlm)

    listoflinksm=[]
    k=driver.find_elements_by_tag_name('h3')
    for i in k:
        try:
            m=i.find_element_by_tag_name('a')
            ma=m.get_property('href')        
            listoflinksm.append(ma)
            length=len(listoflinksm)
            if length==2:
                break
            else:
                continue
        except:
            pass
        

    det=[]
    for link in listoflinksm:
        driver.get(link)
        
        try:
            title=driver.find_element_by_xpath('//*[@id="jobDetailHolder"]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div/div/h1').text
            company=driver.find_element_by_xpath('//*[@id="jobDetailHolder"]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div/div/span/a').text
            tempj={'job_title':title,
               'company':company,
               'link for more details':link}
            det.append(tempj)
        except:
            pass
        

    data1=pd.DataFrame(det)
    
   

    # # shine

    # In[64]:
   

    urls='https://www.shine.com/job-search/'+field+'-jobs-in-'+Location
    driver.get(urls)
    try:
        driver.find_element_by_xpath('//*[@id="push_noti_popup"]/div[1]/span').click()
    except:
        pass
    driver.get(urls)
    time.sleep(3)
    driver.find_element_by_xpath('html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]').click()
    #/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/div/ul
    fieldar=driver.find_element_by_xpath('//*[@id="id_q"]')
    fieldar.send_keys(field)
    fieldar.submit()

    k=driver.find_elements_by_tag_name('h3')
    shlinks=[]
    for i in range(1,20):
        try:
            k=driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[1]/div/div[1]/div/div/div[1]/ul/li['+str(i)+']/div[2]/ul[1]/li/h3')
            link=k.find_element_by_tag_name('a').get_property('href')
            shlinks.append(link)
            length=len(shlinks)
            if length==2:
                break
            else:
                continue
        except:
            pass


    shdet=[]
    for link in shlinks:
        driver.get(link)
        comp=driver.find_element_by_xpath('//*[@id="id_search_head"]/div/div[1]/a/span/span/h2').text
        title=driver.find_element_by_xpath('//*[@id="id_search_head"]/div/div[1]/strong/span[1]/h1').text
        tempj={'job_title':title,
              'company':comp,
              'link for more details':link}
        shdet.append(tempj)

    datash=pd.DataFrame(shdet)


    # In[14]:


    urlin='https://www.linkedin.com/jobs/search?keywords='+field+'&location='+Location+'&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0'


    driver.get(urlin)
    linkin=[]
    driver.get(urlin)

    for i in range(2,8):
        try:
            k=driver.find_element_by_xpath('//*[@id="main-content"]/div/section/ul/li['+str(i)+']/a').get_property('href')
            linkin.append(k)
       

            
            if len(linkin)==2:
                break
            else:
                continue
        except:
            pass

    detlin=[]
    for link in linkin:
        driver.get(link)
        title=driver.find_element_by_xpath('/html/body/main/section[1]/section[2]/div[1]/div[1]/h1').text
        try:
            company=driver.find_element_by_xpath('/html/body/main/section[1]/section[2]/div[1]/div[1]/h3[1]/span[1]/a').text
        except:
            company=driver.find_element_by_xpath('/html/body/main/section[1]/section[2]/div[1]/div[1]/h3[1]/span[1]').text

        tempj={'job_title':title,
                  'company':company,
                  'link for more details':link}
        detlin.append(tempj)


    datalin=pd.DataFrame(detlin)


    # # total data

    # In[90]:
   

    tdata=pd.concat([data1,datash,datalin])
    return tdata.to_html(header=True)

