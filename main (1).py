#write a program that determines whether a year entered by the user is a leap year or not using if elif else statents 
def isLeapYear(year): 
  if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True 
  else:
    return False 
year = 2019
if isLeapYear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))
