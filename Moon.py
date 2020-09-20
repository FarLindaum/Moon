
import os
import time
import requests

# Wait... i thought you wouldnt Skid? :angery:
# - MoonDev.#1337

dir_path = os.path.dirname(os.path.realpath(__file__)) # In Case it Cant find the Tokens File

MainTitle = '''

                                                ╔╦╗╔═╗╔═╗╔╗╔
                                                ║║║║ ║║ ║║║║
                                                ╩ ╩╚═╝╚═╝╝╚╝

                              ╔═══════════════════════════════════════════════╗
                              ║  Joiner                    -          1       ║
                              ║  Server-Flooder            -          2       ║
                              ║  DM-Flooder                -          3       ║
                              ║  Change-Nickname           -          4       ║
                              ║  Typing-Status             -          5       ║
                              ║  Webhook-Options           -          6       ║
                              ║  Exit                      -          0       ║
                              ╚═══════════════════════════════════════════════╝
                                        
'''

SplashTitle = '''

                                                ╔╦╗╔═╗╔═╗╔╗╔
                                                ║║║║ ║║ ║║║║
                                                ╩ ╩╚═╝╚═╝╝╚╝

'''

def Check():

    os.system("cls")
    print(SplashTitle)
    print("[ /-/ ] Moon@Checking-Tokens")
    time.sleep(1)

    TokenList = []

    WorkingTokens = []

    count = 0

    with open(f'{dir_path}\\Tokens.txt', 'r') as Tokens:

        for line in Tokens:

            TokenList.append(line.strip())

            count += 1

    os.system("cls")

    print(SplashTitle)

    print(f"[ /-/ ] Moon@Detected-{count}-Tokens")

    time.sleep(1)

    os.system("cls")

    print(SplashTitle)

    for Token in TokenList:
        
        headers = {'Authorization' : Token}

        r = requests.get(f"https://discord.com/api/v8/users/@me", headers=headers)

        if r.status_code == 200:

            print(f"[ +++ ] Moon@{Token}-Valid")

            WorkingTokens.append(Token)

        else:

            print(f"[ --- ] Moon@{Token}-Invalid")

    open(f'{dir_path}\\Working.txt', 'w+').write(str("\n".join(WorkingTokens)))

    os.system("cls")

    time.sleep(0.5)

    print(SplashTitle)

    print(f"[ /-/ ] Moon@Checked-Tokens")

    time.sleep(1)

    Main()


    
                
def Main():

    os.system("cls")
    print(MainTitle)
    Selection = input("[ >>> ] Moon@Selection: ")

    if Selection == "1":

        Join()

    elif Selection == "2":

        ServerFlooder()

    elif Selection == "3":
        
        DMFlooder
    
    elif Selection == "4":

        ChangeNickName()

    elif Selection == "5":

        Typing()

    elif Selection == "6":

        Webhook()

    elif Selection == "0":

        exit()

def Join():

    TokenList = []

    joined = 0

    os.system("cls")

    print(SplashTitle)

    Invite = input("[ >>> ] Moon@Invite-Code: ")

    Invite2 = Invite[19:2000]

    with open(f'{dir_path}\\Working.txt', 'r') as Tokens:

        for line in Tokens:

            TokenList.append(line.strip())

        for Token in TokenList:
            
            headers = {'Authorization' : Token}

            r = requests.post(f"https://discordapp.com/api/v8/invites/{Invite2}", headers=headers)

            if r.status_code == 200:
                
                joined += 1

                joined = str(joined)

                print("Token: " + Token + " Joined the Server Using the Invite Code: " + Invite + " - " + joined)

            else:

                print("Token: " + Token + " Couldnt Join the Server! Check the Tokens Again or the Account has been Banned!")

def ServerFlooder():

Check()
