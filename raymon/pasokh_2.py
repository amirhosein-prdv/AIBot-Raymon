
import textdistance
import math
import statistics 
#Example
#textdistance.hamming('text', 'test')

#textdistance.hamming.normalized_similarity('text', 'test')

#textdistance.hamming('arrow', 'arow')


#textdistance.hamming.normalized_similarity(A[1], 'نگین')
Question = 'هوای فردای شیراز ساعت ۱۴ و ۲۵ دقیقه چقدر است'
resualt_RE=[]
Type_list =[]
MY_Data_test=['دمای هوای تهران امروز چقدر است؟',#1
                  'دمای هوای فردای شیراز ساعت ۱۴:۲۵ چقدر است؟','دمای هوا در زمان اذان صبح امروز تهران چقدر است؟',#1
                  'دمای هوای دو روز بعد گرگان چند درجه سانتیگراد است؟', 'درجه دمای هوای ۳ روز دیگر رم ساعت ۱۶:۱۰ چند درجه است؟',
                  'گرمی هوای فردای تهران ساعت ۱۹:۱ چقدر است؟ ','درجه حرارت هوای دو روز بعد پکن ساعت ۲۰:۱۰ به چه میزان است؟',#1
                  'میانگین دمای هوای تهران امروز چقدر است؟', 'میانگین اندازه گرمی یا سردی هوای دو روز بعد کاشان چند درجه است؟',#2
                  'امروز حداقل دمای هوای مشهد سردتر است یا تهران؟',#3
                  'اذان صبح تهران سردتر است یا اذان ظهر آن؟']#4
import re
for g in range(len(MY_Data_test)):
    r = textdistance.hamming.normalized_similarity(Question,MY_Data_test[g] )            
    resualt_RE = resualt_RE +[r]
    print(resualt_RE)
               
    max_r = max(resualt_RE)
    print(max_r)
    Max_all_similarity_index = resualt_RE.index(max_r)    # Max_all_similarity is sentence index %number 

    if max_r<0.5:     # bayad barresy beshe??????!!!!!!!!!!!!!!!!!!!!!!!
       Type_list = Type_list + ['-1']
       My_answer = 'سوال شما فراتر از دانش من مي باشد . اطلاعات من در زمينه اعلام دما ، اعلام اوقات شرعي ، اعلام ساعت در تمام نقاط جهان و مناسبت مرتبط با تاريخ مي باشد. لطفا سوال ديگري بپرسيد. تشکر از شما'
       
