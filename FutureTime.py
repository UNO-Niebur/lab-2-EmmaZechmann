#FutureTime.py
#Name: Emma Zechmann
#Date: 2/1/2026
#Assignment: Future time

# datetime will allow us to access the system date and time.
import datetime

def main():
    tz =datetime.timezone(datetime.timedelta(hours=+6))
    now=datetime.datetime.now(tz)

    #getting current time from system, storing to variable

  #TODO:
    hour = int(input("Give me a number of hours: "))
    minute = int(input("Give me a number of minutes: "))
    future_time = now + datetime.timedelta(hours=hour , minutes=minute)
    print("The future time will be: ")
    print(f"{future_time.hour}:{future_time.minute:02d}")

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
