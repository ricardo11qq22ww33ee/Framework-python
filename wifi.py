
from uiautomator import Device
import time
import sys
from serial import read_serial
from printer import start, end
#---------------------------------------------------------------------------

if __name__ == "__main__":

    first_serial = read_serial()
    if(first_serial == "No devices"):
        print("No devices connected")
    else:
        d = Device(first_serial)
        start()
        try:
            d.wakeup()
            time.sleep(1)
            d.press.home()
            time.sleep(1)
            if(d(text='Settings', className='android.widget.TextView').exists):

                d(text='Settings', className='android.widget.TextView').click()
                time.sleep(1)
                d(text='Networks', className='android.widget.TextView').click()
                time.sleep(1)
                d(text='Networks', className='android.widget.TextView').click()
                time.sleep(1)
                d(text='Wi-Fi', className='android.widget.TextView').click()
                time.sleep(1)
                if d(text='ON', className='android.widget.Switch').exists:
                    print('The wifi is off')
                    d(text='ON', className='android.widget.Switch').click()
                    print('The wifi was turned on')
                else:
                    print('The wifi is on')
                    d(text='OFF', className='android.widget.Switch').click()
                    print('The wifi was turned off')
                time.sleep(1)
            else:
                print("Settings is not at home")
        except Exception as ex:
            print(ex)
        finally:
            end()
    


    
    