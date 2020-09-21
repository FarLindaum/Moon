
import os
import time
import requests
import random
import string

# Wait... i thought you wouldnt Skid? :angery:
# - MoonDev.#1337

dir_path = os.path.dirname(os.path.realpath(__file__)) # In Case it Cant find the Tokens File

MainTitle = '''

                                                ╔╦╗╔═╗╔═╗╔╗╔
                                                ║║║║ ║║ ║║║║
                                                ╩ ╩╚═╝╚═╝╝╚╝

                              ╔═══════════════════════════════════════════════╗
                              ║  Server-Joiner             -          1       ║
                              ║  Server-Flooder            -          2       ║
                              ║  Server-Leaver             -          3       ║
                              ║  DM-Friender               -          4       ║
                              ║  DM-Flooder                -          5       ║
                              ║  Check-Tokens              -          6       ║
                              ║  Generate-Tokens           -          7       ║
                              ║  Exit                      -          0       ║
                              ╚═══════════════════════════════════════════════╝
                                        
'''

PreTitle = '''

                                                ╔╦╗╔═╗╔═╗╔╗╔
                                                ║║║║ ║║ ║║║║
                                                ╩ ╩╚═╝╚═╝╝╚╝

                              ╔═══════════════════════════════════════════════╗
                              ║  Main-Menu                 -          1       ║
                              ║  Check-Tokens.txt          -          2       ║
                              ║  Check-Working.txt         -          3       ║
                              ║  Check-Generated.txt       -          4       ║
                              ║  Exit                      -          0       ║
                              ╚═══════════════════════════════════════════════╝
                                        
'''

SplashTitle = '''

                                                ╔╦╗╔═╗╔═╗╔╗╔
                                                ║║║║ ║║ ║║║║
                                                ╩ ╩╚═╝╚═╝╝╚╝

'''

def PreScreen():

    os.system("cls")

    print(PreTitle)

    Selection = input("[ >>> ] Moon@Selection: ")

    if Selection == "1":

        Main()

    elif Selection == "2":

        CheckTokens()

    elif Selection == "3":
        
        CheckWorking()
    
    elif Selection == "4":

        CheckGenerated()

    elif Selection == "0":

        exit()

def CheckGenerated():
    
    os.system("cls")
    print(SplashTitle)
    print("[ /-/ ] Moon@Checking-Tokens")
    time.sleep(1)

    TokenList = []

    WorkingTokens = []

    count = 0

    with open(f'{dir_path}\\TokensGenerated.txt', 'r') as Tokens:

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

def CheckWorking():

    os.system("cls")
    print(SplashTitle)
    print("[ /-/ ] Moon@Checking-Tokens")
    time.sleep(1)

    TokenList = []

    WorkingTokens = []

    count = 0

    with open(f'{dir_path}\\Working.txt', 'r') as Tokens:

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


def CheckTokens():

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
        
        ServerLeaver()
    
    elif Selection == "4":

        DMFriender()

    elif Selection == "5":

        DMFlooder()

    elif Selection == "6":

        Check()

    elif Selection == "7":

        Generate()

    elif Selection == "0":

        exit()

def Join(): # Add ban shit

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

                print("[ +++ ] Token: " + Token + " Joined the Server Using the Invite Code: " + Invite + " - " + str(joined))

            else:

                print("[ --- ] Token: " + Token + " Couldnt Join the Server! Check the Tokens Again or the Account has been Banned!")

    time.sleep(2)

    Main()

def ServerFlooder():

    TokenList = []

    sent = 0

    os.system("cls")

    print(SplashTitle)

    Channel_ID = input("[ >>> ] Moon@Channel-ID: ")

    os.system("cls")

    print(SplashTitle)

    Message = input("[ >>> ] Moon@Message-Content: ")

    with open(f'{dir_path}\\Working.txt', 'r') as Tokens:

        for line in Tokens:

            TokenList.append(line.strip())

        while 1:

            for Token in TokenList:

                headers = {

                    "authorization": f"{Token}"
                }

                payload = {'content' : f'{Message}', 'tts' : 'true'}

                r = requests.post(f"https://discordapp.com/api/v8/channels/{Channel_ID}/messages", headers=headers, json=payload)

                if r.status_code == 200:

                    sent += 1

                    print("[ +++ ] Token: " + Token + " Sent Message: " + Message + " - " + str(sent))


                elif "You are being rate limited" in r.text:

                    print("[ --- ] Token: " + Token + " Couldnt Send Message! You are being Ratelimited!")

                else:

                    print("[ --- ] Token: " + Token + " Couldnt Send Message! Are you Sure you Entered everything Correct?")
    
    

