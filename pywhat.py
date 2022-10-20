import pywhatkit  # pip install pywhatkit
import datetime
import keyboard as k  #pip install keyboard
import time

print("Started")

#You can also create a CSV file then convert to dataframe then to list
# Use +91 (Country code)  
numbers = ["+91xxxx25xxx","+91x0xxx24xx","+91x2xx24xxx","+918xxxx25xxx","+910xxxx25xxx41","+919xx304xx07"]

#Now loop through each Numbers(contacts), it will open new tab for every Contact, dont worry IF you have time just close them 
for i in range(len(numbers)):
	pywhatkit.sendwhatmsg(numbers[i],
	'''
	Hai i have been working around this Thing
	to send message to multiple contacts. Looping done all.
	Beware of contacts and tabs , each contact will create 
	each tab. 2 contacs = 2 tabs of Web Browser
	https://github.com/niranjandasMM/WhatsupAutomation
	''', 
	datetime.datetime.now().hour,datetime.datetime.now().minute+1, 32) # Dont mess with the time format, 32seconds is the timing for delivering you message after opeing whatsup web
	k.press_and_release('enter')

	# Dont mess with the time format, 32seconds is the timing for delivering you message after opeing whatsup web
	
	print(f"{i} message is sent, {i-len(numbers)} left to send...")

print("Whole Job Done..")