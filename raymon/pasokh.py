
#pip install textdistance

import textdistance
import math
import statistics 
#Example
#textdistance.hamming('text', 'test')

#textdistance.hamming.normalized_similarity('text', 'test')

#textdistance.hamming('arrow', 'arow')


#textdistance.hamming.normalized_similarity(A[1], 'نگین')


import re
#answer = {'type': ['-1'], 'city': [], 'date': [],'time': [],'religious_time': [], 'calendar_type': [], 'event': [], 'api_url': [],'result': ['']}
#answer = {'type': Type_list, 'city': City_list, 'date': Date_list,'time': Time_list,'religious_time': Religious__list, 'calendar_type': Calender_list, 'event': Event__list, 'api_url': Api_list,'result': Result_list}
answer = {'type': ['4'], 'city': [], 'date': ['1400-01-12'],'time': [],'religious_time': [],'calendar_type': [], 'event': [], 'api_url': [],'result': ['1400-01-12']}

tempature = ['10','14']
result = '12'
#.....................Weather
type = 1
Question = 'دمای هوای تهران امروز چقدر است'
Question_weather=['دمای هوای تهران امروز چقدر است؟',#1
                  'دمای هوای فردای شیراز ساعت ۱۴:۲۵ چقدر است؟','دمای هوا در زمان اذان صبح امروز تهران چقدر است؟',#1
                  'دمای هوای دو روز بعد گرگان چند درجه سانتیگراد است؟', 'درجه دمای هوای ۳ روز دیگر رم ساعت ۱۶:۱۰ چند درجه است؟',
                  'گرمی هوای فردای تهران ساعت ۱۹:۱ چقدر است؟ ','درجه حرارت هوای دو روز بعد پکن ساعت ۲۰:۱۰ به چه میزان است؟',#1
                  'میانگین دمای هوای تهران امروز چقدر است؟', 'میانگین اندازه گرمی یا سردی هوای دو روز بعد کاشان چند درجه است؟',#2
                  'امروز حداقل دمای هوای مشهد سردتر است یا تهران؟',#3
                  'اذان صبح تهران سردتر است یا اذان ظهر آن؟']#4

City_list = ['شيراز','تهران']
my_answer = []
Result_list =[]
B = ['دمای هوای تهران امروز چقدر است']#['اندازه گرمی یا سردی هوای دو روز بعد باکو ساعت ۱۸:۱۰ چند درجه سانتیگراد است؟']
A =['چقدر است ؟','چطور است ؟']
textdistance.hamming.normalized_similarity(B[0], Question[0])
if type == 1:   
   f = re.findall("\چقدر است ؟", Question)
   if f!=[]:
    if f[0] in Question:
       s = Question.replace('چقدر است ؟','')
       My_answer = s + result+'درجه سلسيوس است'   
   else:
      My_answer = Question + result+'درجه سلسيوس است'   #.....similarity
#.......................Time
Question_Time = [['اذان صبح امروز تهران چه ساعتی است؟ ', '2'],['اذان ظهر هفته ی قبل شیراز چه ساعتی بود؟', '2'],['ساعت اذان ظهر بیروت؟ ', '2'], ['اذان ظهر فردای تورنتو چه زمانی است؟', '2']]
a = textdistance.hamming.normalized_similarity('امروز', Question_Time)

#type=3
resualt_weather =[]
for g in range(len(Question_weather)):
    m = textdistance.hamming.normalized_similarity(Question,Question_weather[g] )
    r = (m)    
    resualt_weather = resualt_weather +[r]
print(resualt_weather)
max_r = max(resualt_weather)
print(max_r)
s = resualt_weather.index(max_r)
if s in range(0,7):#1   
   for c in len(City_list):   #resualt_tempature_city_1!!!!!resualt_weather
      My_answer = 'دمای' +' '+ City_list[c]+' ' + resualt_tempature_all[c]+'درجه سلسيوس است'+'.' + 'هوا در اين زمان'+ resualt_weather[c]+'است'   
      resualt_weather = resualt_weather + [My_answer]

if s in range(7,8):  #2 mean
   for c in len(City_list):   #resualt_tempature_city_1!!!!!resualt_weather
      Result_list = Result_list + statistics.mean(All_Time_temture) 
      My_answer = 'ميانگين دمای' +' '+ City_list[c]+' ' + resualt_tempature_all+'درجه سلسيوس است'+'.'
      resualt_weather = resualt_weather + [My_answer]
     
      
     # if len(City_list)>2:              
#...................................................#          اختلاف تفاوت....All_Time_temture
if s in range(7,7):#3 1 cities
   if word_token2[0] == 'کمینه' or 'کمترین'  or 'حداقل':  #sardtarin-garmtarin
        min_city = min(tempature_city_1)                        
        Result_list = Result_list + [City_list[0]]
            
   if word_token2[0] == 'حداکثر' or 'بيشترين'  or 'بيشينه':  #sardtarin-garmtarin
        min_city = min(tempature_city_1)                        
        Result_list = Result_list + [City_list[0]]                            

     
