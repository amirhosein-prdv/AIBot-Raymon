

import csv

with open('MY_City.csv', "r",encoding='utf16') as file:
     reader = csv.reader(file, delimiter=',')
     country_Eng =[]
     for row in reader:
        country_Eng = country_Eng + [row]
