
#pip install -U hijri-converter

from hijri_converter import convert
import jdatetime

g = convert.Hijri(1443, 2, 17).to_gregorian()  #Ghamary  to milady
print(g)
# 1982-12-02

h = convert.Gregorian(2021, 12, 2).to_hijri()  # milady to Ghamary
print(h)
# 1403-02-17



gregorian_date = jdatetime.date(1399,11,30).togregorian()# Shamsy to Milady
jalili_date =  jdatetime.date.fromgregorian(day=19,month=5,year=2017) # Milady to Shamsy
a =gregorian_date.strftime("%d-%m-%Y")
print(a)



jdatetime.set_locale('fa_IR')
b= jdatetime.datetime.now().strftime("%d-%m-%Y")
print(b)

