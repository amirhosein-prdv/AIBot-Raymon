
#pip install unidecode
#pip install SpeechRecognition


# ...This Program is about Raymon_Robo who answer your request about Weather & Religious Time & Times& ..........

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from Some_File import *


#from Some_File import *
#from hazm import *
import nltk

#from __future__ import unicode_literals

#from hazm import Normalizer
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('punkt') # tokenizer
nltk.download('stopwords') # remove stop-words
nltk.download('averaged_perceptron_tagger') # pos tagger
nltk.download('maxent_ne_chunker') # chunker
nltk.download('words') # ner
nltk.download('treebank') # dependency parser
nltk.download('wordnet') # lematizer

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import treebank
import urllib.parse
import requests
import pandas as pd
import datetime
#import dateparser
#from dateparser.calendars.jalali import JalaliCalendar
#from dateparser.calendars.hijri import HijriCalendar
#from dateparser.search import search_dates
#from hijri_converter import convert
#from googletrans import Translator
from bs4 import BeautifulSoup
from urllib.request import urlopen
from unidecode import unidecode
import os
import speech_recognition as sr
import re

import textdistance
import math
import statistics 

import requests

#pip install -U hijri-converter

from hijri_converter import convert
import jdatetime

import csv


PM = '{"1":"13","2":"14","3":"15","4":"16","5":"17","6":"18","7":"19","8":"20","9":"21","10":"22","11":"23","12":"24"}'
ww_Time1 = {"يک":"01","دو":"02","سه":"03","چهار":"04","پنج":"05","شش":"06","هفت":"07","هشت":"08","نه":"09","ده":"10","يازده":"11","دوازده":"12","سيزده":"13","چهارده":"14","پانزده":"15","شانزده":"16","هفده":"17","هجده":"18","نوزده":"19","بيست":"20","بيست ويک":"21","بيست ودو":"22","بيست و سه":"23","بيست وچهار":"24"}
ww_Time2 = {"1":"01","2":"02","3":"03","4":"04","5":"05","6":"06","7":"07","8":"08","9":"09"}
ww_Time = {"يک":"13","دو":"14","سه":"15","چهار":"16","پنج":"17","شش":"18","هفت":"19","هشت":"20","نه":"21","ده":"22","يازده":"23","دوازده":"24"}

Time_a = ['بيست وچهار','بيست وسه','بيست ودو','بيست ويک','بيست','نوزده','هجده','هفده','شانزده','پانزده','چهارده','سيزده','دوازده','يازده','ده','نه','هشت','هفت','شش','پنج','چهار','سه','دو','يک']	  
Time_b = ['سي ويک','سي','بيست ونه','بيست و هشت','بيست و هفت','بيست وشش','بيست و پنج','بيست وچهار','بيست وسه','بيست ودو','بيست ويک','بيست','نوزده','هجده','هفده','شانزده','پانزده','چهارده','سيزده','دوازده','يازده','ده','نه','هشت','هفت','شش','پنج','چهار','سه','دو','يک']
                
number1 = ['0','1','2','3','4','5','6','7','8','9']
number2 = {'0':'00','1':'01','2':'02','3':'03','4':'04','5':'05','6':'06','7':'07','8':'08','9':'09'}
number3 = ['0','1','2','3','4','5','6','7','8','9','10','12','13','14','15','16','17','18','19','20','21','22','23','24']



