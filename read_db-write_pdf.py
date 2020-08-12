from datetime import datetime
from fpdf import FPDF
import pymongo
import json
class read_file():
    def __init__(self):
        self.client=pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.rv38o.mongodb.net/temp-humidity-datas?retryWrites=true&w=majority")
        self.db=self.client["temp-humidity-datas"]
        self.col=self.db["datas"]
    def read_datas(self):
        temp_datas=[]
        humidity_datas=[]
        x=[]
        if self.col.count_documents({})>=24:
            data=self.col.find({},{"_id":0,"temperature":1,"humidity":1,'measurement time':1})
            for i in data:
                humidity_datas.append(float(i["humidity"].strip("%")))
                temp_datas.append(float(i["temperature"].strip("C")))
                x.append(json.dumps(i))
            self.temp_average=str(sum(temp_datas)/len(temp_datas))+" C"
            self.humid_average="%"+str(sum(humidity_datas)/len(humidity_datas))
            x=[i.strip("{}") for i in x]
            x=[i.replace('"','') for i in x]
            pdf=FPDF()
            pdf.add_page()
            pdf.set_font("Arial",size=10)
            pdf.cell(200,10,txt="average temperature of the day :"+self.temp_average,ln=1,align="C")
            pdf.cell(200,10,txt="average humidity of the day :"+self.humid_average,ln=1,align="C")
            for i in x:
                pdf.cell(200,10,txt=i,ln=1,align="C")
            pdf.output("resultsss.pdf")
            self.col.remove({})
	else:
		raise Exception("error occured while reading sensor during the day")
