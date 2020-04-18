def verify_number(number):
    try:

        if len(number) == 10:
            validation = True
            if ("+" in number or "*" in number):
                print("Invalid number")
                return False
            else:
                for i in number:
                    if (i.isdigit()):
                        print(i)
                    else:
                        validation = False
                print(validation)
                if(validation == False):
                    print("Invalid number")
                    return False
                else:
                    print("National key")
                    return True

        if len(number) == 13:
            if "*" in number:
                print("Invalid number")
                return False
            if (number[0]== "0" and number[1]== "0" and number[2]== "1"):
                print("USA")
                return True
            if (number[0]== "+"):
                validation = True
                for i in range(len(number)):
                    if (number[i].isdigit()):
                        print(i)
                    else:
                        if(number[i] == "+" and i == 0):
                            print(i)
                        else:
                            validation = False
                print(validation)
                if(validation == False):
                    print("Invalid number")
                    return False
                else:
                    print("National key")
                    return True
            else:
                print("Invalid number")
                return False

        if len(number) == 7:
            if ("+" in number or "*" in number):
                print("Invalid number")
                return False
            else:
                for i in number:
                    if (i.isdigit()):
                        print(i)
                    else:
                        validation = False
                print(validation)
                if(validation == False):
                    print("Invalid number")
                    return False
                else:
                    print("Regional key")
                    return True

        if "*" == number[0]:
            for i in range(len(number)):
                    if (number[i].isdigit()):
                        print(i)
                    else:
                        if(number[i] == "*" and i == 0):
                            print(i)
                        else:
                            validation = False
            print(validation)
            if(validation == False):
                print("Invalid number")
                return False
            else:
                print("Services key")
                return True

        if "911" in number:
            print ("Emergency")
            return True

        else:
            print("Invalid number")
            return False

    except Exception as ex:
        print("Invalid number")
        return False
