import time
from playsound import playsound

r = input("Timer for how long? ")
userNumInput = ''.join(x for x in r if x.isdigit())
userStrInput = ''.join(y for y in r if y.isalpha())


if(userStrInput=="min" or userStrInput=="minutes" or userStrInput=="mins" or userStrInput=="minute" and int(userNumInput)<60):
    getUserNumber = int(userNumInput)
    userNumberInSec = int(getUserNumber) * 60
    for i in range(int(userNumberInSec),-1,-1):
        time.sleep(1)
        print('Your timer for',getUserNumber,'mins','in seconds is Starting Now: ','%d\r'%i, end="")
elif(userStrInput=="sec" or userStrInput=="seconds" or userStrInput=="secs" or userStrInput=="second" and int(userNumInput)<60):
    for i in range(int(userNumInput),-1,-1):
        getUserNumberS = userNumInput
        time.sleep(1)
        print('Your timer for',getUserNumberS,'seconds,','Starting Now:','%d\r'%i, end="")
elif(int(userNumInput)>=60 and userStrInput=="mins" or userStrInput=="min" or userStrInput=="minutes" or userStrInput=="minute"):
    print('sorry! This is too long, Try using less than Hour!!')
elif(int(userNumInput)>=60):
    getNumber = int(userNumInput)
    intoMinutes = int(getNumber)/60
    print('Your timer for',getNumber,'secs or',intoMinutes,'minutes','in secods is Starting Now: ','%d\r'%i, end="")
else:
    print("\n This Timer can only be set for minutes and seconds!!")
    r = input("Timer for how long? ")

while True:
    x = playsound('/Users/rudrashah/Desktop/My_python_course/analog-watch-alarm_daniel-simion.mp3')
    
print("\nYour timer for",userNumInput,userStrInput,"is now over")
print("\n      Created by Rudra shah")
    
    

