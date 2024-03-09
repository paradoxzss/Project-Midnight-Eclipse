# Property of Vantage Point Incorporated and InterWarp Industries. Do not steal, and don't fork without credits.

"""
Program Data:
Creation date: 3/8/24 @ 5:00 PM
Purpose: A simple modifiable program for project Midnight Eclipse, or simply, the SecurDeck.
Coder(S): PARADOXzss
 """

# Now to the main stuff!
print("Credits to:")
print("")
print("   ___  ___   ___  ___   ___  ____  _  __          ")
print("  / _ \/ _ | / _ \/ _ | / _ \/ __ \| |/_/__ ___ ___")
print(" / ___/ __ |/ , _/ __ |/ // / /_/ />  </_ /(_-<(_-<")
print("/_/  /_/ |_/_/|_/_/ |_/____/\____/_/|_|/__/___/___/")
print("                                                   ")

print("VANTAGE POINT INCORPORATED and InterWarp Industries presents:")
print("")

# Project name, in this case, the code is made specifically for the SecurDeck
print("   ▄████████    ▄████████  ▄████████ ███    █▄     ▄████████ ████████▄     ▄████████  ▄████████    ▄█   ▄█▄ ")
print("  ███    ███   ███    ███ ███    ███ ███    ███   ███    ███ ███   ▀███   ███    ███ ███    ███   ███ ▄███▀ ")
print("  ███    █▀    ███    █▀  ███    █▀  ███    ███   ███    ███ ███    ███   ███    █▀  ███    █▀    ███▐██▀   ")
print("  ███         ▄███▄▄▄     ███        ███    ███  ▄███▄▄▄▄██▀ ███    ███  ▄███▄▄▄     ███         ▄█████▀    ")
print("▀███████████ ▀▀███▀▀▀     ███        ███    ███ ▀▀███▀▀▀▀▀   ███    ███ ▀▀███▀▀▀     ███        ▀▀█████▄    ")
print("         ███   ███    █▄  ███    █▄  ███    ███ ▀███████████ ███    ███   ███    █▄  ███    █▄    ███▐██▄   ")
print("   ▄█    ███   ███    ███ ███    ███ ███    ███   ███    ███ ███   ▄███   ███    ███ ███    ███   ███ ▀███▄ ")
print(" ▄████████▀    ██████████ ████████▀  ████████▀    ███    ███ ████████▀    ██████████ ████████▀    ███   ▀█▀ ")
print("                                                  ███    ███                                      ▀         ")

# Pre-Made scripts can be uncommented to make this a specific preset program OR you can make your own script to make the SecurDeck program(s) specifically for you.

# Script one - a simple project viewer
"""
print("Current projects: SecurLine, SecurPad")
Selected_project = input("What project to view? ")
    if Selected_project == "SecurLine":
        print(
           "The SecurLine is a off-grid off-line messaging system ment for employees of VPI to communicate throughout the building.")
           
   elif Selected_project == "SecurPad":
   print("The SecurPad is a small notepad sized raspberry pi zero W device made for taking notes, reading code and monitering systems")
   """

# Script two - About the SecurDeck
"""
print("SecurDeck made by PARADOXzss.")
print("Options: Specs, Purpose, and Version")
Options = input("What option? ")
if Options == "Specs":
    print("The SecurDecks hardware is designed to be fast, but low cost. it is powered by a raspberry pi 4 B with 8gb of RAM. The storage of the device is a 128GB MicroSD swappable from the front I/O panel.")
elif Options == "Purpose":
    print("The SecurDeck is made for InfoSec and pentest workfields. It is also capable of being used as a coder's toolkit, complete with an IDE, or a normal device.")
elif Options == "Version":
    print("Version 0.07 PROTOTYPE")
else:
    print("Sorry, not an option.")
"""

# Script three - VPI info
"""
print("About VPI, or VANTAGE POINT INCORPORATED")
print("Options: CEO, DEVELOPER TEAM ONE, or PROJECTS")
Info_selection = input("What info would you like to see? ")
if Info_selection == "CEO":
    print("The CEO of VPI, PARADOXzss, is a part-time Python developer that made the company.")
elif Info_selection == "DEVELOPER TEAM ONE":
    print("Dev team one, or developer team one, is the first and only R&D team in VPI, led by the CEO, PARADOXzss.")
elif Info_selection == "PROJECTS":
    print("VPI and IWI has many projects that are in works, including the SecurDeck, SecurLine, SecurPad, SecurDeck programs, Omega Linux, and many more. All of these projects are computer related due to the fact the CEO does computers more than anything else.")
"""

