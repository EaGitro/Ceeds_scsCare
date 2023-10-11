import datetime
import random


#class VitalData:
#    def __init__(self):
#        self.date = datetime
#        self.HeartRate = 0
#        self.AverageSleepTime = 0.0
#        self.OxygenPercent = 0

date = datetime.datetime.now()

print("正常値？(y/n)")    
PulseRate_Ans = input('Pulse Rate:')
AverageSleeptime_Ans = input('Average Sleep Time:')
OxygenPercent_Ans = input('Blood Oxygen Concentration:')

def value_p(Ans):
    if Ans == 'y':
        return (random.randint(60,100))
    
    else :
        return (random.randint(101,120))

def value_s(Ans):
    if Ans == 'y':
        return (random.randint(6,8))
    
    else :
        return (random.randint(0,5))

def value_o(Ans):
    if Ans == 'y':
        return (random.randint(97,99))
    
    else :
        return (random.randint(93,96))

AverageSleeptime_hour = value_s(AverageSleeptime_Ans)
AverageSleeptime_minute = random.randint(0,59) 

for i in range(20):
    minutes_ago = datetime.timedelta(minutes=20-i)

    print(date-minutes_ago," |  Pulse Rate:", value_p(PulseRate_Ans)," |  Average Sleep Time:", AverageSleeptime_hour,"h",AverageSleeptime_minute,"m"," |  Blood Oxygen Concentration:", value_o(OxygenPercent_Ans),sep = '')



print("\nPulse Rate| 正常値 60~100[bpm]")
print("Average Sleep Time| 正常値 6~[時間]")
print("Blood Oxygen Concentration| 正常値 97~[%]\n")
