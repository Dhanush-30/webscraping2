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
    
    urli='https://www.indeed.co.in/jobs?q='+field+'&l='+Location

    driver.get(urli)

    ik=driver.find_elements_by_tag_name('h2')
    inlinks=[]
    for i in range(len(ik)):
        link=ik[i].find_element_by_tag_name('a').get_property('href')
        inlinks.append(link)
        length=len(inlinks)
        if length==3:
            break
        else:
            continue

    detin=[]
    for link in inlinks:
        driver.get(link)
        title=driver.find_element_by_tag_name('h3')
        titlet=title.text
        try:
            company=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div').text
        except:
            try:
                company=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div[4]/a/div/div/h4').text
            except:
                company='not available right now or visit the link for updates'
        
        tempj={'job_title':titlet,
              'company':company,
              'link for more details':link}
        detin.append(tempj)

    datain=pd.DataFrame(detin)
    tdata=pd.concat([data1,datain])
    return tdata.to_html(header=True)