if s in range(7,7):#3 1 cities
   if word_token2[0] == 'کمینه' or 'کمترین'  or 'حداقل':  #sardtarin-garmtarin
        min_city1 = min(tempature_city_1)
        min_city2 = min(tempature_city_2)       
        min_minimom_tempature = min(min_city1,min_city2)
        if min_minimom_tempature == min_city1:
            Result_list = Result_list + [City_list[0]]
        else:
            Result_list = Result_list + [City_list[1]]
            
   if word_token2[0] == 'حداکثر' or 'بيشترين'  or 'بيشينه':  
        max_city1 = max(tempature_city_1)
        max_city2 = max(tempature_city_2)       
        min_minimom_tempature = max(max_city1,max_city2)
        if min_minimom_tempature == min_city1:
            Result_list = Result_list + [City_list[0]]
#......................................................................            
if s in range(7,7):#3 cities
   if word_token2[0] == 'اختلاف' or 'تفاوت'  or 'حداقل': #true
        Ekhtelaf =tempature_city_1 -tempature_city_2       
        Result_list = Result_list + Ekhtelaf
                        
if s in range(7,7):#3 cities
   if word_token2[0] == 'اختلاف' or 'تفاوت'  or 'حداقل':  
        min_city1 = min(tempature_city_1)
        min_city2 = min(tempature_city_2)       
        min_minimom_tempature = min(min_city1,min_city2)
        if min_minimom_tempature == min_city1:
            Result_list = Result_list + [City_list[0]]

if s in range(7,7):#3 cities
   if word_token2[0] == 'اختلاف' or 'تفاوت'  or 'حداقل':  
        min_city1 = min(tempature_city_1)
        min_city2 = min(tempature_city_2)       
        min_minimom_tempature = min(min_city1,min_city2)
        if min_minimom_tempature == min_city1:
            Result_list = Result_list + [City_list[0]]
#.......................................................................                                                
if s in range(7,7):#4
#if time!=[]:
   time =int(time[0:2]+time[3:5])
   for i in range(len(All_Time_day)):
        time1= All_Time_day[i]
        time1_int =int(time1[0:2]+time1[3:5]) 
        if i<len(All_Time_day)-1:
           time2 =All_Time_day[i+1]
           time2_int =int(time2[0:2]+time2[3:5])
           if time<time2_int and time>time1_int:
              near1 = time-time1_int
              near2 = time2_int-time
              if near1<near2:
                  time_true = time1
              else:
                  time_true = time2


#...................>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>2
resualt_RE =[]
Question_Re = ['اذان صبح امروز تهران چه ساعتی است؟ ','اذان ظهر فردای تهران چه ساعتی است؟ ', #1
      'اذان ظهر دیروز تهران چه ساعتی بود؟', 'اذان مغرب دیروز قم چه ساعتی بود؟', 
      'اذان ظهر پس فردای تهران چه ساعتی است؟','نیمه شب شرعی تهران چه ساعتی است؟ ',
      'اذان صبح مسکو چه ساعتی است؟ ','طلوع آفتاب مسکو چه ساعتی است؟', 
      'غروب آفتاب مشهد چه ساعتی است؟ ','غروب آفتاب کابل چه ساعتی است؟', 
      'اذان مغرب پریروز قم چه ساعتی بود؟ ', 'اذان ظهر ۴ روز پیش قم چه ساعتی بود؟',#2 
      'اذان ظهر هفته ی قبل شیراز چه ساعتی بود؟',
      'اذان ظهر هفته ی بعد شیراز چه ساعتی است؟ ', 
      'اذان صبح امروز دوحه چه ساعتی است؟ ','اذان ظهر امروز بغداد چه ساعتی است؟ ', 
      'اذان ظهر امروز تهران چه زمانی است؟',
      'ساعت اذان ظهر بیروت؟ ', #3
      'اذان ظهر بیروت چه زمانی است؟ ', 'اذان ظهر فردای تورنتو چه زمانی است؟']#1
Question = ['اذان ظهر فردای تورنتو چه زمانی است؟']
if type == 2:   
    for g in range(len(Question_Re)):
        r = textdistance.hamming.normalized_similarity(Question,Question_Re[g] )
    
        resualt_RE = resualt_RE +[r]
    print(resualt_RE)
    max_r = max(Question_Re)
    print(max_r)
    s = resualt_RE.index(max_r)

for c in len(City_list):   #resualt_tempature_city_1!!!!!resualt_weather
   if s in range(0,7):#1 ,2 ,3         
      if "چه ساعتی است؟" or "چه ساعتی بود؟ " or"چه زمانی است؟" in Question:
         s = Question.replace("چه ساعتی است؟","چه زمانی است؟")
         My_answer = s + ' '+'در ساعت'+' '+result+'می باشد'
      if "چه ساعتی بود؟ " or "چه زمانی است؟" in Question:
         s = Question.replace("چه ساعتی بود؟ ","چه زمانی است؟")
         My_answer = s + ' '+'در ساعت'+' '+result+'بوده است'   
   
      else:
         s = Question.replace("؟")
         My_answer = s + ' '+'در ساعت'+' '+result+'می باشد'
        
                 
  