#***********************************************
with open('MY_City.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file, delimiter=',')
     city_Fa =[]
     for row in reader:
        city_Fa = city_Fa + [row]

with open('My_country.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file, delimiter=',')
     country =[]
     for row in reader:
        country = country + [row]        

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import re
PM = '{"1":"13","2":"14","3":"15","4":"16","5":"17","6":"18","7":"19","8":"20","9":"21","10":"22","11":"23","12":"24"}'
ww_Time1 = {"يک":"01","دو":"02","سه":"03","چهار":"04","پنج":"05","شش":"06","هفت":"07","هشت":"08","نه":"09","ده":"10","يازده":"11","دوازده":"12","سيزده":"13","چهارده":"14","پانزده":"15","شانزده":"16","هفده":"17","هجده":"18","نوزده":"19","بيست":"20","بيست ويک":"21","بيست ودو":"22","بيست و سه":"23","بيست وچهار":"24"}
ww_Time2 = {"1":"01","2":"02","3":"03","4":"04","5":"05","6":"06","7":"07","8":"08","9":"09"}
ww_Time = {"يک":"13","دو":"14","سه":"15","چهار":"16","پنج":"17","شش":"18","هفت":"19","هشت":"20","نه":"21","ده":"22","يازده":"23","دوازده":"24"}

Time_a = ['بيست وچهار','بيست وسه','بيست ودو','بيست ويک','بيست','نوزده','هجده','هفده','شانزده','پانزده','چهارده','سيزده','دوازده','يازده','ده','نه','هشت','هفت','شش','پنج','چهار','سه','دو','يک']	  
Time_b = ['سي ويک','سي','بيست ونه','بيست و هشت','بيست و هفت','بيست وشش','بيست و پنج','بيست وچهار','بيست وسه','بيست ودو','بيست ويک','بيست','نوزده','هجده','هفده','شانزده','پانزده','چهارده','سيزده','دوازده','يازده','ده','نه','هشت','هفت','شش','پنج','چهار','سه','دو','يک']
                
number1 = ['0','1','2','3','4','5','6','7','8','9']
number2 = {'0':'12','1':'01','2':'02','3':'03','4':'04','5':'05','6':'06','7':'07','8':'08','9':'09'}
number3 = ['0','1','2','3','4','5','6','7','8','9','10','12','13','14','15','16','17','18','19','20','21','22','23','24']

import csv


#***********************************************
with open('MY_City.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file, delimiter=',')
     country_Fa =[]
     for row in reader:
        country_Fa = country_Fa + [row]



#>>>>>>>> Train <<<<<<<< بايد اينجا کار کنم هنوز#EEEEEEEEEEEEEEEEEE
import pandas as pd

from finglish import f2p

import json
import csv
import numpy as np
#B = []
#with open('world-cities_json.json','r') as fobj:
 #   data = json.load(fobj)
#range(len(data))


    #for i in range(len(data)):
     #   A = data[i]["name"]
        
      #  K = f2p(A)
       # B = B +[K]
#print(B[10:200])
#>>>>>>>>>>>>>fft   بايد اينجا کار کنم هنوز

import numpy as np

from scipy.fft import fft, ifft

x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

y = fft(x)

yinv = ifft(y)                               #EEEEEEEEEEEEEEEEEEEEEEEE
    






#***************************************
with open('My_Event_1395.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Event_1395 =[]
     for row in reader:
        Event_1395 = Event_1395 + row

with open('My_Date_1395.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Date_1395 =[]
     for row in reader:
        Date_1395 = Date_1395 + row        

with open('My_Event_1396.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Event_1396 =[]
     for row in reader:
        Event_1396 = Event_1396 + row

with open('My_Date_1396.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Date_1396 =[]
     for row in reader:
        Date_1396 = Date_1396 + row        

with open('My_Event_1397.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Event_1397 =[]
     for row in reader:
        Event_1397 = Event_1397 + row

with open('My_Date_1397.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Date_1397 =[]
     for row in reader:
        Date_1397 = Date_1397 + row        

with open('My_Event_1398.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Event_1398 =[]
     for row in reader:
        Event_1398 = Event_1398 + row

with open('My_Date_1398.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Date_1398 =[]
     for row in reader:
        Date_1398 = Date_1398 + row
with open('My_Event_1399.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Event_1399 =[]
     for row in reader:
        Event_1399 = Event_1399 + row
with open('My_Date_1399.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Date_1399 =[]
     for row in reader:
        Date_1399 = Date_1399 + row                
with open('My_Date_1400.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Date_1400 =[]
     for row in reader:
        Date_1400 = Date_1400 + row        

with open('My_Event_1400.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Event_1400 =[]
     for row in reader:
        Event_1400 = Event_1400 + row


with open('My_Date_1401.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Date_1401 =[]
     for row in reader:
        Date_1401 = Date_1401 + row        

with open('My_Event_1401.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Event_1401 =[]
     for row in reader:
        Event_1401 = Event_1401 + row
with open('My_Date_1402.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Date_1402 =[]
     for row in reader:
        Date_1402 = Date_1402 + row        

with open('My_Event_1402.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Event_1402 =[]
     for row in reader:
        Event_1402 = Event_1402 + row
with open('My_Date_1403.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Date_1403 =[]
     for row in reader:
        Date_1403 = Date_1403 + row        

with open('My_Event_1403.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file)
     Event_1403 =[]
     for row in reader:
        Event_1403 = Event_1403 + row        
#****************************************

def Event_to_DAte(yyyy,Question):
     my_date =[]        
     if yyyy==1395:         # in monasebat dar sale 1402 che ruzy ast
        for event in Event_1395:
            if event in Question:
               event_index = Event_1395.index(event)
               date = Date_1395[event_index]
               my_date = my_date + [date]
                  
     if yyyy==1396:       
        for event in Event_1396:
            if event in Question:
               event_index = Event_1396.index(event)
               date = Date_1396[event_index]
               my_date = my_date + [date]

     if yyyy==1397:       
        for event in Event_1397:
            if event in Question:
               event_index = Event_1397.index(event)
               date = Date_1397[event_index]
               my_date = my_date + [date]

     if yyyy==1398:       
        for event in Event_1398:
            if event in Question:
               event_index = Event_1398.index(event)
               date = Date_1398[event_index]
               my_date = my_date + [date]

     if yyyy==1399:       
        for event in Event_1399:
            if event in Question:
               event_index = Event_1399.index(event)
               date = Date_1399[event_index]
               my_date = my_date + [date]

     if yyyy==1400:       
        for event in Event_1400:
            if event in Question:
               event_index = Event_1400.index(event)
               date = Date_1400[event_index]
               my_date = my_date + [date]

     if yyyy==1401:       
        for event in Event_1401:
            if event in Question:
               event_index = Event_1401.index(event)
               date = Date_1401[event_index]
               my_date = my_date + [date]
                                                                                          
     if yyyy==1402:         
        for event in Event_1402:
            if event in Question:
               event_index = Event_1402.index(event)
               date = Date_1402[event_index]
               my_date = my_date + [date]

     if yyyy==1403:         
        for event in Event_1403:
            if event in Question:
               event_index = Event_1403.index(event)
               date = Date_1403[event_index]
               my_date = my_date + [date]

     if yyyy==1404:         
        for event in Event_1404:
            if event in Question:
               event_index = Event_1404.index(event)
               date = Date_1404[event_index]
               my_date = my_date + [date]
        
     return my_date
        
#>>>>>>> Google Conect<<<<<<<
def google(file):
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        r.adjust_for_ambient_noise(source)
        data = r.record(source)
    text = r.recognize_google(data, language='fa-IR')
    return(text)



#>>>>>>> Aryana Conect<<<<<<<
import json
import requests as req


def aryana(text):
    body = {
        "Text": text,
        "Speaker": "Female1",
        "PitchLevel": "4",
        "PunctuationLevel": "2",
        "SpeechSpeedLevel": "5",
        "ToneLevel": "10",
        "GainLevel": "3",
        "BeginningSilence": "0",
        "EndingSilence": "0",
        "Format": "wav16",
        "Base64Encode": "0",
        "Quality": "normal",
        "APIKey": "0IYTIY5JNLOU8ON"
    }
    header = {"Content-type": "application/json"}
    r = req.post("http://api.farsireader.com/ArianaCloudService/ReadText",
                 headers=header, data=json.dumps(body), timeout=10)
    return r





#>>>>>>> Google Conect<<<<<<<
        
def google(file):
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        r.adjust_for_ambient_noise(source)
        data = r.record(source)
    text = r.recognize_google(data, language='fa-IR')
    return(text)




#>>>>>>> Aryana Conect<<<<<<<
import json
import requests as req


def aryana(text):
    body = {
        "Text": text,
        "Speaker": "Female1",
        "PitchLevel": "4",
        "PunctuationLevel": "2",
        "SpeechSpeedLevel": "5",
        "ToneLevel": "10",
        "GainLevel": "3",
        "BeginningSilence": "0",
        "EndingSilence": "0",
        "Format": "wav16",
        "Base64Encode": "0",
        "Quality": "normal",
        "APIKey": "0IYTIY5JNLOU8ON"
    }
    header = {"Content-type": "application/json"}
    r = req.post("http://api.farsireader.com/ArianaCloudService/ReadText",
                 headers=header, data=json.dumps(body), timeout=10)
    return r



#>>>>>>> Today Date <<<<<<  ..........................
import datetime

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)

if mm in number1:
   mm=number2[mm]
if dd in number1:
   dd=number2[dd]   

#>>>>>>>>>>>>>>>>>!!!!!!!!!!!! Weather...*****************************************************************
import requests
import re

def Weather(city = 'Tehran',date='21-02-23',time='02:30'):
    url = ('http://api.openweathermap.org/data/2.5/forecast?q=tehran&appid=31f22d9862c83c9cb2aa02687bb25c87')
    response = requests.get(url)
    response.status_code
    data = (response.json())
    #data    
    resualt_tempature =[]
    resualt_weather=[]
    d_5_next_days = []
    All_Time_day =[]
    All_Time_temture =[]
    All_Time_weather = []    
    for W in data['list']:
        dd = W['dt_txt']
        a = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{2,4}", dd)
        b = re.findall(r"[\d]{1,2}:[\d]{1,2}:[\d]{2,4}", dd)
        This_day =[a[0],b[0],W['main']['temp'],W['weather'][0]['main']]
        if a[0] == date:
            All_Time_day = All_Time_day +[This_day[1]]
            All_Time_temture = All_Time_temture+[This_day[2]]
            All_Time_weather = All_Time_weather+[This_day[3]]
        d_5_next_days = d_5_next_days + [This_day]
        #print(d_5_next_days)
    if time!=[]:
          time_int =int(time[0:2]+time[3:5])
          for i in range(len(All_Time_day)):
            time1= All_Time_day[i]
            time1_int =int(time1[0:2]+time1[3:5]) 
            if i<len(All_Time_day)-1:
               time2 =All_Time_day[i+1]
               time2_int =int(time2[0:2]+time2[3:5])
               if time_int<time2_int and time_int>time1_int:
                  if time_int in range(21,25):                                            
                      if time2_int == '00':
                         time2_int ='24'
                  near1 = time_int-time1_int
                  near2 = time2_int-time_int
                  if near1<near2:
                      time_true = time1
                  else:
                      time_true = time2
                  if time_true !=[]:
                     time_index = All_Time_day.index(time_true)
                     resualt_tempature = All_Time_temture[time_index]
                     resualt_weather = All_Time_weather[time_index]

    return  All_Time_temture,resualt_tempature ,resualt_weather

#*************************************************************



RR= {'اذان صبح':'Fajr','نماز صبح':'Fajr', 'طلوع آفتاب':'Sunrise','نماز ظهر':'Dhuhr','اذان ظهر':'Dhuhr', 'اذان عصر':'Asr', 'غروب آفتاب':'Sunset', 'اذان مغرب':'Maghrib','نماز شب':'Maghrib','اذان عشا':'Isha', ' امساک':'Imsak', 'نیمه شب شرعی':'Midnight'}


import requests
from pprint import pprint

city = "Tehran"
country = "Iran"
method = 7 
year = 2021
month = 2
def Oghat(city = "Tehran",country = "Iran"):
    MY_Data_Oghat = []
    method = 7 
    year = 2021
    month = 1
    url = ("http://api.aladhan.com/v1/calendarByCity?city=(Tehran)&country=(country)&method=(7)&month=(month)&year=(year)")
    response = requests.get(url)
    #print(response.status_code)

    data = response.json()['data']
    MY_Data_Oghat =[]
    print(len(data))
    for i in range(len(data)):
        date_milady = data[i]['date']['gregorian']['date']
        date_hijri = data[i]['date']['hijri']['date']
        Timings = (data[i]['timings'])
        MY_Data_Oghat = MY_Data_Oghat + [[date_milady ,date_hijri ,Timings]]
        #print(data[i]['timings'])
        #print('\n<------------------------->\n')
#date_dd = data[dd-1]['date']['gregorian']['date']
#Timings_dd = (data[dd-1]['timings'])
    print(MY_Data_Oghat)     
    print(data[i]['timings']['Sunrise'])
    print(MY_Data_Oghat[0][2]['Fajr'])
    return MY_Data_Oghat

#..............................

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
#1395/1/27
year = 1400
month = 3
day =2
def My_Event(year,month,temp_day):
            url = ('https://www.time.ir/fa/event/list/0/{Year}/{Month}/{Day}')

            Event = []

            opened_url = urlopen(url.format(
                Year=year, Month=month, Day = temp_day))
            html_page = opened_url.read()
            opened_url.close()

            soup = BeautifulSoup(html_page, 'html.parser')

            Events = soup.find('ul', {'class': 'list-unstyled'})
##            print(Events.find("span"))
            type(Events.find("span"))
            if Events.find("span"):
                events = soup.find_all("span", text=re.compile(Events.span.text))
                print('{}/{}/{}'.format(year, month, temp_day))
                #print(events);
                for event in events:                
                    E = str(event.next_sibling).strip()
                
                    Event = Event +[E]
            return Event


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   
def Time_t(Time,wordsFiltered):
        wordsFiltered = wordsFiltered[0]
        if (':') in Time:
            ii = Time.index(':')
            A = Time[0:ii] 
            B = Time[ii+1:] 
        elif ('و') in Time:    
            ii = Time.index('و')
            A = Time[0:ii-1] 
            B = Time[ii+2:] 
        else:
            ii = Time.index(' ')
            A = Time[0:ii] 
            B = Time[ii+1:] 
                
        if A in Time_a:
           A= ww_Time1[A]
        if B in Time_b:
           B= ww_Time1[B]           
        for i in number1: 
          k = Time[0][0]
          if i == k:
            A = number2[i]        
        
        M = re.findall(r"[\d]{1,2}\s(?:ظهر|بعد از ظهر|عصر|غروب|شب نیمه|شب)", wordsFiltered)  
        if M !=[]:
           if M == 'ظهر' :
              B = '12'
           elif M == 'شب نیمه' :
              B = '24'                               
           elif M == 'شب' or 'غروب' or 'عصر' or 'بعد از ظهر':    
              B = ww_Time(Time[0])
           if 'شصت' in Time1[0]:
              B = A +1
              B = '00'
        if B == []:
          B = '00'                  
        new_time = A +':'+ B
        print(new_time)
        return new_time        
        #....................

def Time_h(Time):
    print(Time)
    time = word_tokenize(Time) 
    for u in time:   
       if u == 'نیم' or 'ربع':
          if u == 'نیم':
             second = '30'
             time0 = time[0] + ':'+second
             time0 =[time0]     
          elif u == 'ربع':
             second = '15'
             time0 = time[0] + ':'+second
             time0 =[time0]     
   
             return time0
        #....................
            
def MY_TIME(Question):    #......------------>>>> The Time def shoud be call
    All_Time = []
    Time0 =[]
    Time1 =[]
    Time2 =[]
    Time3 =[]
    Time4 =[]
    Time5 =[]
    Time6 =[]
    Time7 =[]
    Time_ALL =[]         

    wordsFiltered = Question[0]
    print(wordsFiltered)
    Time11 = re.findall(r"[\d]{1,2}:[\d]{1,2}", wordsFiltered)                                
    if  Time11 != []:
      for y in Time11:
         Time = y         
         Time1 = Time_t(Time,Question) 
    print('***')              
    Time22 = re.findall(r"[\d]{1,2}\s(?:و)\s[\d]{1,2}", wordsFiltered)    
                              
    if  Time22 != []:
        for y in Time22:
           Time = y
           Time2 = Time_t(Time,Question)    
    print('....')                       
    Time44 = re.findall(r"[\d]{1,2}\s(?:و)\s(?:نیم|ربع)", wordsFiltered)  # inja... 3 , 4 merge                               
    if  Time44 != []:        
        for y in Time44:           
           Time_n = y           
           time0 = Time_h(Time_n)                                        
           Time4 = Time_t(time0[0],Question)        
                                              
    Time55 = re.findall(r"[\d]{1,2}\s[\d]{1,2}", wordsFiltered)                             
    if  Time55 != []:
        for y in Time55:
            Time = y
            Time5 = Time_t(Time,wordsFiltered)            
    Time33 = re.findall(r"(?:بيست وچهار|بيست وسه|بيست ودو|بيست ويک|بيست|نوزده|هجده|هفده|شانزده|پانزده|چهارده|سيزده|دوازده|يازده|ده|نه|هشت|هفت|شش|پنج|چهار|سه|دو|يک)\s(?:و)\s[\d]{1,2}", wordsFiltered)
    print(Time33)                          
    if  Time33 != []:
        for y in Time33:
            Time = y            
            Time3 = Time_t(Time,wordsFiltered)                   
    
    Time66 = re.findall(r"[\d]{1,2}\s(?:و)\s(?:بيست وچهار|بيست وسه|بيست ودو|بيست ويک|بيست|نوزده|هجده|هفده|شانزده|پانزده|چهارده|سيزده|دوازده|يازده|ده|نه|هشت|هفت|شش|پنج|چهار|سه|دو|يک|سي ويک|سي|بيست ونه|بيست و هشت|بيست و هفت|يست وشش|بيست و پنج|سي ويک|سي|بيست ونه|بيست و هشت|بيست و هفت|يست وشش|بيست و پنج|سی ودو|سی وسه|سی وچهار|سی و پنج|سی و هفت|سی و هشت|سی و نه|چهل|چهل و یک|چهل و دو|چهل و سه|چهل و چهار|چهل و پنج|چهل و شش|چهل و هفت|چهل و هشت|چهل و نه|پنجاه|پنجاه و یک|پنجاه و دو|پنجاه و سه|پنجاه و چهار|پنجاه و پنج|پنجاه و شش|پنجاه و هفت|پنجاه و هشت|پنجاه و نه|نیم|ربع|شصت)", wordsFiltered)
    print(Time66)                          
    if  Time66 != []:
        for y in Time66:
            Time = y
            Time6 = Time_t(Time,wordsFiltered) 
                                                                                                                                                                                    
    Time77 = re.findall(r"(?:بيست وچهار|بيست وسه|بيست ودو|بيست ويک|بيست|نوزده|هجده|هفده|شانزده|پانزده|چهارده|سيزده|دوازده|يازده|ده|نه|هشت|هفت|شش|پنج|چهار|سه|دو|يک)\s(?:و)\s(?:بيست وچهار|بيست وسه|بيست ودو|بيست ويک|بيست|نوزده|هجده|هفده|شانزده|پانزده|چهارده|سيزده|دوازده|يازده|ده|نه|هشت|هفت|شش|پنج|چهار|سه|دو|يک|سي ويک|سي|بيست ونه|بيست و هشت|بيست و هفت|يست وشش|بيست و پنج|سي ويک|سي|بيست ونه|بيست و هشت|بيست و هفت|يست وشش|بيست و پنج|سی ودو|سی وسه|سی وچهار|سی و پنج|سی و هفت|سی و هشت|سی و نه|چهل|چهل و یک|چهل و دو|چهل و سه|چهل و چهار|چهل و پنج|چهل و شش|چهل و هفت|چهل و هشت|چهل و نه|پنجاه|پنجاه و یک|پنجاه و دو|پنجاه و سه|پنجاه و چهار|پنجاه و پنج|پنجاه و شش|پنجاه و هفت|پنجاه و هشت|پنجاه و نه|نیم|ربع|شصت)", wordsFiltered)
    print(Time77)                          
    if  Time66 != []:
        for y in Time66:
            Time = y
            Time7 = Time_t(Time,wordsFiltered)    
    #Time00 = re.findall(r"(?:a|ساعت)\s[\d]{1,2}", wordsFiltered)                                
     #   if  Time00 != []:            
      #      for y in number3:
       #         A = y
        #        B ='00' 
         #       for y in Time00:
          #          Time = y                 
           #         Time0 = Time_t(Time)             
    All_Time = All_Time+[Time1]+[Time2]+[Time3]+[Time4]+[Time5]+[Time6]+[Time7]
    print(All_Time)
    return All_Time

#.......................





#>>>>>>> Extract Date <<<<<< ...........................................................

def MY_DATE(wordsFiltered,mm,dd,yyyy):    #................
#if A in: #1-2-1393-4 #2-2020 #2-5-1944 #to milady  date=.... :else:
    Date =[]
    MY_date=[]
    wordsFiltered = wordsFiltered[0]
    date0 = re.findall(r"[\d]{1,2}\s[\d]{1,2}\s[\d]{2,4}", wordsFiltered) # 2 3 99 & 1 4 1399        
    date1 = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{2,4}", wordsFiltered)  # 1/3/99 &  1/12/1399
    date2 = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{2,4}", wordsFiltered)   #2-2020 &2-5-1944 
    date2 = re.findall(r"[\d]{1,2}[\d]{1,2}[\d]{2,4}", wordsFiltered)
    date3 = re.findall(r"[\d]{1,2}/[\d]{1,2,4}", wordsFiltered)#***  1/2   1/99.....
    date4 = re.findall(r"[\d]{1,2}-[\d]{1,2,4}", wordsFiltered)
    MY_date = MY_date + [date0]+ [date1]+[date2]+[date3]+[date4]

    print(date0,date1,date2,date3,date4)
    if date0 != []:
       for my_date in date0:
            a =my_date.index(' ')
            b= my_date[0:a]            
            if b in number1:
               b=number2[b]            
            my_date = my_date[a:]               
            v =my_date.index(' ')
            yy= my_date[0:v]            
            if yy in number1:
               yy=number2[yy]
               if len(yy)==2:
                 yy = '13' + yy
            date0 = [a,b,yy]
       Date = Date +[date0]
          
    date5 = re.findall(r"([\d]{1,2}\s(?:فروردين|ارديبهشت|خرداد|تير|مرداد|شهريور|مهر|آبان|آذر|دي|اسفند|بهمن|امرداد|فبريه|ژانويه|مارس|آوريل|مه|ژوئن|ژوئیه|آگوست|سپتامبر|نوامبر|اکتبر|دسامبر|محرم|صفر|ربيع الاول|ربيع الثاني|جمادي الاول|جمادي الثاني|رجب|شعبان|رمضان|شوال|ذيقعده|ذيحجه)\s[\d]{2,4})", wordsFiltered)
    date6 = re.findall(r"(?:سي ويک|سي|بيست ونه|بيست و هشت|بيست و هفت|يست وشش|بيست و پنج|بيست وچهار|بيست وسه|بيست ودو|بيست ويک|بيست|نوزده|هجده|هفده|شانزده|پانزده|چهارده|سيزده|دوازده|يازده|ده|نه|هشت|هفت|شش|پنج|چهار|سه|دو|يک)\s(?:فروردين|ارديبهشت|خرداد|تير|مرداد|شهريور|مهر|آبان|آذر|دي|اسفند|بهمن|امرداد|فبريه|ژانويه|مارس|آوريل|مه|ژوئن|ژوئیه|آگوست|سپتامبر|نوامبر|اکتبر|دسامبر|محرم|صفر|ربيع الاول|ربيع الثاني|جمادي الاول|جمادي الثاني|رجب|شعبان|رمضان|شوال|ذيقعده|ذيحجه)\s[\d]{2,4}", wordsFiltered)
    
    
    #date7 = re.findall(r"((?:سي ويک|سي|بيست ونه|بيست و هشت|بيست و هفت|يست وشش|بيست و پنج|بيست وچهار|بيست وسه|بيست ودو|بيست ويک|بيست|نوزده|هجده|هفده|شانزده|پانزده|چهارده|سيزده|دوازده|يازده|ده|نه|هشت|هفت|شش|پنج|چهار|سه|دو|يک)\s(?:فروردين|ارديبهشت|خرداد|تير|مرداد|شهريور|مهر|آبان|آذر|دي|اسفند|بهمن|امرداد|فبريه|ژانويه|مارس|آوريل|مه|ژوئن|ژوئیه|آگوست|سپتامبر|نوامبر|اکتبر|دسامبر|محرم|صفر|ربيع الاول|ربيع الثاني|جمادي الاول|جمادي الثاني|رجب|شعبان|رمضان|شوال|ذيقعده|ذيحجه))\s(?:هزارو سيصدونودونه|هزاروچهارصدوچهار|هزاروچهارصدوسه|هزاروچهارصدودو|هزاروچهارصدویک|هزاروچهارصد|هزاروسیصدونودونه|هزاروسیصدونودوهشت|هزاروسیصدونودوهفت|هزاروسیصدونودوشش|هزاروسیصدونودوپنج|هزاروسیصدونودوچهار)", wordsFiltered)
    #date8 = re.findall(r"([\d]{1,2}\s(?:فروردين|ارديبهشت|خرداد|تير|مرداد|شهريور|مهر|آبان|آذر|دي|اسفند|بهمن|امرداد|فبريه|ژانويه|مارس|آوريل|مه|ژوئن|ژوئیه|آگوست|سپتامبر|نوامبر|اکتبر|دسامبر|محرم|صفر|ربيع الاول|ربيع الثاني|جمادي الاول|جمادي الثاني|رجب|شعبان|رمضان|شوال|ذيقعده|ذيحجه)\s(?:هزارو سيصدونودونه|هزاروچهارصدوچهار|هزاروچهارصدوسه|هزاروچهارصدودو|هزاروچهارصدویک|هزاروچهارصد|هزاروسیصدونودونه|هزاروسیصدونودوهشت|هزاروسیصدونودوهفت|هزاروسیصدونودوشش|هزاروسیصدونودوپنج|هزاروسیصدونودوچهار))", wordsFiltered)
    date9 = re.findall(r"([\d]{1,2}\s(?:فروردين|ارديبهشت|خرداد|تير|مرداد|شهريور|مهر|آبان|آذر|دي|اسفند|بهمن|امرداد|فبريه|ژانويه|مارس|آوريل|مه|ژوئن|ژوئیه|آگوست|سپتامبر|نوامبر|اکتبر|دسامبر|محرم|صفر|ربيع الاول|ربيع الثاني|جمادي الاول|جمادي الثاني|رجب|شعبان|رمضان|شوال|ذيقعده|ذيحجه))", wordsFiltered)
    date10 = re.findall(r"((?:سي ويک|سي|بيست ونه|بيست و هشت|بيست و هفت|يست وشش|بيست و پنج|بيست وچهار|بيست وسه|بيست ودو|بيست ويک|بيست|نوزده|هجده|هفده|شانزده|پانزده|چهارده|سيزده|دوازده|يازده|ده|نه|هشت|هفت|شش|پنج|چهار|سه|دو|يک)\s(?:فروردين|ارديبهشت|خرداد|تير|مرداد|شهريور|مهر|آبان|آذر|دي|اسفند|بهمن|امرداد|فبريه|ژانويه|مارس|آوريل|مه|ژوئن|ژوئیه|آگوست|سپتامبر|نوامبر|اکتبر|دسامبر|محرم|صفر|ربيع الاول|ربيع الثاني|جمادي الاول|جمادي الثاني|رجب|شعبان|رمضان|شوال|ذيقعده|ذيحجه)\s(?:هزارو سيصدونودونه))", wordsFiltered)
    #date11 = re.findall(r"[\d]{1,2}/[\d]{1,2}\s(?:هزارو سيصدونودونه|هزاروچهارصدوچهار|هزاروچهارصدوسه|هزاروچهارصدودو|هزاروچهارصدویک|هزاروچهارصد|هزاروسیصدونودونه|هزاروسیصدونودوهشت|هزاروسیصدونودوهفت|هزاروسیصدونودوشش|هزاروسیصدونودوپنج|هزاروسیصدونودوچهار)", wordsFiltered)

    date12 = re.findall(r"((?:سي ويک|سي ويکم|سي ام|بيست ونهم|بيست و هشتم|بيست و هفتم|بيست وششم|بيست و پنجم|بيست وچهارم|بيست وسوم|بيست ودوم|بيست ويکم|بيستم|نوزدهم|هجدهم|هفدهم|شانزدهم|پانزدهم|چهاردهم|سيزدهم|دوازدهم|يازدهم|دهم|نهم|هشتم|هفتم|ششم|پنجم|چهارم|سوم|دوم|یکم|اول)\s(?:فروردين|ارديبهشت|خرداد|تير|مرداد|شهريور|مهر|آبان|آذر|دي|اسفند|بهمن|امرداد|فبريه|ژانويه|مارس|آوريل|مه|ژوئن|ژوئیه|آگوست|سپتامبر|نوامبر|اکتبر|دسامبر|محرم|صفر|ربيع الاول|ربيع الثاني|جمادي الاول|جمادي الثاني|رجب|شعبان|رمضان|شوال|ذيقعده|ذيحجه)\s(?:هزارو سيصدونودونه|هزاروچهارصدوچهار|هزاروچهارصدوسه|هزاروچهارصدودو|هزاروچهارصدویک|هزاروچهارصد|هزاروسیصدونودونه|هزاروسیصدونودوهشت|هزاروسیصدونودوهفت|هزاروسیصدونودوشش|هزاروسیصدونودوپنج|هزاروسیصدونودوچهار))", wordsFiltered)
    date13 = re.findall(r"((?:سي ويک|سي ويکم|سي ام|بيست ونهم|بيست و هشتم|بيست و هفتم|بيست وششم|بيست و پنجم|بيست وچهارم|بيست وسوم|بيست ودوم|بيست ويکم|بيستم|نوزدهم|هجدهم|هفدهم|شانزدهم|پانزدهم|چهاردهم|سيزدهم|دوازدهم|يازدهم|دهم|نهم|هشتم|هفتم|ششم|پنجم|چهارم|سوم|دوم|یکم|اول)\s(?:فروردين|ارديبهشت|خرداد|تير|مرداد|شهريور|مهر|آبان|آذر|دي|اسفند|بهمن|امرداد|فبريه|ژانويه|مارس|آوريل|مه|ژوئن|ژوئیه|آگوست|سپتامبر|نوامبر|اکتبر|دسامبر|محرم|صفر|ربيع الاول|ربيع الثاني|جمادي الاول|جمادي الثاني|رجب|شعبان|رمضان|شوال|ذيقعده|ذيحجه)\s[\d]{2,4})", wordsFiltered)

    date14 = re.findall(r"((?:one|سال|هفته|روز|ماه)\s(?:پیش|قبل|گذشته|بعد|آینده))", wordsFiltered)
    if date14 != []:
        for p in date14:
            if (p == 'روز قبل' or 'روز آینده' or 'روز گذشته' or 'روز بعد' or 'روز پیش'):
                ruz = 'روز'
                for l in lemwords:
                    if l == ruz:
                       index_ruz = lemwords.index(ruz)
                       pre_ruz_index = index_ruz -1
                       next_ruz_index = index_ruz +1

                       if (lemwords[next_ruz_index] =='پیش' or 'قبل' or 'گذشته'):
                           pre = lemwords[pre_ruz_index]
                           for h in Adad:
                               if pre == h:
                                   return h                               
                               else:
                                  h = 1
                               dd=int(dd)             
                               if (dd != '01'):
                                   dd = int(dd)
                                   dd = dd - h
                                   dd = str(dd)
                               else:
                                   mm = int(mm)
                                   if (mm<=7 and mm>=1):
                                      dd = '31'
                                      mm = mm-1
                                      mm = str(mm)
                                   elif (mm>7 and mm<12):
                                      dd = '30'
                                      mm = mm-1
                                      mm = str(mm)
                                   else:
                                       yyyy = int(yyyy)
                                       if (yyyy%4 == 0):
                                          dd='30'
                                          mm = str(mm)
                                          mm = '12'
                                          yyyy -= 1
                                          yyyy = str(yyyy)
                                       else:
                                          dd="29"
                                          mm = str(mm)
                                          mm = '12'
                                          yyyy -= 1
                                          yyyy = str(yyyy)
                       if (lemwords[next_ruz_index] =='بعد' or 'آینده'):                           
                           pre = lemwords[pre_ruz_index]
                           for h in Adad:
                               if pre == h:
                                   return h                               
                               else:
                                  h = 1
                           dd=int(dd)          
                           if (dd<30):
                                dd += h
                                dd = str(dd)
                           else:
                                mm = int(mm)
                                if (mm <= 6):
                                   if (dd<31):
                                      dd += 1
                                      dd = str(dd)
                                   else:
                                      dd = '01'
                                      mm = mm + 1
                                elif (mm <12):
                                    if (dd<30):
                                       dd += 1
                                       dd = str(dd)
                                    else:
                                       dd = '01'
                                       mm = mm + 1
                                else:
                                    yyyy= int(yyyy)
                                    if (yyyy%4 == 3):
                                       if (dd<30):
                                          dd += 1
                                          dd = str(dd)
                                       else:
                                          dd = '01'
                                          mm = '01'
                                    else:
                                        dd ='01'
                                        mm = '01'
                                        yyyy += 1
                                        yyyy = str(yyyy)      
                           mm = str(mm)  
                       date_ok = '-'+ mm +'-'+ dd
                       date.append(date_ok)
                       calendar_type.append("شمسی")    
    
    day_name = re.findall(r"(?:پس فردا|پریروز|دیروز|فردا|فردای|روز بعد|دیشب|فردای)",wordsFiltered)  #ruz - sal..... #پس فردا
    #if day_name != []:
        #date15  = date_2(wordsFiltered)#,dd,mm,yyyy,day_name)
            #if (p == 'ماه قبل' or 'ماه  آینده' or 'ماه گذشته' or 'ماه بعد' or 'ماه پیش'):
             #      if l == ruz
              #         index_ruz = lemwords.index(ruz)
               #        pre_ruz_index = index_ruz -1
                #       next_ruz_index = index_ruz +1
                 ##          pre = lemwords[pre_ruz_index]
                      #      if (pre = ):
                   #             dd = dd+30
                    #        else
                     #           dd = dd +1
                       #if (lemwords[next_ruz_index] =='پیش' or 'قبل' or 'گذشته'):
                        #   pre = lemwords[pre_ruz_index]
            #if (p == 'هفته قبل' or 'هفته آینده' or 'هفته گذشته' or 'هفته بعد' or 'هفته پیش'):
             #    for l in lemwords:
              #      if l == ruz
               #        index_ruz = lemwords.index(ruz)
                #       pre_ruz_index = index_ruz -1
                 #      next_ruz_index = index_ruz +1
                  #     if (lemwords[next_ruz_index] =='بعد' or 'آینده'):                           
                   #         pre = lemwords[pre_ruz_index]
                    #        if (pre = ):
                     #           dd = dd+7
                      #      else
                       #         dd = dd +1
                       #if (lemwords[next_ruz_index] =='پیش' or 'قبل' or 'گذشته'):
                        #   pre = lemwords[pre_ruz_index]
    Date = date1+ date2 + date3+ date4+ date5 + date6# + date7 + date8+ date9 + date10+ date11+ date12 + date13#+ date20 
    return Date


################################################ Religious Time Argoman ##################################
#Month_Shamsi = '{"فروردين":"1", "ارديبهشت":"2", "خرداد":"3", "تير":"4", "مرداد":"5", "شهريور":"6","مهر":"7", "آبان":"8", "آذر":"9", "دي":"10", "بهمن":"11", "اسفند":"12"}'
#Month_Milady = '{"ژانويه":"1", "فبريه":"2", "مارس":"3", "آوريل":"4", "مه":"5", "ژوئن":"6","ژوئیه":"7", "آگوست":"8", "سپتامبر":"9", "اکتبر":"10", "نوامبر":"11", "دسامبر":"12"}'
#Month_Ghamari = '{"محرم":"1", "صفر":"2", "ربيع الاول":"3", " ربيع الثاني":"4", "جمادي الاول":"5", " جمادي الثاني ":"6","رجب ":"7", "شعبان":"8", "رمضان ":"9", " شوال ":"10", "ذيقعده":"11", " ذيحجه":"12"}'
Month_ALL_code ='{"فروردين":"1", "ارديبهشت":"2", "خرداد":"3", "تير":"4", "مرداد":"5", "شهريور":"6","مهر":"7", "آبان":"8", "آذر":"9", "دي":"10", "بهمن":"11", "اسفند":"12","ژانويه":"1", "فبريه":"2", "مارس":"3", "آوريل":"4", "مه":"5", "ژوئن":"6","ژوئیه":"7", "آگوست":"8", "سپتامبر":"9", "اکتبر":"10", "نوامبر":"11", "دسامبر":"12","محرم":"1", "صفر":"2", "ربيع الاول":"3", " ربيع الثاني":"4", "جمادي الاول":"5", " جمادي الثاني ":"6","رجب ":"7", "شعبان":"8", "رمضان ":"9", " شوال ":"10", "ذيقعده":"11", " ذيحجه":"12"}'
RR= {'اذان صبح':'Fajr','نماز صبح':'Fajr', 'طلوع آفتاب':'Sunrise','نماز ظهر':'Dhuhr','اذان ظهر':'Dhuhr', 'اذان عصر':'Asr', 'غروب آفتاب':'Sunset', 'اذان مغرب':'Maghrib','نماز شب':'Maghrib','اذان عشا':'Isha', ' امساک':'Imsak', 'نیمه شب شرعی':'Midnight'}

pp = '{"7":"جمعه","6":"پنجشنبه","5":"چهارشنبه","4":"سه شنبه","3":"دوشنبه","2":"يکشنبه","1":"شنبه","7":"جمعه","6":"پنجشنبه","5":"چهارشنبه","4":"سه شنبه","3":"دوشنبه","2":"يکشنبه","1":"شنبه"}'
oo ='{"31":"سي ويکم","30":"سي ام","29":"بيست ونهم","28":"بيست و هشتم","27":"بيست و هفتم","26":"بيست وششم","25":"بيست و پنجم","24":"بيست وچهارم","23":"بيست وسوم","22":"بيست ودوم","21":"بيست ويکم","20":"بيستم","19":"نوزدهم","18":"هجدهم","17":"هفدهم","16":"شانزدهم","15":"پانزدهم","14":"چهاردهم","13":"سيزدهم","12":"دوازدهم","11":"يازدهم","10":"دهم","9":"نهم","8":"هشتم","7":"هفتم","6":"ششم","5":"پنجم","4":"چهارم","3":"سوم","2":"دوم","1":"اول"}'

Miladyy = ['دوهزاروبیست وپنج','دوهزاروبیست وچهار','دوهزارو بیست وسه','دوهزاروبیست ودو','دوهزاروبیست ویک','دوهزاروبیست','دوهزارونوزده','دوهزارو هجده','دوهزاروهفده','دوهزاروشانزده','دوهزاروپانزده']
Ghamaryy = [' هزاروچهارصدوچهل وهفت',' هزاروچهارصدوچهل وشش',' هزاروچهارصدوچهل وپنج',' هزاروچهارصدوچهل وچهار',' هزاروچهارصدوچهل وسه',' هزاروچهارصدوچهل ودو',' هزاروچهارصدوچهل ویک','هزاروچهارصدوچهل',' هزاروسیصدوسی ونه','هزاروسیصدوسی وهشت','هزاروسیصدوسی وهفت']
Shamsy = [' هزاروچهارصدوچهار',' هزاروچهارصدوسه',' هزاروچهارصدودو',' هزاروچهارصدویک','هزاروچهارصد',' هزاروسیصدونودونه',' هزاروسیصدونودوهشت',' هزاروسیصدونودوهفت',' هزاروسیصدونودوشش',' هزاروسیصدونودوپنج','هزاروسیصدونودوچهار']
dddd = '{"سي ويکمين:31","سيمين:30","بيست ونهمين:29","بيست وهشتمين:28","بيست وهفتمين:27","بيست وششمين:26","بيست وپنجمين:25","بيست وچهارمين:24","بيست وسومين:23","بيست ودومين:22","بيست ويکمين:21","بيستمين:20","نوزدهمين:19","هجدهمين:18","هفدهمين:17","شانزدهمين:16","پانزدهمين:15","چهاردهمين:14","سيزدهمين:13","دوازدهمين:12","يازدهمين:11","دهمين:10","نوهمين:9","هشتمين:8","هفتمين:7","ششمين:6","پنجمين:5","چهارمين:4","سومين:3","دومين:2","نخستين:1"}'
keys = ['امروز','ديروز','فردا','پس فردا','هفته بعد','هفته قبل','ماه بعد','ماه قبل']

religious_type_eng= {"سپيده دم":'Sunrise','اشا':'Isha','اشاء':'Isha','طلوع':'Sunrise','غروب':'Sunset','شب هنگام':'Sunset','اذان صبح':'Fajr','نماز صبح':'Fajr','نماز ظهر':'Dhuhr','اذان ظهر':'Dhuhr', 'اذان عصر':'Asr',  'اذان مغرب':'Maghrib','نماز شب':'Maghrib','اذان عشا':'Isha', ' امساک':'Imsak', 'نیمه شب شرعی':'Midnight'}
religious_type_fa= {"سپيده دم":'طلوع آفتاب','اشا':'اذان عشا','عشا':'اذان عشا','اشاء':'اذان عشا','طلوع خورشيد':'طلوع آفتاب','غروب خورشید':'غروب آفتاب','شب هنگام':'غروب آفتاب','نماز صبح':'اذان صبح','نماز ظهر':'اذان ظهر','نماز شب':'نماز مغرب','نماز شب':'نماز عشا', 'نیمه شب':'نیمه شب شرعی'}


def religious_type(wordsFiltered):
    Religious__list =[]
    Religious__list_eng =[]
    My_religious = re.findall(r"(?:اذان صبح|طلوع|غروب|نماز صبح|سپيده دم|اشا|اشاء|شب هنگام|نماز ظهر|اذان ظهر|اذان عصر|اذان مغرب|نماز شب|عشا|امساک|نیمه شب)",wordsFiltered[0])
    if My_religious !=[] :
       for k in My_religious:
           Rel = religious_type_fa[k]
           Religious__list = Religious__list + [Rel]
           Religious__list_eng = Religious__list_eng + [religious_type_eng[Rel]]
    return Religious__list ,Religious__list_eng

                
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
Question_weather=['دمای هوای تهران امروز چقدر است؟','دمای هوای فردای شیراز ساعت ۱۴ و ۲۵ دقیقه چقدر است',#1
                  'دمای هوای فردای شیراز ساعت ۱۴:۲۵ چقدر است؟','دمای هوا در زمان اذان صبح امروز تهران چقدر است؟',#1
                  'دمای هوای دو روز بعد گرگان چند درجه سانتیگراد است؟', 'درجه دمای هوای ۳ روز دیگر رم ساعت ۱۶:۱۰ چند درجه است؟',
                  'گرمی هوای فردای تهران ساعت ۱۹:۱ چقدر است؟ ','درجه حرارت هوای دو روز بعد پکن ساعت ۲۰:۱۰ به چه میزان است؟',#1
                  'میانگین دمای هوای تهران امروز چقدر است؟', 'میانگین اندازه گرمی یا سردی هوای دو روز بعد کاشان چند درجه است؟',#2
                  'امروز حداقل دمای هوای مشهد سردتر است یا تهران؟',#3
                  'اذان صبح تهران سردتر است یا اذان ظهر آن؟']#4        
            #.............................................................#
Question_Re = ['اذان صبح امروز تهران چه ساعتی است؟ ','اذان ظهر فردای تهران چه ساعتی است؟ ', #1
      'اذان ظهر دیروز تهران چه ساعتی بود؟', 'اذان مغرب دیروز قم چه ساعتی بود؟', 
      'اذان ظهر پس فردای تهران چه ساعتی است؟','نیمه شب شرعی تهران چه ساعتی است؟ ',
      'اذان صبح مسکو چه ساعتی است؟ ','طلوع آفتاب مسکو چه ساعتی است؟', 
      'غروب آفتاب مشهد چه ساعتی است؟ ','غروب آفتاب کابل چه ساعتی است؟',
      'اذان ظهر بیروت چه زمانی است؟ ', 'اذان ظهر فردای تورنتو چه زمانی است؟'
      'اذان مغرب پریروز قم چه ساعتی بود؟ ', 'اذان ظهر ۴ روز پیش قم چه ساعتی بود؟',#2 
      'اذان ظهر هفته ی قبل شیراز چه ساعتی بود؟',
      'اذان ظهر هفته ی بعد شیراز چه ساعتی است؟ ', 
      'اذان صبح امروز دوحه چه ساعتی است؟ ','اذان ظهر امروز بغداد چه ساعتی است؟ ', 
      'اذان ظهر امروز تهران چه زمانی است؟',
      'ساعت اذان ظهر بیروت؟ '] #3
      
            #.....................................................................#
Question_Time=['ساعت در تهران چند است؟',      #1
     'ساعت به وقت ابوظبی چند است؟ ',      
     'الان به وقت تهران چه زمانی از روز است؟ ', #2 صبح.... ظهر .... شب
     'الان در سنگاپور چه ساعتی در شبانه روز است؟',      #1
     'الان در استکهلم ساعت دقیقا چند است؟',      
     'در این لحظه ساعت مسکو چند است؟', 
     'ساعت به وقت بیروت چند است؟', 
     'در تاشکند، این لحظه چه زمانی از روز است؟',      #2
     'ساعت به طور دقیق در استانبول چند است؟',      
     'ساعت فعلی در تورنتو؟',      #1
     'در کابل چه زمانی از روز است؟ ', #2
     'ساعت فعلی ونکوور چند است؟',   #1
     'ساعت در شهر زوریخ چند است؟', 
     'ساعت دبی در این لحظه چند است؟', 
     'ساعت در لس آنجلس چند است؟', 
     'اکنون در ریاض چه زمانی از روز است؟',       
     'اکنون در شهر باکو ساعت چند است؟', 
     'ساعت در پایتخت ایران چند است؟',      
     'در پایتخت روسیه چه زمانی از روز است؟',                 
     'الان به وقت پایتخت ازبکستان چه زمانی از روز است؟']
           #.....................................................................................#   
Question_T=['روز حافظ در سال ۹۹ چه روزی است؟',  'هوای فردای شیراز ساعت ۱۴ و ۲۵ دقیقه چقدر است'           #1  
    'در سال ۹۷ روز جهانی محیط زیست چه روزی است؟',     
    'کدام روز از سال ۱۴۰۳ روز اصناف است؟',                  #1
    'سالروز زمین لرزه ی بم در سال ۹۹کدام روز است؟',     #1
    'امسال جشن سده در کدام روز است؟',       #1
    'روز جهانی بهداشت در سال ۹۹کدام روز از سال است؟',  #1
    'سالگرد درگذشت پروین اعتصامی در سال ۱۳۹۶ کدام روز است؟',         
    'روز جمهوری اسلامی در سال ۱۴۰۰؟', 
    'کدام روز از سال ۱۴۰۰ روز قلم است؟',   #1
    'سالگرد اعلام پذیرش قطعنامه ۵۹۸ شورای امنیت از سوی ایران در کدام روز ۱۴۰۰ اتفاق افتاده است؟', #1
    'تاریخ روز صنعت و معدن امسال چه روزی است؟ ',    #1
    'در این سال روز عرفه چه روزی بود؟', 
    'تاریخ برگزاری اولین کنکور در ایران؟ ', 
    'روز خبرنگار کدام روز از امسال است؟',     
    'تاریخ ولادت امام موسی کاظم علیه السلام در سال ۹۹؟',      
    'روز بزرگداشت ابوعلی سینا و روز پزشک در کدام روز سال ۹۹است؟',        
    'مناسبت روز ۱۸ اسفند امسال چیست؟ ',                    #2    
    'بهمن امسال به میلادی؟ ۲۲',                 #3        
    'سال شمسی امسال چند روز است؟',        #4
    'تاریخ شمسی امروز؟',                #5
    'تاریخ میلادی امروز؟',     
    'تعداد روزهای اسفند ۱۴۰۰؟']             #6
    
   
MY_Data_test = Question_weather + Question_Re + Question_Time+ Question_T

MY_Data_label =[1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,23,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
        #.............................................................................................#
#>>>>>>> T <<<<<<



#@@@@@@@@ >>> START <<< @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



class BOT:
    def __init__(self):
        self.modified = False

    def is_modified(self):
        return self.modified

   
    def aibot(self, Question):
        
                #.......
        Type_list =  []
        City_list =[]
        Date_list =[]
        Time_list =[]
        Religious__list =[]
        Calender_list =[]
        Event__list =[]
        Api_list =[]
        Result_list =[]  # temp answer

        resualt_RE =[]

        answer = {'type': Type_list, 'city': City_list, 'date': Date_list,'time': Time_list,'religious_time': Religious__list, 'calendar_type': Calender_list, 'event': Event__list, 'api_url': Api_list,'result': Result_list}

                #>>>>>>>>>>>>>> Today Date >>>>>........
        
        
       #>>>>>>> Today Date <<<<<<  ..........................


        now = datetime.datetime.today()
        mm = str(now.month)
        dd = str(now.day)
        yyyy = str(now.year)
        hour = str(now.hour)
        mi = str(now.minute)
        ss = str(now.second)

        if mm in number1:
            mm=number2[mm]
        if dd in number1:
            dd=number2[dd]


        
        #>>>>>>>>start                    
        Question = google(Question)
        #normalizer = Normalizer()
        #Question = normalizer.normalize(Question)
        Question = [Question]
        print(Question[0])
        #********** The Type of Question
        for g in range(len(MY_Data_test)):
            r = textdistance.hamming.normalized_similarity(Question[0],MY_Data_test[g] )            
            resualt_RE = resualt_RE +[r]
        print(resualt_RE)
        max_r = max(resualt_RE)
        print(max_r)
        Max_all_similarity_index = resualt_RE.index(max_r)    # Max_all_similarity is sentence index %number 
        
        if max_r<0.1:     # bayad barresy beshe??????!!!!!!!!!!!!!!!!!!!!!!!
           Type_list = Type_list + ['-1']
           My_answer = 'سوال شما فراتر از دانش من مي باشد . اطلاعات من در زمينه اعلام دما ، اعلام اوقات شرعي ، اعلام ساعت در تمام نقاط جهان و مناسبت مرتبط با تاريخ مي باشد. لطفا سوال ديگري بپرسيد. تشکر از شما'
           print(My_answer)
        else:
        
        
            #clf.predict(count_vect.transform(Question))    #label for predict...

            label_similarity = MY_Data_label[Max_all_similarity_index] #label for similarity...
            print(label_similarity)
        #********************
                    


 
                        
            #...........................................................
            label = label_similarity
            label = 2

            #word_token = word_tokenize(A)
            #Lem=[]
            #for c in word_token:
             #   ll=lemmatizer.lemmatize(c)
              #  Lem= Lem+[ll]

            if label == 1:   #'21-02-26'

               time_in = MY_TIME(Question)      # با فرض يک ساعت داشتن
               print(time_in)
               #for h in time_in:
                #   Question1 = Question.replace(h[0])
                
              #TIME
               if time_in ==[]:
                  time_in = hour + ':'+mi              

               #DATE
               date_in = MY_DATE(Question,mm,dd,yyyy)
               
               #Question2 = Question1.replace(i)
               if date_in ==[]:
                 date_in = yyyy[2:] + '-' + mm + '-' + dd
                 
               print(date_in,time_in)

               #CITY
               #MY_city_data = MY_City(Question)                                
               #word_token = word_tokenize(Question)
               City =[]
               word_token =['هوای', 'فردای', 'شیراز', 'ساعت', '۱۴', 'و', '۲۵', 'دقیقه', 'چقدر', 'اس']
               for c_city in city_Fa:                      
                  for word in word_token:
                      if c_city == word:
                         City = City+c_city                                   
               if City==[]:   
                  City = 'Tehran'
               print(City)                               
               for t in range(len(City)):                                    
                 All_Time_temture,resualt_tempature ,resualt_weather  =Weather(city = City[t],date=date_in[t],time=time_in[0])
            
               URL = "https://api.openweathermap.org/data/2.5/weather"
               Type_list = Type_list + ['1']
               City_list = City_list + [City]
               Date_list = Date_list + [date_in]
               Time_list = Time_list + [time_in]
               Api_list = Api_list +[URL]
               Result_list = Result_list + [resualt]

            #@@@
            if label == 2:

               #DATE  .................................  01-02-2021
               date_in = MY_DATE(Question,mm,dd,yyyy)
               
               #Question2 = Question1.replace(i)
               if date_in ==[]:
                  date_in = dd + '-' + mm + '-' + yyyy

               #City....
               City =[]
               Country =[]
               word_token =['هوای', 'فردای', 'شیراز', 'ساعت', '۱۴', 'و', '۲۵', 'دقیقه', 'چقدر', 'اس']
               for c_city in city_Fa:                      
                   for word in word_token:
                       if c_city == word:
                          city_index = city_Fa.index(c_city)
                          City = City+c_city
                          c_country = country[city_index]
                          Country = Country+c_country
               if City==[] :   
                  City = 'Tehran'
                  Country ="Iran"
               print(City)
               print(Country) 
               When_w = []
               Result =[]
               for i in range(len(City)):
                    city = City[i]   
                    country = Country[i]                                        
                    Religious__list ,Religious__list_eng = religious_type(Question)

                    date = date_in[i]    #>>>>>>>>????????????2 ta tarikh...
                    When = Religious__list[i]
                    Religous_timeOghat =Oghat(city = "Tehran",country = "Iran")
                    
                    a_milady=[(index, row.index(date)) for index, row in enumerate(Religous_timeOghat) if date in row]
                    makan_tarikh = a_milady[0][0]
                    result = Religous_timeOghat[makan_tarikh][2][Religious__list_eng]

                    When_w = When_w +When
                    Result =Result + result
               URL = ("http://api.aladhan.com/v1/calendarByCity?city=(Tehran)&country=(Iran)&method=(7)&month=(month)&year=(year)")
               Type_list = Type_list + ['2']       
               City_list = City_list + [City]
               Date_list = Date_list + [Date]               
               Api_list = Api_list +[URL]
               Religious__list = Religious__list +[When_w]
               Result_list = Result_list + Result
               
            if label == 3:

               City =[]
               Country =[]
               Area =[]
               #word_token = word_tokenize(Question)
               word_token =['هوای', 'فردای', 'شیراز', 'ساعت', '۱۴', 'و', '۲۵', 'دقیقه', 'چقدر', 'اس']
               for c_city in city_Fa:                      
                     for word in word_token:
                         if c_city == word:
                            city_index = city_Fa.index(c_city)
                            City = City+c_city
               for c_country in country_Fa:                      
                     for word in word_token:
                         if c_country == word:
                            Country_index = country_Fa.index(c_country)
                            cc_city = city_country_Fa[Country_index]
                            City = City + cc_city
                            Country = Country + c_country       #Area????
                            
               if City==[] :   
                  City = 'Tehran'
                  area = 'Asia'
                  
               print(City)
               print(Country) 
               

               url = 'http://worldtimeapi.org/api/timezone/{Area}/{City}'
               city = 'Tehran'
               area = 'Asia'
               res = requests.get(url.format(Area=area,City=city))
               print(res.json())
                
               for i in range(len(City)):     
                    city = City[i]
                    area = Area[i]
                    url = 'http://worldtimeapi.org/api/timezone/{Area}/{City}'                                                  
               Type_list = Type_list + ['3']       
               City_list = City_list + [City]               
               Api_list = Api_list +[url]
               Result_list = Result_list +[resualt]


            if label == 4:

               #DATE  .................................  1399/3/4
               my_date =[]
               date_in = MY_DATE(Question,mm,dd,yyyy)
               if date_in==[]:
                  date_in = [[yyyy ,mm,dd]]

               #dar tarikh  
               #if ....

               for i in range(len(date_in)):
                 d = date_in[0][i]
                 dd = d[0]
                 mm = d[1]
                 yyyy = d[2]
                 if 'چه روزي است' in Question:                    
                    Event_to_DAte(yyyy,Question)
                    
                 if 'مناسبت' or 'رويداد' or 'رخداد' in lem_word:                        

                     My_Event(yyyy,mm,dd)                 
               
                 if ('شمسی' or 'میلادی'or 'قمری') in Question:
                    if 'شمسی' in Question :
                          jalili_date =  jdatetime.date.fromgregorian(dd,mm,yyyy) # Milady to Shamsy
                          a = jalili_date.index('-')
                          yyyy = jalili_date[0:a]
                          jalili_date = jalili_date[a:]
                          b = jalili_date.index('-')
                          mm = jalili_date[0:b]
                          dd = jalili_date[b:]
                          Event = My_Event(yyyy,mm,dd)                           
                       
                    if 'میلادی' in Question :   #.strftime("%d-%m-%Y")
                       gregorian_date = jdatetime.date(yyyy,mm,dd).togregorian()# Shamsy to Milady
                    if 'قمری' in Question :   
                       gregorian_date = jdatetime.date(yyyy,mm,dd).togregorian()# Shamsy to Milady
                       a = gregorian_date.index('-')
                       yyyy = gregorian_date[0:a]
                       gregorian_date = gregorian_date[a:]
                       b = gregorian_date.index('-')
                       mm = gregorian_date[0:b]
                       dd = gregorian_date[b:]
                       h = convert.Gregorian(yyyy,mm,dd).to_hijri()  # milady to Ghamary
               Date = Event_to_DAte(yyyy,Question)
               URL = ('https://www.time.ir/fa/event/list/0/(Year)/(Month)/(Day)')
               Type_list = Type_list + ['4']
               Api_list = Api_list +[URL]
               
               Date_list = Date_list + [Date]
               Calender_list = Calender_list +[]
               Event__list =Event__list +[]
               Result_list = Result_list + [resualt]
               
              #if city != [] and Tarikh_true!= [] and Saat_true != [] and ZAman_true != [] and taghvim:
            #answer['type'] = -1   
                       #g = convert.Hijri(1443, 2, 17).to_gregorian()  #Ghamary  to milady 
           # print(g)
            # 1982-12-02

            #h = convert.Gregorian(2021, 12, 2).to_hijri()  # milady to Ghamary
            #print(h)
            # 1403-02-17

            #gregorian_date = jdatetime.date(1399,11,30).togregorian()# Shamsy to Milady
            #jalili_date =  jdatetime.date.fromgregorian(day=19,month=5,year=2017) # Milady to Shamsy
            #a =gregorian_date.strftime("%d-%m-%Y")
            #print(a)

            #jdatetime.set_locale('fa_IR')
            #b= jdatetime.datetime.now().strftime("%d-%m-%Y")
            #print(b)


                          
            answer = {'type': Type_list, 'city': City_list, 'date': Date_list,'time': Time_list,'religious_time': Religious__list, 'calendar_type': Calender_list, 'event': Event__list, 'api_url': Api_list,'result': Result_list}
        return answer


    def AIBOT_Modified(self, Address):
        answer = {'type': '0', 'city': [], 'date': [],
                  'time': [], 'religous_time': [], 'calendar_type': [], 'event': [], 'api_url': '', 'result': ''}

        
        return answer
