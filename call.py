from subprocess import check_call
import sys
import time
from uiautomator import Device

def callAdb(opt, serial):
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_WAKEUP'])
    time.sleep(3)
    # home
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
    time.sleep(3)
    # Menu_click
    check_call(['adb', 'shell', 'input', 'touchscreen', 'tap', "50", "1090"])
    time.sleep(3)
    # Phone
    check_call(['adb', 'shell', 'input', 'touchscreen', 'tap', "1", "136"])
    time.sleep(3)
    # Marcar
    print(opt)
    for i in str(opt):
        numberAdb(i, serial)
    #Insert_number
    check_call(['adb', 'shell', 'input', 'touchscreen', 'tap', "291", "1043"])
    time.sleep(1)
    #Press_call
    return True

def callUiautomator(opt, serial):
    d = Device(serial)
    d.wakeup()
    time.sleep(2)
    # home
    d.press.home()
    time.sleep(2)
    # Menu_click
    if(d(text='Phone', className='android.widget.TextView').exists):
        d(text='Phone', className='android.widget.TextView').click()
        time.sleep(2)
        d(text='Dial', className='android.widget.TextView').click()
        time.sleep(2)
        d(resourceId="com.android.contacts:id/digits").clear_text()
        for i in opt:
            if(i == "+"):
                d(text='0', className='android.widget.TextView').long_click()
            else:
                d(text=i, className='android.widget.TextView').click()
            time.sleep(2)
        d(className='android.widget.ImageButton', resourceId='com.android.contacts:id/btnLogsCall').click()
        time.sleep(1)
        return True
    else:
        print("Phone is not at home")
        return False


def numberAdb(number,serial):
    numbers = [["1", 97, 598], ["2", 305, 598], ["3", 513, 598],
               ["4", 97, 713],["5", 305, 713], ["6", 513, 713],
               ["7", 97, 828],["8", 305, 828],["9", 513, 828],
               ["0", 305, 942],["*", 87, 949], ["#", 513, 945],["+", 305, 942]]

    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            if(number == "+"):
                if numbers[i][j] == number:
                    check_call(['adb', 'shell', 'input', 'swipe', str(numbers[i][j+1]), str(numbers[i][j+2]),str(numbers[i][j+1]), str(numbers[i][j+2]), "2000"])
                    time.sleep(1)
                    print(number)
            else:
                if numbers[i][j] == number:
                    check_call(['adb', 'shell', 'input', 'touchscreen', 'tap', str(numbers[i][j+1]), str(numbers[i][j+2])])
                    time.sleep(1)
                    print(number)
