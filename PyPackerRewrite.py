import os, json, sys, ctypes, webbrowser, subprocess, urllib.request, random, time #built in imports
try:
    import numpy, pygame #non built in imports, most people have these installed so not a problem
    from localization.funni import * #Splash Text
    from localization.en import * #English Localization
    from localization.du import * #German/Dutch Localization
    from localization.es_mx import * #Spanish Localization
    from localization.fr_ca import * #French Localization
    from update import *
except Exception:
    print("installing nessasary libraries...")
    os.system("pip3 install requirements.txt")
    time.sleep(3)
    os.startfile(sys.argv[0])

#constants
DefaultSettingsFormat = '{"SettingsVersion":"0", "DefaultVersion": "1.19.2", "DefaultEdition": "java","DefaultFilepath": "local", "FileMovement": "move", "AnsiColorToggle": true, "TextEditor": "notepad /a", "ImageEditor": "mspaint", "AudioEditor": "start Audacity", "Debug": false, "MinecraftDir":""}'
__version__ = "0.0.3+1.19.2_PyPacker_Unstable_Dev" #Version Number; Newest compatable (Java only) MC Version; Stable/Unstable; Dev, Beta, Release
random.seed(time.time())
SplashText = AListOfFunni[random.randrange(len(AListOfFunni))]

