import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # set BCM chip as handle
GPIO.setwarnings(False)
# set some useful channel
Relay_1 = 20
Relay_2 = 21
PWM_1   = 26
Output_List = [Relay_1,Relay_2,PWM_1]

GPIO.setup (Output_List,GPIO.OUT,initial = GPIO.HIGH)

"""
init_freq = 50 # initial frequency in Hz
PWM_Pin37 = GPIO.PWM(PWM_1, init_freq)

# set GPIO as low/high output
GPIO.output(Relay_1,GPIO.LOW)

init_dc = 50
PWM_Pin37.start(init_dc)

# change frequency and duty cycle
para_freq = 60
para_duty = 20
PWM_Pin37.ChangeFrequency(para_freq)
PWM_Pin37.ChangeFrequency(para_duty)

# stop PWM out
PWM_Pin37.stop()
print(GPIO.input(Relay_2))
"""
def Pwm_func ():
    p = GPIO.PWM(PWM_1, 50) 
    p.start(0)   
    try:
        while 1:
            for dc in range(0, 101, 5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(100, -1, -5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    p.stop()    
Pwm_func ()
# release the system resource and close GPIO control
GPIO.cleanup()
