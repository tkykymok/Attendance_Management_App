from django import template
from datetime import datetime, date, time, timedelta
from time import localtime, mktime
register = template.Library() 

@register.filter
def in_group(user, team_name):
    if user.groups.filter(name=team_name).exists():
        return True
    else:
        return False
    

@register.filter(name="subtraction_h")
def subtraction_h(value, args):
    d = datetime(2020, 1, 1).date()
    if value != None and args != None:
        return str(int(abs(datetime.combine(d,value) - datetime.combine(d,args)).seconds/60//60))+':'
    else:
        pass

@register.filter(name="subtraction_m")
def subtraction_m(value, args):
    d = datetime(2020, 1, 1).date()
    if value != None and args != None:
        if int(abs(datetime.combine(d,value) - datetime.combine(d,args)).seconds/60%60) == 0:
            return str("00")
        else:
            return str(int(abs(datetime.combine(d,value) - datetime.combine(d,args)).seconds/60%60))
    else:
        pass



    
"""
a = CheckInOut.objects.get(staff=1, date_worked__masterdate=today)
d = a.date_worked
x = a.overtime_s
y = a.overtime_e

>>> a = CheckInOut.objects.get(staff=1, date_worked__masterdate=today)
>>> d = a.date_worked.masterdate
>>> x = a.overtime_s
>>> y = a.overtime_e
>>> 
>>> a
<CheckInOut: 2020-03-20>
>>> d
datetime.date(2020, 3, 20)
>>> x
datetime.time(18, 0)
>>> y
datetime.time(20, 20)

x2 = datetime.combine(d,x)
y2 = datetime.combine(d,y)
r = abs(x2-y2).seconds/60 #秒から分に直す
r1 = r//60  #分から時間に直す
r2 = r%60   #時間を引いた余りの分
"""