to send mail as pdf-- just fill send_mail.py(mail address and password)
to send mail as text-- just fill send_mail_text.py
to push your sensor datas to mongodb run mongo.py(this also read sensor)-- to read datas from db run read_db-write_pdf.py

cron schedule:
open the terminal and type crontab -e	
0 * * * * python /path/to/read_sensor.py
5 0 * * * python /path/to/send_mail.py or send_mail_text.py

program create txt and pdf file in the current location(end of the day). u can check the datas(read by DHT11) as u wish 
if some issue occur while reading sensor every hour, the program raise the exception at end of the day-u can check the sensor or connection
