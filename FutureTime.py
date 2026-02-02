#FutureTime.py
#Name: Emma Zechmann
#Date: 2/1/2026
#Assignment: Future time

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  
    currentHour = int(input("give me the current hour: "))
    currentMinute = int(input("give me the current minutes: "))

     
  #TODO:
    Number_hours = int(input("Give me a number of hours: "))
    Number_minutes = int(input("Give me a number of minutes: "))
    Totalmin = (currentHour * 60) + (currentMinute) + (Number_hours * 60) +Number_minutes
    
    Future_hours= (Totalmin//60)
   
    future_min=(Totalmin/60)-(Future_hours)
    New_min=(future_min * 60)

    print("The future time will be: ")
    print(f"{Future_hours}:{New_min}")

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
