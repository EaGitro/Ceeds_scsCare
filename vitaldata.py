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
    def value_b(self):
        #体温初期化、更新
        return (np.round((39 - 35.5) * np.random.rand() + 35,decimals = 1))
    def value_p(self):
        #心拍数初期化、更新
        return (np.random.randint(60,120))

    def value_s(self):
        #睡眠時間初期化
        return (np.random.randint(0,8))

    def value_o(self):
        #血中酸素濃度初期化
        return (np.random.randint(93,99))
    
    def update_vital(self):
        #バイタル更新
        self.BodyTemperature = self.value_b()
        self.HeartRate = self.value_p()
        self.OxygenPercent = self.value_o()
    
    def make_dictionary(self):
        #辞書作成
        d = {
            'date':self.date,
            'BodyTemperature':self.BodyTemperature,
            'HeartRate':self.HeartRate,
            'AverageSleepTime':self.AverageSleepTime,
            'OxygenPercent':self.OxygenPercent
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