# Script four - IWI info
"""
print("About IWI, or InterWarp Industries.")
print("Options: VPI and IWI, CEO, or Purpose")
Info_selection2 = input("What info would you like? ")
if Info_selection2 == "VPI and IWI":
    print("VPI and IWI are led by the same CEO, PARADOXzss, as sister companies, and VPI makes more infoSec and computer related devices, while IWI makes Planes and Fight/Bomber jets.")
elif Info_selection2 == "CEO":
    print("Same as VPI, CEO PARADOXzss, is a part-time Python developer that made the company.")
elif Info_selection2 == "Purpose":
    print("IWI makes more engineering related devices, while VPI makes more tech centered devices.")
"""

# Script five - Sales system
"""
print("Welcome to VPI & IWI Sales System")
# Prices
SecurDeck = 750
SecurLine = 250
SecurPad = 300
OmegaLinuxUSB = 30
print("Prices")
print("SecurDeck")
print(SecurDeck)
print("SecurLine")
print(SecurLine)
print("SecurPad")
print(SecurPad)
print("OmegaLinux USB")
print(OmegaLinuxUSB)

# Descriptions
SecurDeckDESCRIPTION = " The SecurDeck is a InfoSecurity Cyberdeck made specifically for VPI employees to use as a inventory managment device and a control console."
SecurLineDESCRIPTION = " The SecurLine is a offgrid and offline messaging system for emergency contact within the VANTAGE building in case of the power going out."
SecurPadDESCRIPTION = " The SecurPad is a raspberry pi zero phone replacment using the same tech as the SecurLine for messaging but ment for normal messaging."
OmegaLinuxUSBDESCRIPTION = "This is a simple USB drive with the OmegaLinux ISO burned on it. The drive is 512 GB."

# Sales system
cost = 0
#Purchase one
print("MAX 4 ITEMS")

# Item 1
sale1 = input("What first item? ")
if sale1 == "SecurDeck":
    print(SecurDeckDESCRIPTION)
elif sale1 == "SecurLine":
    print(SecurLineDESCRIPTION)
elif sale1 == "SecurPad":
    print(SecurPadDESCRIPTION)
elif sale1 == "OmegaLinux USB":
    print(OmegaLinuxUSBDESCRIPTION)

# item 2
sale2 = input("What second item? ")
if sale2 == "SecurDeck":
    print(SecurDeckDESCRIPTION)
elif sale2 == "SecurLine":
    print(SecurLineDESCRIPTION)
elif sale2 == "SecurPad":
    print(SecurPadDESCRIPTION)
elif sale2 == "OmegaLinux USB":
    print(OmegaLinuxUSBDESCRIPTION)

# Item 3
sale3 = input("What third item? ")
if sale3 == "SecurDeck":
    print(SecurDeckDESCRIPTION)
elif sale3 == "SecurLine":
    print(SecurLineDESCRIPTION)
elif sale3 == "SecurPad":
    print(SecurPadDESCRIPTION)
elif sale3 == "OmegaLinux USB":
    print(OmegaLinuxUSBDESCRIPTION)

# Item 4
sale4 = input("What fourth item? ")
if sale4 == "SecurDeck":
    print(SecurDeckDESCRIPTION)
elif sale4 == "SecurLine":
    print(SecurLineDESCRIPTION)
elif sale4 == "SecurPad":
    print(SecurPadDESCRIPTION)
elif sale4 == "OmegaLinux USB":
    print(OmegaLinuxUSBDESCRIPTION)

# Sale 1 CALC
if sale1 == "SecurDeck":
    cost =+ SecurDeck
elif sale1 == "SecurLine":
    cost =+ SecurLine
elif sale1 == "SecurPad":
    cost =+ SecurPad
elif sale1 == "OmegaLinux USB":
    cost =+ OmegaLinuxUSB

# Sale 2 CALC
if sale2 == "SecurDeck":
    cost =+ SecurDeck
elif sale2 == "SecurLine":
    cost =+ SecurLine
elif sale2 == "SecurPad":
    cost =+ SecurPad
elif sale2 == "OmegaLinux USB":
    cost =+ OmegaLinuxUSB

# Sale 3 CALC
if sale3 == "SecurDeck":
    cost =+ SecurDeck
elif sale3 == "SecurLine":
    cost =+ SecurLine
elif sale3 == "SecurPad":
    cost =+ SecurPad
elif sale3 == "OmegaLinux USB":
    cost =+ OmegaLinuxUSB

# Sale 4 CALC
if sale4 == "SecurDeck":
    cost =+ SecurDeck
elif sale4 == "SecurLine":
    cost =+ SecurLine
elif sale4 == "SecurPad":
    cost =+ SecurPad
elif sale4 == "OmegaLinux USB":
    cost =+ OmegaLinuxUSB
"""

# Project Midnight Eclipse by PARADOXzss on Github
