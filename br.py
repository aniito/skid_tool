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
un script Kiddie à été détécté ... || Skid Tool By anito && Cursed Help""")
    await asyncio.sleep(1)
    print("Skiddage en cours ...")


def rama_y():
    print("mon serveur : https://discord.gg/yHFQBKnXAF")
    print("tu auras compris que ce def sert à rien et donc est juste pour les personnes qui lisent le script vous êtes des bons !")




def prout():
    with open("skid.txt", "r") as f:
        for line in f.readlines():
                ski = line.strip()
                skid = requests.get(f"https://ctf-1-ymortail.netlify.app/user/{ski}.gif")
                if skid.status_code == 200:
                    print ('[+] FOUND :', ski)
                    print("[+] Une backdoor à été installée dans votre système ")
                    break
                else:
                    print("[-] NOT WORK :", ski)
                    pass


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    prout()
