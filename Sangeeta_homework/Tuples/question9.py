'''
You have a tuple of daily temperatures temps = (30, 32, 29, 35, 31). Find the highest temperature
and the day number (1-based) it occurred on.
'''

temps = (30, 32, 29, 35, 31)
highest_temp = max(temps)
print(highest_temp)
day = temps.index(highest_temp) + 1
print(day)