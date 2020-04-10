import pandas as pd 
import time 
import datetime as dt # manupulating date

## Selenium 
from selenium import webdriver   # importing selenium webdrivers
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys  # importing webdriver keys
 
class Test:
    
    def __init__(self):
        self.url = 'https://forms.gle/tNV8Ra2TN7aLfgri8'
        self.df = pd.read_html('PythonTest/index.html',header=0)[0]
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
             
    def PreProcessing(self):
        df = self.df[~self.df.Name.str.contains("an")]
        #df.to_excel('Data_Details.xls')
        df['Phone'] = df['Phone'].str.replace(r'\(|\)| ','')
        df.reset_index(inplace=True)
        df.drop('index',axis=1,inplace=True)
        df['Date']=pd.to_datetime(df["Date"]).dt.strftime("%d%m%Y")
        return df
    
    def FormAuthomation(self):
        data = self.PreProcessing()
        Path =['//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input',
               '//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input',
               '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input',
               '//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/div[2]/div[1]/div/div[1]/input']
        Columns = ['Name','Phone','Email','Date']
        for j in range(0,len(data)):
            self.browser.get(self.url)
            for i in range(0,len(Path)):
                Attributes = self.browser.find_element_by_xpath(Path[i])
                Attributes.send_keys(data[Columns[i]][j])
                time.sleep(2)
            Submit = self.browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span/span')
            Submit.click()
            print('Submitted', j)