#.......................Time

Question_Time=['ساعت در تهران چند است؟', 
     'در نیویورک چه زمانی از روز است؟',
     'ساعت به وقت ابوظبی چند است؟ ', 
     
     'الان به وقت تهران چه زمانی از روز است؟ ', 
     'الان در سنگاپور چه ساعتی در شبانه روز است؟', 
     
     'الان در استکهلم ساعت دقیقا چند است؟', 
     
     'در این لحظه ساعت مسکو چند است؟', 
     'ساعت به وقت بیروت چند است؟', 
     'در تاشکند، این لحظه چه زمانی از روز است؟', 
     'ساعت اسلام آباد چند است؟ ', 
     'ساعت به طور دقیق در استانبول چند است؟', 
     
     'ساعت فعلی در تورنتو؟', 
     
     'در کابل چه زمانی از روز است؟ ', 
     'ساعت فعلی ونکوور چند است؟', 
     'ساعت در شهر زوریخ چند است؟', 
     'ساعت دبی در این لحظه چند است؟', 
     'ساعت در لس آنجلس چند است؟', 
     'اکنون در ریاض چه زمانی از روز است؟', 
     'ساعت کنونی آمستردام چند است؟', 
     'اکنون در شهر باکو ساعت چند است؟', 
     'ساعت در پایتخت ایران چند است؟', 
     
     'در پایتخت روسیه چه زمانی از روز است؟', 
     
     'ساعت به وقت پایتخت آذربایجان چند است؟', 
     
     'الان به وقت پایتخت ازبکستان چه زمانی از روز است؟', 
     
     'الان در پایتخت انگلستان چه ساعتی در شبانه روز است؟']

         
Question = ['ساعت در پایتخت ایران چند است؟']
if type == 2:   
    #for g in range(len(Question_Re)):
    #m = textdistance.hamming.normalized_similarity(Question,Question_Re[g] )
    #r = (m)    
    #resualt_RE = resualt_RE +[r]
#print(resualt_RE)
#max_r = max(Question_Re)
#print(max_r)
#s = resualt_RE.index(max_r)

   for c in len(City_list):   #resualt_tempature_city_1!!!!!resualt_weather
   #if s in range(0,7):#1 ,2 ,3         
         My_answer = ' ساعت'+' '+result+'می باشد'
Question_T=['روز حافظ در سال ۹۹ چه روزی است؟', 
    
    'روز حافظ در سال ۱۳۹۶ چه روزی است؟', 
    'امسال سالروز شهادت سردار حاج قاسم سلیمانی چه روزی است؟', 
    'شهادت حضرت فاطمه زهرا سلام االله علیها چه روزی است؟', 
    'مناسبت روز ۱۸ اسفند امسال چیست؟ ', 
    'مناسبت ۱۸ اسفند سال بعد چیست؟', 
    'کدام روز از سال ۱۴۰۳ روز اصناف است؟', 
    
    'در سال ۹۷ روز جهانی محیط زیست چه روزی است؟', 
    
    'بهمن امسال به میلادی؟ ۲۲', 
    
    'سالروز زمین لرزه ی بم در سال ۹۹کدام روز است؟', 
    
    'امسال جشن سده در کدام روز است؟', 
    'سال شمسی امسال چند روز است؟', 
    'تاریخ شمسی امروز؟', 
    'تاریخ میلادی امروز؟', 
    
    'تعداد روزهای اسفند ۱۴۰۰؟', 
    
    'روز جهانی بهداشت در سال ۹۹کدام روز از سال است؟', 
    'سالگرد درگذشت پروین اعتصامی در سال ۱۳۹۶ کدام روز است؟', 
    
    'روز دندانپزشک در سال ۱۳۹۶؟', 
    'روز جمهوری اسلامی در سال ۱۴۰۰؟', 
    'کدام روز از سال ۱۴۰۰ روز قلم است؟', 
    'سالگرد اعلام پذیرش قطعنامه ۵۹۸ شورای امنیت از سوی ایران در کدام روز ۱۴۰۰ اتفاق افتاده است؟', 
    'تاریخ روز صنعت و معدن امسال چه روزی است؟ ', 
    'در این سال روز عرفه چه روزی بود؟', 
    'تاریخ برگزاری اولین کنکور در ایران؟ ', 
    'روز خبرنگار کدام روز از امسال است؟', 
    'عید سعید غدیر خم کدام روز امسال است؟', 
    'تاریخ ولادت امام موسی کاظم علیه السلام در سال ۹۹؟', 
    'تاریخ روز جهانی چپ دست ها در سال ۹۹؟', 
    'روز بزرگداشت ابوعلی سینا و روز پزشک در کدام روز سال ۹۹است؟', 
    'روز سینما در سال ۱۳۹۹؟']      
        
for c in len(City_list):   #resualt_tempature_city_1!!!!!resualt_weather
   #if s in range(0,7):#1 ,2 ,3         
         My_answer = 'تاريخ'+' '+date+' '+ 'مصادف با'+' '+ event+ ' '+'می باشد'
