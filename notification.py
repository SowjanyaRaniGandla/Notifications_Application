import time 
import os 

# the format: "MonthDay  
  
NotificationFile = '/home/dell/Desktop/python project/notify.txt'
  
def checkNotifications(): 
    fileName = open(NotificationFile, 'r') 
    today = time.strftime('%m%d') 
    flag = 0
    for line in fileName: 
        if today in line: 
            line = line.split(' ') 
            flag =1
            os.system('notify-send "Notifications for Today: ' + line[1] + ' ' + line[2] + ' ' + line[3] + '"') 
    if flag == 0: 
            os.system('notify-send "No Notifications for Today!"') 

checkNotifications() 
    
    
    
    
    
    
    
