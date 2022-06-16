#https://pypi.org/project/persiantools/

import jdatetime
jdatetime.datetime.now()
jdatetime.datetime(1394, 12, 4, 8, 37, 31, 855729)
jdatetime.date.today()
jdatetime.date(1394, 12, 4)


from hijri_converter import convert

g = convert.Hijri.to_gregorian() # hejry(Ghamary) to milady
print(g)
print(g.strftime("%A"))
# 1982-12-02

#h = convert.Gregorian(1982, 12, 2).to_hijri() #hejry to milady
#print(h)
# 1403-02-17


from persiantools.jdatetime import JalaliDate  #Shamsy today Shamsy = jalaly
import datetime
JALALI = JalaliDate.today()
print(JALALI)
print(JALALI.strftime("%A"))
#>>>>>
#https://strftime.org/
#EX:strftime("%A")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import calendar

c = calendar.TextCalendar(calendar.SUNDAY) #
str =c.formatmonth(2025,1)
print(str)



#...............................
numbers = [1,2,3,4,5,6,7]

evens = [x for x in numbers if x % 2 is 0]

odds = [y for y in numbers if y not in evens]



 from persiantools.jdatetime import JalaliDate, JalaliDateTime
>>> import pytz

>>> JalaliDate(1367, 2, 14).isoformat()
'1367-02-14'

>>> JalaliDate(1395, 3, 1).strftime("%Y/%m/%d")
'1395/03/01'

>>> JalaliDateTime(1369, 7, 1, 14, 0, 10, 0, pytz.utc).strftime("%c")
'Yekshanbeh 01 Mehr 1369 14:00:10'

>>> JalaliDateTime.now(pytz.utc).strftime("%I:%M:%S.%f %p %z %Z")
'01:49:22.518523 PM +0000 UTC'



>>> JalaliDateTime.to_jalali(datetime.datetime(1988, 5, 4, 14, 0, 0, 0))    # Gregorian to Jalali
JalaliDateTime(1367, 2, 14, 14, 0)

>>> JalaliDateTime.fromtimestamp(578723400, pytz.timezone("Asia/Tehran"))   # Timestamp to Jalali
JalaliDateTime(1367, 2, 14, 8, 0, tzinfo=<DstTzInfo 'Asia/Tehran' +0330+3:30:00 STD


JalaliDateTime(1395, 4, 18, 1, 43, 24, 720505)               
