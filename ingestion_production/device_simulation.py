from typing import List, Callable
import scipy.stats as stats
import datetime
import time
import json 
import ingestion_training.ingest_data_into_s3 as ingest_data_into_s3
#get now time
now = datetime.datetime.now()
class Device:
    def __init__(self, device_id:int):
        self.device_id = device_id
        self.STATUS = 'OFF'
        self.mean = 20
        self.std = 10
        self.BUCKET_NAME = 'amplify-blogfinal-dev-231714-deployment'

    def start(self):
        self.STATUS = 'ON'
        while self.STATUS == 'ON':
            data = {
                "timestamp": "2020-01-01 00:00:00",
                "sensor1": stats.norm.rvs(self.mean, self.std),
                "sensor2": stats.norm.rvs(self.mean, self.std),
                "sensor3": stats.norm.rvs(self.mean, self.std),
                "sensor4": stats.norm.rvs(self.mean, self.std),
                "sensor5": stats.norm.rvs(self.mean, self.std),
                "sensor6": stats.norm.rvs(self.mean, self.std),
                "sensor7": stats.norm.rvs(self.mean, self.std),
                "sensor8": stats.norm.rvs(self.mean, self.std),
                "sensor9": stats.norm.rvs(self.mean, self.std),
                "sensor10": stats.norm.rvs(self.mean, self.std),
                "sensor11": stats.norm.rvs(self.mean, self.std),
                "sensor12": stats.norm.rvs(self.mean, self.std),
                "sensor13": stats.norm.rvs(self.mean, self.std),
                "sensor14": stats.norm.rvs(self.mean, self.std),
                "sensor15": stats.norm.rvs(self.mean, self.std),
                "sensor16": stats.norm.rvs(self.mean, self.std),
                "sensor17": stats.norm.rvs(self.mean, self.std),
                "sensor18": stats.norm.rvs(self.mean, self.std),
                "sensor19": stats.norm.rvs(self.mean, self.std),
                "sensor20": stats.norm.rvs(self.mean, self.std),
                "sensor21": stats.norm.rvs(self.mean, self.std),
                "sensor22": stats.norm.rvs(self.mean, self.std),
                "sensor23": stats.norm.rvs(self.mean, self.std),
                "sensor24": stats.norm.rvs(self.mean, self.std),
                "sensor25": stats.norm.rvs(self.mean, self.std),
                "sensor26": stats.norm.rvs(self.mean, self.std),
                "sensor27": stats.norm.rvs(self.mean, self.std),
                "sensor28": stats.norm.rvs(self.mean, self.std),
                "sensor29": stats.norm.rvs(self.mean, self.std),
                "sensor30": stats.norm.rvs(self.mean, self.std),
                "sensor31": stats.norm.rvs(self.mean, self.std),
                "sensor32": stats.norm.rvs(self.mean, self.std),
                "sensor33": stats.norm.rvs(self.mean, self.std),
                "sensor34": stats.norm.rvs(self.mean, self.std),
                "sensor35": stats.norm.rvs(self.mean, self.std),
                "sensor36": stats.norm.rvs(self.mean, self.std),
                "sensor37": stats.norm.rvs(self.mean, self.std),
                "sensor38": stats.norm.rvs(self.mean, self.std),
                "sensor39": stats.norm.rvs(self.mean, self.std),
                "sensor40": stats.norm.rvs(self.mean, self.std),
                "sensor41": stats.norm.rvs(self.mean, self.std),
                "sensor42": stats.norm.rvs(self.mean, self.std),
                "sensor43": stats.norm.rvs(self.mean, self.std),
                "sensor44": stats.norm.rvs(self.mean, self.std),
                "sensor45": stats.norm.rvs(self.mean, self.std),
                "sensor46": stats.norm.rvs(self.mean, self.std),
                "sensor47": stats.norm.rvs(self.mean, self.std),
                "sensor48": stats.norm.rvs(self.mean, self.std),
                "sensor49": stats.norm.rvs(self.mean, self.std),
                "sensor50": stats.norm.rvs(self.mean, self.std),
                "sensor51": stats.norm.rvs(self.mean, self.std),
                "sensor52": stats.norm.rvs(self.mean, self.std),
                "sensor53": stats.norm.rvs(self.mean, self.std),
                "sensor54": stats.norm.rvs(self.mean, self.std),
                "sensor55": stats.norm.rvs(self.mean, self.std),
                "sensor56": stats.norm.rvs(self.mean, self.std),
                "sensor57": stats.norm.rvs(self.mean, self.std),
                "sensor58": stats.norm.rvs(self.mean, self.std),
                "sensor59": stats.norm.rvs(self.mean, self.std),
                "sensor60": stats.norm.rvs(self.mean, self.std),
                "sensor61": stats.norm.rvs(self.mean, self.std),
            }
            with open(f"data_{self.device_id}_{now}.json", "a") as f:
                json.dump(data, f)
            file_name = f"data_{self.device_id}_{now}.json"
            ingest_data_into_s3.upload_file_to_s3(file_name, self.BUCKET_NAME, object_name=None) 
            time.sleep(60)
        def stop(self):
            self.STATUS = 'OFF'
        
        
#create 5 devices
for i in range(5):
    device = Device(i)
    device.run()

                

