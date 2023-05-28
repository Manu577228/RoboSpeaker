#  This Project only works on mac os as "say" command is for Mac OS

import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 2.0 created by Manu")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
           os.system("say 'bye bye friend' ")
        break
    command = f"say {x}"
    os.system(command)



