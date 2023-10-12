import datetime
import numpy as np
import json


class VitalData:
    def __init__(self):
        """
        date:日付(str)
        BodyTemperature:体温(float)
        HeartRate:心拍数(int)
        AverageSleepTime:睡眠時間(int,float)
        OxygenPercent:血中酸素濃度(int)
        """
        self.date = datetime.datetime.now().isoformat()
        self.BodyTemperature = self.value_b()
        self.HeartRate = self.value_p()
        self.AverageSleepTime = self.value_s()
        self.OxygenPercent = self.value_o()

        self.bool_BodyTemperature = 0
        self.bool_HeartRate = 0
        self.bool_AverageSleepTime = 0
        self.bool_OxygenPercent = 0
        
        self.is_helth = 0

    def value_b(self):
        #体温初期化、更新
        return (np.round((39 - 35.5) * np.random.rand() + 35,decimals = 1))
    def value_p(self):
        #心拍数初期化、更新
        return (np.random.randint(60,120))

    def value_s(self):
        #睡眠時間初期化
        return (np.round(8 * np.random.rand(),decimals = 2))

    def value_o(self):
        #血中酸素濃度初期化
        return (np.random.randint(93,99))
    
    def update_vital(self):
        #バイタル更新
        self.BodyTemperature = self.value_b()
        self.HeartRate = self.value_p()
        self.OxygenPercent = self.value_o()
    
    def bool_vital(self):
        num_false = 0
        if self.BodyTemperature <= 37.5:
            self.bool_BodyTemperature = True
        else:
            self.bool_BodyTemperature = False 
            num_false = num_false + 1
        if self.HeartRate  <= 100:
            self.bool_HeartRate = True
        else:
            self.bool_HeartRate = False 
            num_false = num_false + 1

        if self.AverageSleepTime  >= 6:
            self.bool_AverageSleepTime = True
        else:
            self.bool_AverageSleepTime = False
            num_false = num_false + 1
        
        if self.OxygenPercent >= 97:
            self.bool_OxygenPercent = True
        else:
            self.bool_OxygenPercent = False
            num_false = num_false + 1
        
        if num_false < 3:
            self.is_helth = True
        
        else:
            self.is_helth = False

        

        
    def make_dictionary(self):
        #辞書作成
        self.bool_vital()
        d = {
            'date':self.date,
            'BodyTemperature':{'value':self.BodyTemperature,'bool':self.bool_BodyTemperature},
            'HeartRate':{'value':self.HeartRate,'bool':self.bool_HeartRate},
            'AverageSleepTime':{'value':self.AverageSleepTime,'bool':self.bool_AverageSleepTime},
            'OxygenPercent':{'value':self.OxygenPercent,'bool':self.bool_OxygenPercent},
            'isHealth':self.is_helth
        }
        return d

    def make_json(self):
        #jsonに変換
        vital_json = json.dumps(self.make_dictionary())
        return vital_json
    
if __name__ == "__main__":
    vital = VitalData()
    print(vital.make_json())
    vital.update_vital()
    print(vital.make_json())
