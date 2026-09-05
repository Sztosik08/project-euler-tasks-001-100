import math

def day_of_month(day_month, month, year):
    day_week = (day_month + math.floor((13*(month+1))/5) + year%100 + math.floor(year%100/4) + math.floor(math.floor(year/100)/4)  - 2 * math.floor(year/100)) % 7
    return day_week


months_19 = [3 , 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
counter_19 = 0

if day_of_month(1, 13, 1900) == 1:
    counter_19 +=1
if day_of_month(1, 14, 1900) == 1:
    counter_19 +=1

for year in range(1901, 2001):
    for month in months_19:
        if day_of_month(1, month, year) == 1:
            counter_19 +=1
   
if day_of_month(1, 13, 2001) == 1:
    counter_19 -=1
if day_of_month(1, 14, 2001) == 1:
    counter_19 -=1
         
print(counter_19)
