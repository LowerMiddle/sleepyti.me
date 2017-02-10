#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import time
import datetime

R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
O = '\033[33m'

def cls():
  os.system('cls' if os.name=='nt' else 'clear')
  
def inputNumber(message):
  while True:
    try:
      userInput=int(input(message))
    except:
	error()
    else:
      return userInput
      break
 
def error():
  error2=raw_input(R + "Wrong choice. Press Enter and try again!")
  main2()
 
def end():
  question = raw_input(C + "Do you want to go back to the main menu?: Yes/No \n") 
  if question == "Yes": 
     cls()
     main2() 
  elif question == "No": 
     sys.exit()
  else:
     end()
  
def main():
  cls()
  print C + "      _                       _   _                  "
  time.sleep(0.3)
  print C + "  ___| | ___  ___ _ __  _   _| |_(_)  _ __ ___   ___ "
  time.sleep(0.3)
  print C + " / __| |/ _ \/ _ \ '_ \| | | | __| | | '_ ` _ \ / _ \ "
  time.sleep(0.3)
  print C + " \__ \ |  __/  __/ |_) | |_| | |_| |_| | | | | |  __/ "
  time.sleep(0.3)
  print C + " |___/_|\___|\___| .__/ \__, |\__|_(_)_| |_| |_|\___| "
  time.sleep(0.3)
  print C + "                 |_|    |___/                        "
  time.sleep(0.5)
  main2()

def main2():
  print C + "1. I have to wake up at..."
  print C + "2. Find out when to get up if you go to bed now"
  print C + "3. Exit"
  userChoice=inputNumber(O + "Your choice: ")
  if 1 <= int(userChoice) <= 3:
    if userChoice == 1:
      ein()
    if userChoice == 2:
      zwei()
    if userChoice == 3:
      sys.exit()
  else:
    error()
 
def ein():
  from datetime import timedelta
  while True:
    try:
    	timee = datetime.datetime.strptime(raw_input(C + 'Please enter the time you would like to wake up at in HH:MM format: '), "%H:%M")
	if timee == 2400:
	    print C + "You should try to fall asleep at one of the following times:"
	    time.sleep(0.3)
	    print O + "15:00"
	    time.sleep(0.3)
	    print "16:30"
	    time.sleep(0.3)
	    print "18:00"
	    time.sleep(0.3)
	    print "19:30"
	    time.sleep(0.5)
	elif timee != "24:00":   
	    one = timee + timedelta(minutes=900) #smqta greshno zaradi strptime kogato e <=8:00 (vadi 1899 god.) zatova +15h 15*60=900
	    two = timee + timedelta(minutes=990)
	    three = timee + timedelta(minutes=1080)
	    four = timee + timedelta(minutes=1170)
	    print C + "You should try to fall asleep at one of the following times:"
	    time.sleep(0.3)
	    print O + one.strftime('%H:%M')
	    time.sleep(0.3)
	    print two.strftime('%H:%M')
	    time.sleep(0.3)
	    print three.strftime('%H:%M')
	    time.sleep(0.3)
	    print four.strftime('%H:%M')
	    time.sleep(0.5)
	print R + "Please keep in mind that you should be falling asleep at these times."
	print R + "It takes the average human fourteen minutes to fall asleep."
	print O + "sleepyti.me works by counting backwards in sleep cycles. Waking up in the middle of a sleep cycle leaves you feeling tired and groggy, but waking up in between cycles wakes you up feeling refreshed and alert!"
	end()
    except ValueError:
	print R + "Problems with your input!"
	print "Please try again!"
    else:
	break


def zwei():
  from datetime import datetime, timedelta
  print "Current time is: " + datetime.now().strftime('%H:%M')
  one = datetime.now() + timedelta(minutes=105)
  two = datetime.now() + timedelta(minutes=195)
  three = datetime.now() + timedelta(minutes=285)
  four = datetime.now() + timedelta(minutes=375)
  five = datetime.now() + timedelta(minutes=465)
  six = datetime.now() + timedelta(minutes=555)
  print C + "If you head to bed right now, you should try to wake up at one of the following times:"
  time.sleep(0.3)
  print O + one.strftime('%H:%M')
  time.sleep(0.3)
  print two.strftime('%H:%M')
  time.sleep(0.3)
  print three.strftime('%H:%M')
  time.sleep(0.3)
  print four.strftime('%H:%M')
  time.sleep(0.3)
  print five.strftime('%H:%M')
  time.sleep(0.3)
  print six.strftime('%H:%M')
  time.sleep(0.5)
  print R + "Please keep in mind that you should be falling asleep at these times."
  print R + "It takes the average human fourteen minutes to fall asleep."
  end()
  
if __name__ == "__main__":
  main()
  
