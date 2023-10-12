import datetime
import random

#---------------もらう引数----------------------------

#list_allは今日行うべきTo Doの個数 一応20個にしてある
list_all = 20

#list _nowは今現在のTo Do実績　一応12個にしてある
list_now = 12

#-----------------------------------------------------


dt_now = datetime.datetime.now()
dt_hour = dt_now.hour
dt_minute = dt_now.minute

def list_prob(a,b):
    return (b/a)*100

def list_ideal(hour,minute):
    if ((9<=hour) and (hour<12)) or ((13<hour) and (hour<=16)) :
        prob = ((hour-9) * 60 + minute) / 450
    
    if (12<=hour) and (hour<=13):
        prob = 180/450

    if hour == 17 :
        if (0<=minute) and (minute<=30):
            prob = prob = ((hour-9) * 6 + minute) / 450
        else :
            prob = 1
    
    return prob*100


#---------------------------------返り値にします------------------------------------

#現在時間(date型)（演算する場合はint変換してね）
dt_now

#現在のtodo消化率[%](int型)
todo_now = list_prob(list_all,list_now)

#現在の理想消化率[%](int型)
todo_ideal = list_ideal(dt_hour,dt_minute)

#----------------------------------------------------------------------------------

print("現在時間: ", dt_now)
print("あなたのToDo消化率: ", todo_now,"%", sep='')
print("理想消化率: ", todo_ideal,"%", sep='')

