import datetime
import json

#---------------もらう引数----------------------------

#list_allは今日行うべきTo Doの個数 一応20個にしてある
#list_all = 20

#list _nowは今現在のTo Do実績　一応12個にしてある
#list_now = 12

#-----------------------------------------------------

class todo:
    def __init__(self):
        self.date = datetime.datetime.now().isoformat()
        self.YourAchieve = self.list_prob()
        self.IdealAchieve = self.list_ideal()
        self.LevelAchieve = self.list_level()
        self.TF = self.list_TF()


    def list_prob(self):
        list_now = 12 #todo実績
        list_all = 20 #todo全体
        listprob = (list_now/list_all)*100
        return listprob

    def list_ideal(self):
        dt_now = datetime.datetime.now()
        hour = dt_now.hour
        minute = dt_now.minute 

        if hour <= 8:
            prob =0
        
        if ((9<=hour) and (hour<12)):
            prob = ((hour-9) * 60 + minute) / 450
    
        if 12 == hour:
            prob = 180/450

        if ((13<=hour) and (hour<=16)) :

            prob = ((hour-10) * 60 + minute) / 450

        if hour == 17 :
            if (0<=minute) and (minute<=30):
                prob = ((hour-10) * 60 + minute) / 450
            else :
                prob = 1
        
        if hour>=18:
            prob = 1

        listideal = prob*100

        return listideal
    
    def list_level(self):
        dt_now = datetime.datetime.now()
        hour = dt_now.hour
        minute = dt_now.minute
        list_now = 12 #todo実績
        list_all = 20 #todo全体

        listprob = (list_now/list_all)*100

        if hour <= 8:
            prob =0
        if ((9<=hour) and (hour<12)):
            prob = ((hour-9) * 60 + minute) / 450
    
        if hour == 12:
            prob = 180/450

        if ((13<=hour) and (hour<=16)) :

            prob = ((hour-10) * 60 + minute) / 450

        if hour == 17 :
            if (0<=minute) and (minute<=30):
                prob = ((hour-10) * 60 + minute) / 450
            else :
                prob = 1
        
        if hour >= 18:
            prob = 1

        listideal = prob*100


        return (listprob/listideal)*100
    
    def list_TF(self):

        dt_now = datetime.datetime.now()
        hour = dt_now.hour
        minute = dt_now.minute
        list_now = 12 #todo実績
        list_all = 20 #todo全体

        listprob = (list_now/list_all)*100

        if hour <= 8:
            prob =0
        if ((9<=hour) and (hour<12)):
            prob = ((hour-9) * 60 + minute) / 450
    
        if hour == 12:
            prob = 180/450

        if ((13<=hour) and (hour<=16)) :

            prob = ((hour-10) * 60 + minute) / 450

        if hour == 17 :
            if (0<=minute) and (minute<=30):
                prob = ((hour-10) * 60 + minute) / 450
            else :
                prob = 1
        
        if hour >= 18:
            prob = 1

        listideal = prob*100


        if ((listprob/listideal) >= 0.7 ):
            return bool(1)
        
        if ((listprob/listideal) < 0.7 ):
            return bool(0)
    


#---------------------------------返り値------------------------------------

#現在時間
#dt_now

#現在のtodo消化率[%]
#todo_now = list_prob(list_all,list_now)

#現在の理想消化率[%]
#todo_ideal = list_ideal(dt_hour,dt_minute)

#----------------------------------------------------------------------------------

#print("現在時間: ", dt_now)
#print("あなたのToDo消化率: ", todo_now,"%", sep='')
#print("理想消化率: ", todo_ideal,"%", sep='')

    def update_prob(self):
        self.YourAchieve = self.list_prob()
        self.IdealAchieve = self.list_ideal()
        self.LevelAchieve = self.list_level()
        self.TF = self.list_TF()

    def make_json(self):
        d = {
            'date':self.date,
            'YourAchievementRate':self.YourAchieve,
            'IdealAchievementRate':self.IdealAchieve,
            'LevelofAchievement':self.LevelAchieve,
            'TrueorFalse':self.TF
        }
        todoprob = json.dumps(d)
        return todoprob

if __name__ == "__main__":
    prob = todo()
    print(prob.make_json())
    prob.update_prob()
    print(prob.make_json())