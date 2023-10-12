import datetime
import numpy as np
import json


class VitalData:
    def __init__(self):
        self.date = datetime.datetime.now().isoformat()
        self.HeartRate = self.value_p()
        self.AverageSleepTime = self.value_s()
        self.OxygenPercent = self.value_o()

    def value_p(self):
        return (np.random.randint(60,120))

    def value_s(self):
        return (np.random.randint(0,8))

    def value_o(self):
        return (np.random.randint(93,99))
    
    def update_vital(self):
        self.HeartRate = self.value_p()
        self.OxygenPercent = self.value_o()

    def make_json(self):
        d = {
            'date':self.date,
            'HeartRate':self.HeartRate,
            'AverageSleepTime':self.AverageSleepTime,
            'OxygenPercent':self.OxygenPercent
        }
        vital_json = json.dumps(d)
        return vital_json
    
if __name__ == "__main__":
    vital = VitalData()
    print(vital.make_json())
    vital.update_vital()
    print(vital.make_json())
