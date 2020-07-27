from datetime import datetime
from fpdf import FPDF
class read_file():
    def __init__(self):
        pass
    def read_datas(self):
        temp_datas=[]
        humidity_datas=[]
        with open("sensor_datas.txt", "r") as file:
            x=file.readlines()
            x =[i.strip("\n") for i in x]
            x.reverse()
            if len(x)<24:
                raise Exception("--not enough data was received from the sensor to calculate average for today--")
        count=0
        for i in x:
            temp_datas.append(float(i[41:45]))
            count+=1
            if count==24:
                break
        count=0
        for i in x:
            humidity_datas.append(float(i[61:66]))
            count+=1
            if count==24:
                break

        self.temp_average=str(sum(temp_datas)/len(temp_datas))+" C"
        self.humid_average="%"+str(sum(humidity_datas)/len(humidity_datas))
        pdf=FPDF()
        pdf.add_page()
        pdf.set_font("Arial",size=10)
        f=open("sensor_datas.txt","r")
	#the fallowing commands are used to txt to pdf
        pdf.cell(200,10,txt="average temperature of the day :"+self.temp_average,ln=1,align="C")
        pdf.cell(200,10,txt="average temperature of the day :"+self.humid_average,ln=1,align="C")
        for i in f:
                pdf.cell(200,10,txt=i,ln=1,align="C")
        pdf.output("result.pdf")
