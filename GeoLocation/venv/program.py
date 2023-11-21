
'''
My api key
AIzaSyADySfAiLC9qj4gwpAY40Fs5B2mBBbwlfE
'''
def main():
    ipaddress= None

    for x in range(1,3):
        if ipaddress is not None:
            break

        print("Please Enter your IP address:")
        ipaddress = input()


    print(ipaddress)

    means = None

    print("Are you Walking or Driving?")
    print("reply with walking/driving")
    for x in range(0,3):
        if means is not None:
            break

        means = input()
        if means != "walking" and means != "driving":
            if x is not 2:
                print("Please reply with walking or driving")
            else:
                print("You should have replied with walking or driving")
            means = None

    if means is None:
        '''Quit application, user does not know what he wants'''
        return
    print(means)


main()