def ServerLeaver():

    TokenList = []

    left = 0

    os.system("cls")

    print(SplashTitle)

    ServerID = input("[ >>> ] Moon@Server-ID: ")

    
    with open(f'{dir_path}\\Working.txt', 'r') as Tokens:

        for line in Tokens:

            TokenList.append(line.strip())

        
        for Token in TokenList:
        
            headers = {
        
                "authorization": f"{Token}"
        
            }
        
            r = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{ServerID}", headers=headers)
        
            if r.status_code == 204:
    
                left += 1

                print("[ +++ ] Token: " + Token + " Left Server: " + ServerID + " - " + str(left))
        
            else:
  
                print("[ --- ] Token: " + Token + " Couldnt Leave Server! Are you Sure you entered Everything Correct?")

    time.sleep(2)

    Main()

def DMFriender(): 


    TokenList = []

    friends = 0

    os.system("cls")

    print(SplashTitle)

    UserID = input("[ >>> ] Moon@User-ID: ")

    
    with open(f'{dir_path}\\Working.txt', 'r') as Tokens:

        for line in Tokens:

            TokenList.append(line.strip())

        
        for Token in TokenList:
        
            headers = {
        
                "authorization": f"{Token}"
        
            }

            payload = {'' : ''}
        
            r = requests.put(f"https://discordapp.com/api/v8/users/@me/relationships/{UserID}", headers=headers, json=payload)
        
            if r.status_code == 204:
    
                friends += 1

                print("[ +++ ] Token: " + Token + " Friended User: " + UserID + " - " + str(friends))

            elif "Cannot send friend request to self" in r.text:

                print("[ --- ] Token: " + Token + " Cant add itself!")
        
            else:
  
                print("[ --- ] Token: " + Token + " Couldnt Friend User! Are you Sure you entered Everything Correct?")

    time.sleep(2)

    Main()

def DMFlooder(): 


    TokenList = []

    sent = 0

    os.system("cls")

    print(SplashTitle)

    ChannelID = input("[ >>> ] Moon@Channel-ID: ")

    os.system("cls")

    print(SplashTitle)

    Message = input("[ >>> ] Moon@Message-Content: ")

    with open(f'{dir_path}\\Working.txt', 'r') as Tokens:

        for line in Tokens:

            TokenList.append(line.strip())

        while 1:

            for Token in TokenList:

                headers = {

                    "authorization": f"{Token}"
                }

                payload = {'content' : f'{Message}', 'tts' : 'true'}

                r = requests.post(f"https://discordapp.com/api/v8/channels/{ChannelID}/messages", headers=headers, json=payload)

                if r.status_code == 200:

                    sent += 1

                    print("[ +++ ] Token: " + Token + " Sent Message: " + Message + " - " + str(sent))


                elif "You are being rate limited" in r.text:

                    print("[ --- ] Token: " + Token + " Couldnt Send Message! You are being Ratelimited!")

                else:

                    print("[ --- ] Token: " + Token + " Couldnt Send Message! Are you Sure you Entered everything Correct?")

def Generate():

    os.system("cls")

    print(SplashTitle)

    Amount = input('[ >>> ] How many Generations: ')

    count = 0

    TokensGen = []

    os.system("cls")

    for i in range(int(Amount)):


        Token1 = f'Nz{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}.X{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}.{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}'
        Token2 = f'NT{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}.X{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}.{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}'
        Token3 = f'ND{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}.X{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}.{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}'
        Token4 = f'Nz{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}.X{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}.{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}'
        Token5 = f'Nj{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}.X{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}.{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}'
        Token6 = f'ND{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}.X{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}.{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}{(random.choice(string.ascii_letters + string.digits))}'

        tokens = [
            Token1,
            Token2,
            Token3,
            Token4,
            Token5,
            Token6
            ]

        
        count += 1

        TokensReal = random.choice(tokens)

        print('[ +++ ] Generated: '  +  TokensReal  + ' - ' + str(count))

        TokensGen.append(TokensReal)

        
 
    open(f'{dir_path}\\TokensGenerated.txt', 'w+').write(str("\n".join(TokensGen)))


    Main()
    


if __name__ == "__main__":

    PreScreen()
