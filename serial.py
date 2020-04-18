from subprocess import check_output
def read_serial():
    output = check_output(['adb', 'devices'])
    lines = output.splitlines()
    no_devices = lines[1]
    if(no_devices == ""):
        return ("No devices")
    else:
        first_dev = lines[1].split()[0]
        print ("1st Device on List = {}".format(first_dev))
        return first_dev

