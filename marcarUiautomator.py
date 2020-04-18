
from uiautomator import Device
import sys
from serial import read_serial
from printer import start, end
from utils import verify_number
from call import callUiautomator

#---------------------------------------------------------------------------

if __name__ == "__main__":

    first_serial = read_serial()
    if(first_serial == "No devices"):
        print("No devices connected")
    else:
        start()
        print("Please insert the telephone number you want to call")
        while True:
            opt = raw_input()
            if opt == 'q':
                print("Exit")
                break
            if verify_number(opt):
                print ("Calling")
                try:
                    callUiautomator(opt,first_serial)
                except Exception as ex:
                    print("Exception")
                    print(ex)
                finally:
                    end()


    
    