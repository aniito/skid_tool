import requests
import asyncio
# import script_kiddage
# from skid_universal import 2qi


async def main():
    print(""" 
 ____  ____  _   _ _____ _____   _____ ___  ____   ____ _____ 
                _A
                .'`"`'.
               /   , , \\
              |   <\^/> |
              |  < (_) >|
              /====\\
             (.--._ _.--.)
              |\  -`\- /|
              |(_.- >-.)|
              \__.-'^'._/
               |\   .  /
            _.'\ '----'|'-.
        _.-'  O ;-.__.' \O `o.
       /o \      \/-.-\/|     \\
   43G|    ;,     '.|\| /
A script Kiddie has been detected ... || Skid Tool By anito && Cursed Help""") #translated by NeKroFR
    await asyncio.sleep(1)
    print("Skiddage in progress...")


def rama_y():
    print("discord : https://discord.gg/yHFQBKnXAF")
    print("You will understood that this ctf is useless and is just for the people who read the script you are good ones!")




def prout():
    with open("skid.txt", "r") as f:
        for line in f.readlines():
                ski = line.strip()
                skid = requests.get(f"https://ctf-1-ymortail.netlify.app/user/{ski}.gif")
                if skid.status_code == 200:
                    print ('[+] FOUND :', ski)
                    print("[+] A backdoor has been installed in your system ")
                    break
                else:
                    print("[-] NOT WORK :", ski)
                    pass


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    prout()





