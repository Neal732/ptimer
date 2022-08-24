import time
seconds = int(input("Enter the time in seconds:"))
def countDownTimer(seconds):
    while seconds>0:
        min = int(seconds/60)
        sec = int(seconds%60)
        timer = "{:02d}:{:02d}".format(min,sec)
        print(timer,end="\r")
        time.sleep(1)
        seconds -=1
    print("Time up")

countDownTimer(seconds)