try:
    class utils:
        
        def LocalFiles(Self): #the "Self" is useless, but there are so many instances of this function with a blank input its not worth deleting
            return os.path.dirname(os.path.realpath(__file__))

        def ClearConsole():
            if sys.platform=='win32':
                os.system('cls')
            if sys.platform=='darwin':
                os.system('clear')
            print(f'{BGREEN}{WHITE}Version: "{__version__}"{RESET}\n\n')
                
        def EditSettings(JsonKey, Value):
            
            #set new value
            if "\\" or "/" in Value:
                SettingsData[JsonKey] = Value
            else:
                SettingsData[JsonKey] = Value.lower()
            
            #write new file
            with open('settings.json', 'w') as f:
                json.dump(SettingsData, f)
        
        def DeleteStuff(List):
            for Dele in len(List):
                if sys.platform=='win32':
                    os.system(f"del /f {List[Dele]}")
                if sys.platform=='darwin':
                    os.system(f"")
                    
    class main:
        def __init__(self):
            
            global BLACK, RED, BRED, GREEN, BGREEN, YELLOW, BYELLOW, BLUE, MAGENTA, BMAGENTA, CYAN, WHITE, BWHITE, RESET, BOLD, UNDERLINE
            BLACK = '\u001b[30m'
            RED = '\u001b[31m'
            BRED = '\u001b[41;1m'
            GREEN = '\u001b[32m'
            BGREEN = '\u001b[42;1m'
            YELLOW = '\033[92m'
            BYELLOW = '\u001b[43;1m'
            BLUE = '\u001b[34m'
            MAGENTA = '\u001b[35m'
            BMAGENTA = '\u001b[45;1m'
            CYAN = '\u001b[36;1m'
            WHITE = '\u001b[37m'
            BWHITE = '\u001b[47;1m'
            RESET = "\u001b[0m"
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
            
            global MissingFiles
            MissingFiles = []
            
            #the higher tha placement the better the program,
            #key is the program name, 
            #data is the command used to open a file pasted directly after, so leave the space
            #impossible to trigger no text or image editors on windows due to having them built in, so they're left out
            if sys.platform=='win32':
                TextEditors = {
                    "VSCode":"code ",
                    "NotpadPP":"start notepad++ ",
                    "notepad":"notepad "
                }
                ImageEditors = {
                    "Photoshop":" ",
                    "paint.net":" ",
                    "mspaint":"mspaint "
                }
                AudioEditors = {
                    "audacity":"start audacity ",
                    "No Audio Editor":"No Audio Editor"
                }
            if sys.platform=='darwin':#While this program doesnt work on linux/OSX, at least you can start it up without <i>serious</i> errors
                TextEditors = {
                    "VSCode":"code ",
                    "NotpadPP":"start notepad++ ",
                    "No Text Editor":"No Text Editor"
                }
                ImageEditors = {
                    "Photoshop":" ",
                    "paint.net":" ",
                    "No Image Editor":"No Image Editor"
                }
                AudioEditors = {
                    "audacity":"start audacity ",
                    "No Audio Editor":"No Audio Editor"
                }
            
            if bool(os.path.exists(utils.LocalFiles("") + r"\output")) != True:
                MissingFiles.append("Created \"output\" folder as it was missing from local (" + utils.LocalFiles("") + ")\n")
                os.chdir(utils.LocalFiles(""))
                os.mkdir('output')
                
            if bool(os.path.exists(utils.LocalFiles("") + r"\assets")) != True:
                MissingFiles.append("Created \"assets\" folder as it was missing from local (" + utils.LocalFiles("") + ")\n")
                os.chdir(utils.LocalFiles(""))
                os.mkdir('assets')
            
            if bool(os.path.exists(utils.LocalFiles("") + r"\settings.json")) != True:       
                MissingFiles.append("Created and filled \"settings.json\" file as it was missing from local (" + utils.LocalFiles("") + ")\n")
                os.chdir(utils.LocalFiles(""))
                with open("settings.json", "x") as NewSettings:
                    NewSettings.write(DefaultSettingsFormat)
                    NewSettings.close()
                
            if bool(os.path.exists(utils.LocalFiles("") + r"\assets\Aberdeen_Tolbooth.jpg")) != True:
                MissingFiles.append("Downloaded \"Aberdeen_Tolbooth.jpg\" file as it was missing from local (" + utils.LocalFiles("") + ")\n")
                imgURL = "https://upload.wikimedia.org/wikipedia/commons/6/62/Aberdeen_Tolbooth.jpg"
                imgLOCAL = utils.LocalFiles("") + r"\assets\Aberdeen_Tolbooth.jpg"
                urllib.request.urlretrieve(imgURL, imgLOCAL)
            
            if bool(os.path.exists(utils.LocalFiles("") + r"\assets\United_States_Navy_Band_-_God_Save_the_Queen.oga")) != True:
                MissingFiles.append("Downloaded \"United_States_Navy_Band_-_God_Save_the_Queen.oga\" file as it was missing from local (" + utils.LocalFiles("") + ")\n")
                imgURL = "https://upload.wikimedia.org/wikipedia/commons/0/03/United_States_Navy_Band_-_God_Save_the_Queen.oga"
                imgLOCAL = utils.LocalFiles("") + r"\assets\United_States_Navy_Band_-_God_Save_the_Queen.oga"
                urllib.request.urlretrieve(imgURL, imgLOCAL)
                
            #i hit randomize a few times and found the page for Aberdeen Tolbooth, a prison turned museum in Scotland
            #"god save the king" was the only free audio file i could think of that wasn't from a sketchy site
            #full rights to the copyright holder of this photo, if it needs to be removed i will gladly do so
            #note: do not remove the depricated print statements, they will be used later

            SettingsFile = utils.LocalFiles("") + "\settings.json"
            
            with open(SettingsFile, "r") as f:
                global SettingsData
                SettingsData = json.load(f)
            
            global filePath
            if SettingsData['DefaultFilepath'] == 'local': 
                filePath = utils.LocalFiles('') + r'\output'
            else:
                filePath = SettingsData['DefaultFilepath']
            
            print(f"Begin Debug Logs:\n\n"
                  f"setting.json loaded: {SettingsData}\n"
                  f"Files Downloaded/Created: {str(MissingFiles)}\n"
                  f"Output Filepath: {filePath}\n")
            
            if SettingsData["AnsiColorToggle"] == False:
                BLACK, RED, BRED, GREEN, BGREEN, YELLOW, BYELLOW, BLUE, MAGENTA, BMAGENTA, CYAN, WHITE, BWHITE, RESET, BOLD, UNDERLINE = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
                
                print(f'ANSI Text Coloring is turned off')
            else:
                print(f'{BYELLOW}{WHITE}ANSI Text Coloring is turned on{RESET}')
        
        def main(self):
            
            #Startup/Debug Menu
            MenuingInput = print(f'{BYELLOW}{WHITE}If you are seeing this for more than a microsecond, Debug mode is turned on. Input a command or simply press enter to continue.{RESET}\n\n{CYAN}')
            if SettingsData["Debug"] == True:
                MenuingInput = input("")
                if MenuingInput != "":
                    if MenuingInput == "temp":
                        pass
                    if MenuingInput == "temp":
                        pass
                    if MenuingInput == "temp":
                        pass
                
            utils.ClearConsole()
            MenuingTemp = ""
            validMain = "mainmenu"
            while validMain == "mainmenu":
                    
                #Main Menu
                if MissingFiles == []:
                    MenuingInput = input(f"{BGREEN}{WHITE}PyPacker Main Menu:{RESET}\n"
                                        f'{BGREEN}{WHITE}All commands in PyPacker are case sensitve, "open" and "out" not guaranteed to work on all Lunix distros{RESET}\n'
                                        f'{BGREEN}{WHITE}You can format "set" and "link" commands like "Command Here":"Command On Next Screen" to skip navigation{RESET}\n'
                                        
                                        f'\n{BGREEN}{WHITE}Program Folders:{RESET}\n'
                                        f"{BWHITE}{BLACK}Open Program Folder > open {RESET}\n"
                                        f"{BWHITE}{BLACK}Open Output Folder > out {RESET}\n"
                                        
                                        f'\n{BGREEN}{WHITE}PyPacker:{RESET}\n'
                                        f"{BWHITE}{BLACK}Pack File Generators > pfiles (Datapack, Behavior, Resource){RESET}\n"
                                        f"{BWHITE}{BLACK}Pack File Editors > pedit (Datapack, Behavior, Resource){RESET}\n"
                                        f"{BWHITE}{BLACK}Other File Editors > oedit (Scarpet, PLCCjson, Mlog){RESET}\n"
                                        
                                        f'\n{BGREEN}{WHITE}Miscellaneous:{RESET}\n'
                                        f"{BWHITE}{BLACK}Settings Menu > set {RESET}\n"
                                        f"{BWHITE}{BLACK}External Links > link {RESET}\n\n"
                                        
                                        f"{BWHITE}{BLACK}Quit PyPacker > quit {RESET}\n"
                                        f"{BWHITE}{BLACK}Restart PyPacker > res {RESET}\n"
                                        f"{CYAN}\n").lower()
                    
                else:
                    MenuingInput = "set"
                
                if ":" in MenuingInput:
                    MenuingTemp = MenuingInput[4:].replace(':', '')
                    MenuingInput = MenuingInput[:4].replace(':','')
                
                #Program Folders
                if MenuingInput == "open": #opens the program file location
                    if sys.platform=='win32':
                        os.system("start " + utils.LocalFiles(""))

                    if sys.platform=='darwin':
                        os.system("open " + utils.LocalFiles(""))

                    utils.ClearConsole()
                    print(RESET + BYELLOW + "Program File has been opened, choose another option." + RESET + CYAN + "\n")
                    
                elif MenuingInput == "out": #attempts to open the program output file location
                    
                    if sys.platform=='win32':
                        os.system("start " + filePath)

                    if sys.platform=='darwin':
                        os.system("open " + filePath)
                    
                    utils.ClearConsole()
                    print(RESET + BYELLOW + "Output File has been opened, choose another option." + RESET + CYAN + "\n")
                
                #PyPacker
                elif MenuingInput == "pfiles": #datapack file creator
                    MenuingInput = "filecreate"
                    while validMain == "filecreate":
                        pass
                    
                elif MenuingInput == "pedit": #resourcepack file creator
                    print(RESET + BYELLOW + "launching RP file generator" + RESET + CYAN)
                    MenuingInput = "editors"
                    while validMain == "editors":
                        pass
                
                #Miscellaneous
                elif MenuingInput == "set": #settings page
                    
                    global RestartNess1
                    global RestartNess2
                    RestartNess1 = "(Entering any settings page will cause the need for a restart)"
                    RestartNess2 = "Back to Main Menu"
                    #a play on words, both "Restart Nessasary" and "Restartness" like "happiness"
                    
                    validMain = "settings"
                    utils.ClearConsole()
                    while validMain == "settings":
                        
                        if MissingFiles != []:
                            RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                            RestartNess2 = 'Restart PyPacker'
                            print(f'{BYELLOW}{WHITE}It seems like this is your first time using PyPacker, check these settings and type "quit" to continue.{RESET}')
                        
                        if SettingsData["DefaultFilepath"] == "local":
                            filePathDes = f"{filePath}, aka \"Local\""
                        else:
                            filePathDes = filePath
                        
                        if MenuingTemp == "":
                            MenuingInput = input(f'{BGREEN}{WHITE}PyPacker Settings: {BRED}{RestartNess1}{RESET}\n'
                                            f'{BGREEN}{WHITE}"{BRED}{WHITE}[N]{BGREEN}{WHITE}" means that setting is nessasary to run the program, changing any of these settings to an invalid value will cause a crash loop.{RESET}\n'
                                            f'{BGREEN}{WHITE}Fun Fact: For debug purposes, you can use this page as a intergrated terminal, although there may be issues when trying to scroll.{RESET}\n'
                                            
                                            f'\n{BGREEN}{WHITE}File Settings:{RESET}\n'
                                            f'{BWHITE}{BLACK}Output File > out (currently: {filePathDes}){BRED}{WHITE}[N]{RESET}\n'
                                            f'{BWHITE}{BLACK}Move or Copy Files > mocy (currently: {SettingsData["FileMovement"]}){BRED}{WHITE}[N]{RESET}\n'
                                            f'{BWHITE}{BLACK}Minecraft /assets Directory > dir (currently: {SettingsData["MinecraftDir"]}){RESET}\n'
                                            
                                            f'\n{BGREEN}{WHITE}Text Settings:{RESET}\n'
                                            f'{BWHITE}{BLACK}Show Debug Messages > debug (currently: {SettingsData["Debug"]}){BRED}{WHITE}[N]{RESET}\n'
                                            f'{BWHITE}{BLACK}Use ANSI+Unicode text > color (currently: {SettingsData["AnsiColorToggle"]}){BRED}{WHITE}[N]{RESET}\n'
                                            
                                            f'\n{BGREEN}{WHITE}Customization Settings:{RESET}\n'
                                            f'{BWHITE}{BLACK}Saved Default Version > ver (currently: {SettingsData["DefaultVersion"]}){BRED}{WHITE}[N]{RESET}\n'
                                            f'{BWHITE}{BLACK}Saved Default Edition > edi (currently: {SettingsData["DefaultEdition"]}){BRED}{WHITE}[N]{RESET}\n'
                                            f'{BWHITE}{BLACK}Text Editor > text (currently: {SettingsData["TextEditor"]}){RESET}\n'
                                            f'{BWHITE}{BLACK}Texture Editor > img (currently: {SettingsData["ImageEditor"]}){RESET}\n'
                                            f'{BWHITE}{BLACK}Audio Editor> audio (currently: {SettingsData["AudioEditor"]}){RESET}\n'
                                            
                                            f'\n{BGREEN}{WHITE}Miscellaneous:{RESET}\n'
                                            f'{BWHITE}{BLACK}Open settings.json > open (Useful for manual tinkering){RESET}\n'
                                            f'{BWHITE}{BLACK}Reset Everything > reset (NONFUNCTIONAL) (Use when the program is having issues or you\'re planning to update, reset options inside){RESET}\n\n'
                                            
                                            f'{BWHITE}{BLACK}{RestartNess2} > quit {RESET}\n'
                                            f'{BWHITE}{BLACK}Restart PyPacker > res {RESET}\n'
                                            f'{CYAN}\n')
                        else:
                            MenuingInput = MenuingTemp
                            MenuingTemp = ""
                        
                        #File
                        if MenuingInput == "out":
                            FilePathSettings = 0
                            utils.ClearConsole()
                            validMain = "choose out"
                            while validMain == "choose out":
                                
                                SettingsTemp = input(f'{BYELLOW}{WHITE}Input the filepath to your chosen output file ("quit" to abort, "local" for the output file in this programs dir){RESET}\n\n{CYAN}')
                                if SettingsTemp != "quit":
                                    
                                    if SettingsTemp == "local":
                                            print(f'{BYELLOW}{WHITE}Your chosen filepath exists and has been added to the settings file{RESET}\n\n')
                                            FilePathSettings = 1
                                    
                                    elif bool(os.path.exists(SettingsTemp)) == True:  
                                        print(f'{BYELLOW}{WHITE}Your chosen filepath exists and has been added to the settings file{RESET}\n\n')
                                        FilePathSettings = 1
                                
                                    else:
                                        pass
                                    
                                if FilePathSettings == 1:
                                    SettingsData["DefaultFilepath"] = SettingsTemp         
                                    utils.EditSettings("DefaultFilepath", SettingsTemp)
                                    RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                                    RestartNess2 = 'Restart PyPacker'
                                            
                                validMain = "settings"
                                utils.ClearConsole()
                            
                        elif MenuingInput == "mocy":
                            utils.ClearConsole()
                            validMain = "choose mode"
                            while validMain == "choose mode":
                                SettingsTemp = input(f'{BGREEN}{WHITE}Move, Copy, or Choose? (case sensitive){RESET}\n'
                                                    f'{BWHITE}{BLACK}Move: Moves Files when they are chosen to be added to a Resource Pack.{RESET}\n'
                                                    f'{BWHITE}{BLACK}Copy: Copies Files when they are chosen to be added to a Resource Pack.{RESET}\n'
                                                    f'{BWHITE}{BLACK}Choose: You can choose between either choice whenever you add a new file.{RESET}\n'
                                                    f'{BWHITE}{BLACK}Enter your choice below or enter "quit" to go back to Settings{RESET}\n\n'
                                                    f'{CYAN}')

                                if SettingsTemp != "quit":
                                    if SettingsTemp == "Move" or "Copy" or "Choose":
                                        utils.EditSettings("FileMovement", SettingsTemp)
                                        print(f'{BYELLOW}{WHITE}Your choice has been added to the settings file{RESET}\n\n')
                                    else:
                                        print(f'{RESET}{RED}Invalid argument. Please send a valid input.\n{RESET}\n')
                                
                                RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                                RestartNess2 = 'Restart PyPacker'        
                                validMain = "settings"
                                utils.ClearConsole()
                                
                        elif MenuingInput == "dir":
                            utils.ClearConsole()
                            validMain = "MCdir"
                            SetNewSettings = 0
                            LeaveScreen = 0
                            while validMain == "MCdir":
                                utils.ClearConsole()
                                SettingsTemp = ""
                                SettingsTemp = input(f'{BGREEN}{WHITE}Minecraft Assets Directory{RESET}\n'
                                                    f'{BWHITE}{BLACK}Auto Dectect: PyPacker will try and dectect your Java Minecraft instalation.{RESET}\n' 
                                                    f'{BWHITE}{BLACK}It can\'t auto detect other launchers like PolyMC, MultiMC, or GDlaucnher, instead goes straight for your \".minecraft\" folder.{RESET}\n'
                                                    f'{BWHITE}{BLACK}Manual Input: You can also input the filepath to a custom instalation "assets" folder {RESET}\n' 
                                                    f'{BWHITE}{BLACK}It can detect other launchers like Prism Launcher, MultiMC, or GDlaucnher\n{RESET}'
                                                    f'{BWHITE}{BLACK}(This program will refuse to link to TLauncher, PolyMC, or any other Cracked/questionable launchers){RESET}\n' 
                                                    f'{BWHITE}{BLACK}Type "auto" to Detect, "manu" for Manual, or "quit" to abort.{RESET}\n'
                                                    f'{CYAN}\n')
                                LeaveScreen = 0
                                if SettingsTemp != "quit":
                                    if SettingsTemp == "auto":
                                        if bool(os.path.exists(MCDir := os.path.join(os.environ["APPDATA"], ".minecraft"))) == True:
                                            input(f'{BWHITE}{BLACK}That filepath exists and has been set as the output filepath. Press enter to contiue.{RESET}\n\n')
                                            SetNewSettings = 1
                                            LeaveScreen = 1
                                        else:
                                            input(f'{RESET}{RED}It seems Minecraft Java is not installed. If it is but PyPacker can\'t detect it, try setting it manually.\nPress enter to continue{RESET}\n')
                                    elif SettingsTemp == "manu":
                                        SettingsTemp = input(f'{BWHITE}{BLACK}Paste the filepath to your chosen launcher and press enter.{RESET}\n\n')
                                        if bool(os.path.exists(SettingsTemp)) == True:
                                            input(f'{BWHITE}{BLACK}That filepath exists and has been set as the output filepath. Press enter to contiue.{RESET}\n\n')
                                            MCDir = SettingsTemp
                                            SetNewSettings = 1
                                            LeaveScreen = 1
                                        else:
                                            input(f'{RESET}{RED}That is not a valid filepath Press enter to continue{RESET}\n')
                                
                                    if SetNewSettings == 1:
                                        SettingsData["MinecraftDir"] = MCDir
                                        utils.EditSettings("MinecraftDir", MCDir)
                                else:
                                    LeaveScreen = 1
                                
                                if LeaveScreen == 1:
                                    RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                                    RestartNess2 = 'Restart PyPacker'
                                    validMain = "settings"
                                    utils.ClearConsole()
                                
                        #Text        
                        elif MenuingInput == "debug":
                            utils.ClearConsole()
                            validMain = "debug toggle"
                            while validMain == "debug toggle":
                                SettingsTemp = ""
                                SettingsTemp = input(f'{BWHITE}{BLACK}Debug mode will cause some minor graphical issues but is overall useful if you plan\non messing with this projects code or the settings file.{RESET}\n' 
                                                    f"{BYELLOW}{WHITE}This is meant for devs, github contributors, and people who know what they're doing only.{RESET}\n"
                                                    f'{BWHITE}{BLACK}Type "true" to turn it on, "false" to turn it off, "quit" to abort.{RESET}\n'
                                                    f'{CYAN}\n')
                                
                                if SettingsTemp == "quit":
                                    pass
                                elif SettingsTemp == "true" or "false":
                                    utils.EditSettings("Debug", SettingsTemp)
                                    print(f'{BYELLOW}{WHITE}Your choice has been added to the settings file{RESET}\n\n')
                                else:
                                    print(f'{RESET}{RED}Invalid argument. Please send a valid input.\n{RESET}\n')
                                
                                RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                                RestartNess2 = 'Restart PyPacker'
                                validMain = "settings"
                                utils.ClearConsole()
                                
                        elif MenuingInput == "color":
                            utils.ClearConsole()
                            validMain = "color toggle"
                            while validMain == "color toggle":
                                SettingsTemp = ""
                                SettingsTemp = input(f'{BWHITE}{BLACK}Toggle the ANSII/Unicode encoding for ancient terminals{RESET}\n' 
                                                    f"{BYELLOW}{WHITE}It is not reccomended to toggle this setting.{RESET}\n"
                                                    f'{BWHITE}{BLACK}Type "true" to turn it on, "false" to turn it off, "quit" to abort.{RESET}\n'
                                                    f'{CYAN}\n')
                                
                                if SettingsTemp == "quit":
                                    pass
                                elif SettingsTemp == "true" or "false":
                                    utils.EditSettings("AnsiColorToggle", SettingsTemp)
                                    print(f'{BYELLOW}{WHITE}Your choice has been added to the settings file{RESET}\n\n')
                                else:
                                    print(f'{RESET}{RED}Invalid argument. Please send a valid input.\n{RESET}\n')
                                
                                RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                                RestartNess2 = 'Restart PyPacker'
                                validMain = "settings"
                                utils.ClearConsole()
                        
                        #Customization
                        elif MenuingInput == "ver":
                            utils.ClearConsole()
                            validMain = "ver id"
                            while validMain == "ver id":
                                SettingsTemp = ""
                                SettingsTemp = input(f'{BGREEN}{WHITE}Change Default Minecraft Version{RESET}\n' 
                                                    f'{BWHITE}{BLACK}Type any version from 1.13 to 1.19.2 to set as default{RESET}\n{BWHITE}{BLACK}(not including snapshots, in that case use the nearest release version by date, then trail and error.){RESET}\n'
                                                    f'{CYAN}\n')
                                if SettingsTemp != "quit":
                                    if SettingsTemp in MineVersions:
                                        utils.EditSettings("", 0, SettingsTemp)
                                        input(f'{BYELLOW}{WHITE}You Chose: {SettingsTemp}, hit Enter to continue.{RESET}\n')
                                        validMain = "settings"
                                        RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                                        RestartNess2 = 'Restart PyPacker'
                                    else:
                                        print(f"{RESET}{RED}Invalid argument. Please send a valid input.\n{RESET}\n")
                                validMain = "settings"
                                RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                                RestartNess2 = 'Restart PyPacker'
                        
                        elif MenuingInput == "edi":
                            pass
                                
                        elif MenuingInput == "text":
                            pass
                        
                        elif MenuingInput == "img":
                            pass
                        
                        elif MenuingInput == "audio":
                            pass
                        
                        #Miscellaneous
                        elif MenuingInput == "open":
                            if sys.platform=='win32':
                                os.system(SettingsData["TextEditor"] + utils.LocalFiles() + "\settings.json")

                            #if sys.platform=='darwin':
                            #    os.system("cat" + utils.LocalFiles("") + "\settings.json")
                        
                            RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                            RestartNess2 = 'Restart PyPacker'
                        
                        elif MenuingInput == "reset":
                            
                            ReallyList = [" sure ", " really sure ", " REALLY sure ", " REALLY REALLY SURE ", " REAL FUCKIN SURE "] #space are there for a reason, dont remove them
                            ReallyCounter = 0
                            #i spent 15 minutes on this funni dont ruin it please
                            
                            GitIsInstalled = subprocess.getoutput("git --version")
                            if "version" not in GitIsInstalled:
                                CanRunReset = "can not safely reset.\n\nYou have two options:\nVisit the PyPacker Github page and grab the lastest release manually > Py\nDownload Git > Git"
                                GitIsInstalled = "Not Installed!"
                            else:
                                CanRunReset = "can safely reset."
                            
                            utils.ClearConsole()
                            validMain = "reset"
                            while validMain == "reset":
                                SettingsTemp = input(f'{BGREEN}{WHITE}Reset All Files?{RESET}\n'
                                                    f'{BWHITE}{BLACK}Delete Settings, and \\assets files, then regenerates. Simple refresh, can be done without Git installed. > upd{RESET}\n'
                                                    f'{BWHITE}{BLACK}The "Update" option, but adds the main script file. Soft Reset > most{RESET}\n'
                                                    f'{BWHITE}{BLACK}Wipe everything in this directory except for a update script, then clones this project from Github. Hard reset. > everything{RESET}\n'
                                                    f'{BWHITE}{BLACK}Go back to settings menu > quit{RESET}\n\n'
                                                    f'{BRED}{WHITE}Warning:{BWHITE}{BLACK} the program \"Git\" is required to be installed to use its commands to clone to repository to this folder.{RESET}\n'
                                                    f'{BWHITE}{BLACK}If you have no idea what that means, thats ok, we\'ll handle it from here.{RESET}\n'
                                                    f'{BWHITE}{BLACK}Your version of Git is: "{GitIsInstalled}" and {CanRunReset}{RESET}\n'
                                                    f'{CYAN}\n')

                                if SettingsTemp != "quit":
                                    if SettingsTemp == "upd":
                                        SettingsTemp = [utils.LocalFiles("") + r"\settings.json", utils.LocalFiles("") + r"\assets"]
                                        
                                    if CanRunReset == "can safely reset.":
                                              
                                        if SettingsTemp == "most":
                                            SettingsTemp = [utils.LocalFiles("") + r"\settings.json", utils.LocalFiles("") + r"\localization", utils.LocalFiles("") + r"\assets", ]
                                            GrabWithGit = [utils.LocalFiles("") + r"\localization", ]
                                            
                                        elif SettingsTemp == "everything":
                                            SettingsTemp = [utils.LocalFiles("") + r"\settings.json", utils.LocalFiles("") + r"\localization", utils.LocalFiles("") + r"\assets",]
                                            
                                        while ReallyCounter < len(ReallyList):
                                            FinalResetCheck = input(f'{BYELLOW}{WHITE}Are you{ReallyList[ReallyCounter]}you want to reset? y/n{RESET}\n\n')
                                            if FinalResetCheck != "y":
                                                break
                                            else:
                                                ReallyCounter+=1
                                    else:
                                        utils.ClearConsole("")
                                        print(f'{RESET}{RED}Git is not installed, you can\'t use that comamnd{RESET}\n')
                                        
                                    if ReallyCounter == len(ReallyList):
                                        input(f"{BRED}{WHITE}Press enter to delete, alt+f4 to abort.{RESET}\n")
                                        utils.DeleteStuff(SettingsTemp)

                                input(f"{BWHITE}{BLACK}Reset Aborted. Press enter to continue.{RESET}")        
                                validMain = "settings"
                                utils.ClearConsole()
                                
                        #Standard    
                        elif MenuingInput == "quit":
                            if RestartNess2 != "Back to Main Menu":
                                print(f'{BYELLOW}{WHITE}These are your new settings:{SettingsData}{RESET}')
                                input(RESET + BYELLOW + "Press enter to restart PyPacker." + RESET + "\n")
                                utils.ClearConsole()
                                os.startfile(sys.argv[0])
                                sys.exit()
                            else:
                                utils.ClearConsole()
                                validMain = "mainmenu"
                      
                        elif MenuingInput == "res":
                            input(RESET + BYELLOW + "Press enter to restart PyPacker." + RESET + "\n")
                            utils.ClearConsole()
                            os.startfile(sys.argv[0])
                            sys.exit()
                        
                        elif MenuingInput == "crash": #only for debug, hiden from print statement
                            raise Exception("Intentional Crash")
                        
                        elif MenuingInput == "":
                            utils.ClearConsole()
                                        
                        else:
                            utils.ClearConsole()
                            print(f"{BWHITE}{BLACK}PyPacker Intergrated Terminal:{RESET}\n\n")
                            print(f"{subprocess.getoutput(MenuingInput)}\n\n")
                            input(f"{BWHITE}{BLACK}Press Enter to continue.{RESET}{CYAN}\n\n")
                            utils.ClearConsole()
                
                elif MenuingInput == "link":
                    utils.ClearConsole()
                    validMain = "links"
                    while validMain == "links":
                        if MenuingTemp == "":
                            MenuingInput = input(f"{BGREEN}{WHITE}External Links:{RESET}\n"
                                            f'{BGREEN}{WHITE}Project Links:{RESET}\n'
                                            f'{BWHITE}{BLACK}PyPacker Github > git {RESET}\n'
                                            
                                            f'\n{BGREEN}{WHITE}Other Links:{RESET}\n'
                                            f'{BWHITE}{BLACK}Carpet Mod Github > car {RESET}\n'
                                            f'{BWHITE}{BLACK}Scarpet Docs > scar {RESET}\n'
                                            
                                            f'\n{BGREEN}{WHITE}Inspiration:{RESET}\n'
                                            f'{BWHITE}{BLACK}DataPackGen > dpg {RESET}\n'
                                            f'{BWHITE}{BLACK}DataCreate.py > dcp {RESET}\n'
                                            
                                            f'\n{BGREEN}{WHITE}Contributer links: (to contributers: only add if you plan to help out with docs/support or contribute more than just code){RESET}\n'
                                            f'{BWHITE}{BLACK}Blurple\'s Twitter > twit_1 (May post updates here){RESET}\n'
                                            f'{BWHITE}{BLACK}Blurple\'s Discord Server > disc_1 (If you have any specific questions, join this and i\'ll help you out){RESET}\n'
                                            
                                            f'\n{BWHITE}{BLACK}Main Menu > quit {RESET}\n'
                                            f'{CYAN}\n\n')
                        else:
                            MenuingInput = MenuingTemp
                            MenuingTemp = ""
                        
                        if MenuingInput == "git":
                            webbrowser.open("https://github.com/GirlInPurple/Py-Packer")
                            utils.ClearConsole()
                        elif MenuingInput == "twit_1":
                            webbrowser.open("https://twitter.com/blurpl3d")
                            utils.ClearConsole()
                        elif MenuingInput == "disc_1":
                            webbrowser.open("https://discord.gg/2PxCfY9jRd")
                            utils.ClearConsole()
                        elif MenuingInput == "car":
                            webbrowser.open("https://github.com/gnembon/fabric-carpet")
                            utils.ClearConsole()
                        elif MenuingInput == "scar":
                            webbrowser.open("https://github.com/gnembon/fabric-carpet/blob/master/docs/scarpet/Documentation.md")
                            utils.ClearConsole()
                        elif MenuingInput == "dpg":
                            webbrowser.open("https://misode.github.io/")
                            utils.ClearConsole()
                        elif MenuingInput == "dcp":
                            webbrowser.open("https://github.com/OrigamingWasTaken/DataCreate")
                            utils.ClearConsole()
                        elif MenuingInput == "quit":
                            validMain = "mainmenu"
                            utils.ClearConsole()
                        elif MenuingInput == "": #fixes a stupid bug that spams the custom error below
                            utils.ClearConsole()
                        else:
                            utils.ClearConsole()
                            print(f"{RESET}{RED}Invalid argument. Please send a valid input.\n{RESET}\n")
                
                #Standard                
                elif MenuingInput == "quit": #closes the program
                    input(RESET + BYELLOW + "Press enter to quit." + RESET + "\n")
                    utils.ClearConsole()
                    sys.exit()
                
                elif MenuingInput == "res": #closes the program
                    input(RESET + BYELLOW + "Press enter to restart PyPacker." + RESET + "\n")
                    utils.ClearConsole()
                    os.startfile(sys.argv[0])
                    sys.exit()
                
                elif MenuingInput == "": #fixes a stupid bug that spams the custom error below
                    utils.ClearConsole()
                                
                else:
                    utils.ClearConsole()
                    print(f"{RESET}{RED}Invalid argument. Please send a valid input.\n{RESET}\n")

    if __name__ == "__main__":
        
        global MineVersions 
        MineVersionsDatapack = { #Every MC version datapack id
            "1.13":"4",
            "1.13.1":"4",
            "1.13.2":"4",
            "1.14":"4",
            "1.14.1":"4",
            "1.14.2":"4",
            "1.14.3":"4",
            "1.14.4":"4",
            "1.15":"5",
            "1.15.1":"5",
            "1.15.2":"5",
            "1.16":"5",
            "1.16.1":"5",
            "1.16.2":"6",
            "1.16.3":"6",
            "1.16.4":"6",
            "1.16.5":"6",
            "1.17":"7",
            "1.17.1":"7",
            "1.18":"8",
            "1.18.1":"8",
            "1.18.2":"9",
            "1.19":"10",
            "1.19.1":"10",
            "1.19.2":"10",
            "1.19.3":"10"
        }
        MineVersionsResourcepack = { #Every MC version resourcepack id (THIS IS OUTDATED AND MOST LIKELY WRONG)
            "1.13":"4",
            "1.13.1":"4",
            "1.13.2":"4",
            "1.14":"4",
            "1.14.1":"4",
            "1.14.2":"4",
            "1.14.3":"4",
            "1.14.4":"4",
            "1.15":"5",
            "1.15.1":"5",
            "1.15.2":"5",
            "1.16":"5",
            "1.16.1":"5",
            "1.16.2":"6",
            "1.16.3":"6",
            "1.16.4":"6",
            "1.16.5":"6",
            "1.17":"7",
            "1.17.1":"7",
            "1.18":"8",
            "1.18.1":"8",
            "1.18.2":"9",
            "1.19":"10",
            "1.19.1":"10",
            "1.19.2":"10",
            "1.19.3":"12"
        }
        
        if sys.platform == "win32":
            os.system('mode con: cols=135 lines=50')
            ctypes.windll.kernel32.SetConsoleTitleW(f'PyPacker: "{SplashText}"')
            
        os.system("") #activate ANSI coloring
        main = main() #for __init__()
        main.main() #everything else
        
except Exception as ex: #"better" error handling
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    ExTemp = input(f"{RESET}\n\n{BWHITE}{BLACK}PyPacker has encountered a serious error and has crashed:{RESET}\n"
                   f"{BYELLOW}{WHITE}{ex}{RESET}\n"
                   f"{RESET}{BWHITE}{BLACK}Here is a little more Info:{RESET}\n"
                   f"{BYELLOW}{WHITE}Type: {exc_type}{RESET}\n" 
                   f"{BYELLOW}{WHITE}File: {fname}{RESET}\n" 
                   f"{BYELLOW}{WHITE}Line: {exc_tb.tb_lineno}{RESET}\n"
                   f"{BWHITE}{BLACK}Press enter to restart PyPacker, or type \"Exit\" to exit.{RESET}\n\n")
    if ExTemp != "exit":
        os.startfile(sys.argv[0])
        sys.exit()
    else:
        sys.exit()