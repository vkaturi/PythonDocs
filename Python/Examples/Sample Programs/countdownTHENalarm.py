import time, subprocess
timeLeft = 10
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1
subprocess.Popen(['start', 'alarm.wav'], shell=True)
