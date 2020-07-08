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
    from selenium import webdriver
    urlm='https://www.monsterindia.com/srp/results?query='+str(field)+'&locations='+str(Location)+'&experienceRanges='+str(Experience)+'~'+str(Experience)+'&experience='+str(Experience)+'&searchId=81e909fa-3756-40af-be64-538c1eade7e1'
    driver.get(urlm)
    det=[]
    for i in range(1,4):
        try:
            a=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/div[2]/div[2]/div/div[1]/div[1]/div[3]/div/div['+str(i)+']/div/div[1]/div/div/h3/a')
            title=a.text
            company=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/div[2]/div[2]/div/div[1]/div[1]/div[3]/div/div['+str(i)+']/div/div[1]/div/div/span/a').text
            link=a.get_property('href')

            tempj={'job_title':title,
                   'company':company,
                   'link for more details':link}
            det.append(tempj)
        except:
            pass
    data1=pd.DataFrame(det)
    ##
    urli='https://www.indeed.co.in/jobs?q='+str(field)+'&l='+str(Location)
    driver.get(urli)
    for i in range(7,12,2):
        try:
            a=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[1]/div['+str(i)+']/h2/a')
            title=a.text
        except:
            pass
        try:
            company=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[1]/div['+str(i)+']/div[1]/div[1]/span').text
        except:
            try:
                company=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[1]/div['+str(i)+']/div[1]/div[1]/span[1]').text
            except:
                company='Nan'
        link=a.get_property('href')
        tempj={'job_title':title,
              'company':company,
              'link for more details':link}
        detin.append(tempj)
    datain=pd.DataFrame(detin)
    tdata=pd.concat([data1,datain])
    return tdata.to_html(header=True)
