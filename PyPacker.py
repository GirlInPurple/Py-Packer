import sys, os, re, time, ctypes, webbrowser, urllib.request #all built in, convenient
os.system("") #why does this fix ANSI color coding? god only knows, i have no clue

#window customisation, breaks VScode
os.system('mode con: cols=130 lines=50')
if sys.platform == "win32":
    ctypes.windll.kernel32.SetConsoleTitleW("PyPacker") #rename console window, thx stackoverflow

class utils: #startup and other universal utils
    def __init__(self):
        pass

    global mineVersions
    mineVersions = { #Every MC version this is compatable with
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
        "1.19.2":"10"
    }
    
    def LocalFiles(self):
        return os.path.dirname(os.path.realpath(__file__))

    def append_mkdir(self, dir):
        try:
            os.mkdir(dir)
        except:
            tryPathTemp = 0
            while tryPathTemp >= 0:
                try:
                    os.mkdir(dir + "_" + str(tryPathTemp))
                    break
                except:
                    tryPathTemp += 1
    
    def ClearConsole():
        if sys.platform=='win32':
            os.system('cls')

        if sys.platform=='darwin':
            os.system('clear')
            
    def EditSettings(self, pos, value):
        settings[pos] = value
        with open(openTXT, "w") as appendSettings:
            appendSettings.write(settings[0] + "\n" + settings[1] + "\n" + settings[2] + "\n" + settings[3] + "\n" + settings[4] + "\n" + settings[5] + "\n" + settings[6] + "\n" + settings[7] + "\n" + settings[8])
            appendSettings.close()
        
class main: #the main program
    def __init__(self):
        
        global BLACK
        global RED
        global BRED
        global GREEN
        global BGREEN
        global YELLOW
        global BYELLOW
        global BLUE
        global MAGENTA
        global BMAGENTA
        global CYAN
        global WHITE
        global BWHITE
        global RESET
        global BOLD
        global UNDERLINE
        
        data = []
        global settings
        settings = []

        global openTXT
        openTXT = utils.LocalFiles(self) + "\settings.txt"   
        
        with open(openTXT,"r") as f:
            data = f.readlines() #readlines() returns a list of items in said file

        for i in range(0, len(data)): #list loop, the console is (unintentionally) spammed for a bit
            settings.append(data[i].strip('\n'))
            
        f.close()
        
        #settings handlers:
        if settings[3] != "False":
            print(f"{BYELLOW}{WHITE}start debug messages:\n{openTXT}\n{data}\n{settings}{RESET}")
        
        #debug
        global txtlocations
        if settings[3] == "True":
            txtlocations = ["(txtlocation: line 1)", "(txtlocation: line 2)", "(txtlocation: line 3)", "(txtlocation: line 4)", "(txtlocation: line 5)", "(txtlocation: line 6)", "(txtlocation: line 7)", "(txtlocation: line 8)", "(txtlocation: line 9)"]
        else:
            txtlocations = ['','','','','','','','','',]
        
        #colors
        if settings[4] == "True":
            BLACK, RED, BRED, GREEN, BGREEN, YELLOW, BYELLOW, BLUE, MAGENTA, BMAGENTA, CYAN, WHITE, BWHITE, RESET, BOLD, UNDERLINE = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
        
        #version
        if settings[0] in mineVersions:
            if settings[3] != "False":
                print(f'set default version to: {settings[0]}')
        else:
            settings[0] = "1.19.2"
            print(f"error while setting default version, setting to 1.19.2 as a default, maybe the version you picked isn't compatable with this version of PyPacker or input wrong?")
        
        #filepath
        global filePath
        if settings[1] != "local":
            if bool(os.path.exists(settings[1])) == True:
                filePath = settings[1]
                if settings[3] != "False":
                    print(f"chosen filepath: {filePath}")
        else:
            filePath = utils.LocalFiles(self) + "\output"
            if settings[3] != "False":
                print(f'output filepath set to "local", aka: {filePath}')
   
        if settings[3] != "False":
            print(f"{BYELLOW}{WHITE}end debug messages\n{RESET}")
        
    def main():
        
        print(f'{BGREEN}Welcome to PyPacker! Where would you like to start?\n(All commands case sensitve; "open" and "out" not guaranteed to work on all Lunix distros){RESET}')
        
        validMain = "mainmenu"
        while validMain == "mainmenu":
            if settings[8] != "0":
                lastMain = input(f"{BGREEN}{WHITE}PyPacker Main Menu{RESET}\n"
                                f"{BWHITE}{BLACK}Open Program Folder > open {RESET}\n"
                                f"{BWHITE}{BLACK}Open Output Folder > out {RESET}\n"
                                f"{BWHITE}{BLACK}Settings Menu > set {RESET}\n"
                                f"{BWHITE}{BLACK}External Links > link {RESET}\n"
                                f"{BWHITE}{BLACK}File Generators > files {RESET}\n"
                                f"{BWHITE}{BLACK}Pack Editors > edit {RESET}\n"
                                f"{BWHITE}{BLACK}Quit PyPacker > quit {RESET}\n"
                                f"{BWHITE}{BLACK}Restart PyPacker > restart {RESET}\n\n"
                                f"{CYAN}") #the input text will be cyan, also really easy to add extra stuff to
            else:
                lastMain = "set"
        
            if lastMain == "open": #opens the program file location
                if sys.platform=='win32':
                    os.system("start " + utils.LocalFiles(""))

                if sys.platform=='darwin':
                    os.system("open " + utils.LocalFiles(""))

                print(RESET + BYELLOW + "Program File has been opened, choose another option." + RESET + CYAN + "\n")
                utils.ClearConsole()
                
            elif lastMain == "out": #attempts to open the program output file location
                if sys.platform=='win32':
                    os.system("start " + filePath)

                if sys.platform=='darwin':
                    os.system("open " + filePath)

                print(RESET + BYELLOW + "Output File has been opened, choose another option." + RESET + CYAN + "\n")
                utils.ClearConsole()
                
            elif lastMain == "set": #settings page
                
                global RestartNess1
                global RestartNess2
                RestartNess1 = ""
                RestartNess2 = "Back to Main Menu"
                
                validMain = "settings"
                while validMain == "settings":
                    utils.ClearConsole()
                    
                    if settings[8] == "0":
                        RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                        RestartNess2 = 'Restart PyPacker'
                        print(f'{BYELLOW}{WHITE}It seems like this is your first time using PyPacker, check these settings and type "quit" to continue.{RESET}')
                    
                    lastMain = input(f'{BGREEN}{WHITE}PyPacker Settings{BRED}{RestartNess1}{RESET}\n{BGREEN}{WHITE}("{BRED}{WHITE}[N]{BGREEN}{WHITE}" means that setting is nessasary to run the program.){RESET}\n'
                                    f'{BGREEN}{WHITE}File Settings:{RESET}\n'
                                    f'{BWHITE}{BLACK}Output File > out (currently: {filePath}){txtlocations[1]}{BRED}{WHITE}[N]{RESET}\n'
                                    f'{BWHITE}{BLACK}Move or Copy Files > mocy (currently: {settings[2]}){txtlocations[2]}{BRED}{WHITE}[N]{RESET}\n'
                                    #f'{BWHITE}{BLACK}Minecraft /assets Directory > dir (currently: ){txtlocations[]}{RESET}\n' depricated option
                                    
                                    f'{BGREEN}{WHITE}Text Settings:{RESET}\n'
                                    f'{BWHITE}{BLACK}Show Debug Messages > debug (currently: {settings[3]}){txtlocations[3]}{BRED}{WHITE}[N]{RESET}\n'
                                    f'{BWHITE}{BLACK}Disable ANSI+Unicode text > color (currently: {settings[4]}){txtlocations[4]}{BRED}{WHITE}[N]{RESET}\n'
                                    
                                    f'{BGREEN}{WHITE}Customization Settings:{RESET}\n'
                                    f'{BWHITE}{BLACK}Saved Default Version > ver (currently: {settings[0]}){txtlocations[0]}{BRED}{WHITE}[N]{RESET}\n'
                                    f'{BWHITE}{BLACK}Text Editor > text (currently: {settings[5]}){txtlocations[5]}{RESET}\n'
                                    f'{BWHITE}{BLACK}Texture Editor > img (currently: {settings[6]}){txtlocations[6]}{RESET}\n'
                                    f'{BWHITE}{BLACK}Audio Editor> audio (currently: {settings[7]}){txtlocations[7]}{RESET}\n'
                                    
                                    f'{BGREEN}{WHITE}Miscellaneous:{RESET}\n'
                                    f'{BWHITE}{BLACK}Open Settings.TXT > open (useful for manual tinkering){RESET}\n'
                                    f'{BWHITE}{BLACK}In-Depth Explantion > exp {RESET}\n'
                                    f'{BWHITE}{BLACK}{RestartNess2} > quit {RESET}\n\n'
                                    f'{CYAN}')
                    
                    if lastMain == "out":
                        FilePathSettings = 0
                        utils.ClearConsole()
                        validMain = "choose out"
                        while validMain == "choose out":
                            SettingsTemp = input(f'{BYELLOW}{WHITE}Input the filepath to your chosen output file ("quit" to abort, "local" for the output file in this programs dir){RESET}\n\n{CYAN}')
                            if SettingsTemp != "quit":
                                
                                if bool(os.path.exists(SettingsTemp)) == True:  
                                    print(f'{BYELLOW}{WHITE}Your chosen filepath exists and has been added to the settings file{RESET}\n\n')
                                    FilePathSettings = 1
                                    
                                elif SettingsTemp == "local":
                                        print(f'{BYELLOW}{WHITE}Your chosen filepath exists and has been added to the settings file{RESET}\n\n')
                                        FilePathSettings = 1
                                else:
                                    pass
                            if FilePathSettings == 1:            
                                utils.EditSettings("", 1, SettingsTemp)
                                
                            RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                            RestartNess2 = 'Restart PyPacker'        
                            validMain = "settings"
                        
                    elif lastMain == "mocy":
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
                                    utils.EditSettings("", 2, SettingsTemp)
                                    print(f'{BYELLOW}{WHITE}Your choice has been added to the settings file{RESET}\n\n')
                                else:
                                    print(f'{RESET}{RED}Invalid argument. Please send a valid input.\n{RESET}\n')
                            
                            RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                            RestartNess2 = 'Restart PyPacker'        
                            validMain = "settings"
                            
                    elif lastMain == "dir": #depricated option
                    #    utils.ClearConsole()
                    #    validMain = "MC dir"
                    #    while validMain == "MD dir":
                    #        SettingsTemp = ""
                    #        SettingsTemp = input(f'{BGREEN}{WHITE}Minecraft Assets Directory{RESET}\n'
                    #                             f'{BWHITE}{BLACK}Auto Dectect: PyPacker will try and dectect you Java Minecraft instalation.{RESET}\n' 
                    #                             f'{BWHITE}{BLACK}It can not detect other launchers like PolyMC, MultiMC, or GDlaucnher.{RESET}\n'
                    #                             f'{BWHITE}{BLACK}Manual Input: You can also input the filepath to a custom instalation "assets" folder {RESET}\n' 
                    #                             f'{BWHITE}{BLACK}It can detact other launchers like PolyMC, MultiMC, or GDlaucnher, as long as PyPacker has admin permision to do so.{RESET}\n' 
                    #                             f'{BWHITE}{BLACK}Type "auto" to Detect, "manu" for Manual, or "quit" to abort.{RESET}\n'
                    #                             f'{CYAN}\n')
                    #        
                    #        if SettingsTemp == "quit":
                    #            RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                    #            RestartNess2 = 'Restart PyPacker'
                    #            validMain = "settings"
                    #        elif SettingsTemp == "auto":
                        pass
                    
                    elif lastMain == "debug":
                        utils.ClearConsole()
                        validMain = "debug toggle"
                        while validMain == "debug toggle":
                            SettingsTemp = ""
                            SettingsTemp = input(f'{BWHITE}{BLACK}Debug mode will cause some minor graphical issues but is overall useful if you plan\non messing with this projects code or the settings file.{RESET}\n' 
                                                 f"{BYELLOW}{WHITE}This is meant for devs, github contributors, and people who know what they're doing only.{RESET}\n"
                                                 f'{BWHITE}{BLACK}Type "True" to turn it on, "False" to turn it off, "quit" to abort.{RESET}\n'
                                                 f'{CYAN}\n')
                            
                            if SettingsTemp == "quit":
                                pass
                            elif SettingsTemp == "True" or "False":
                                utils.EditSettings("", 3, SettingsTemp)
                                print(f'{BYELLOW}{WHITE}Your choice has been added to the settings file{RESET}\n\n')
                            else:
                                print(f'{RESET}{RED}Invalid argument. Please send a valid input.\n{RESET}\n')
                            
                            RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                            RestartNess2 = 'Restart PyPacker'
                            validMain = "settings"
                            
                    elif lastMain == "color":
                            RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                            RestartNess2 = 'Restart PyPacker'
                            print("")
                    
                    elif lastMain == "ver":
                        utils.ClearConsole()
                        validMain = "ver id"
                        while validMain == "ver id":
                            SettingsTemp = ""
                            SettingsTemp = input(f'{BGREEN}{WHITE}Change Default Minecraft Version{RESET}\n' 
                                                 f'{BWHITE}{BLACK}Type any version from 1.13 to 1.19.2 to set as default{RESET}\n{BWHITE}{BLACK}(not including snapshots, in that case use the nearest release version by date, then trail and error.){RESET}\n'
                                                 f'{CYAN}\n')
                            if SettingsTemp != "quit":
                                if SettingsTemp in mineVersions:
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
                            
                    elif lastMain == "text":
                        pass
                    
                    elif lastMain == "img":
                        pass
                    
                    elif lastMain == "audio":
                        pass
                    
                    elif lastMain == "quit":
                        if RestartNess2 != "Back to Main Menu":
                            print(f'{BYELLOW}{WHITE}These are your new settings:{settings}{RESET}')
                            input(RESET + BYELLOW + "Press enter to restart PyPacker." + RESET + "\n")
                            utils.ClearConsole()
                            if settings[8] == "0":
                                utils.EditSettings("", 8, "1")
                            os.startfile(sys.argv[0])
                            sys.exit()
                        else:
                            utils.ClearConsole()
                            validMain = "mainmenu"
                    
                    elif lastMain == "open":
                        if sys.platform=='win32':
                            os.system(openTXT)

                        if sys.platform=='darwin':
                            os.system("cat" + openTXT)
                    
                        RestartNess1 = '(A restart is nessasary for these changes to take place. Enter "quit" to continue)'
                        RestartNess2 = 'Restart PyPacker'
                    
                    elif lastMain == "exp":
                        utils.ClearConsole()
                        input(f'{BGREEN}{WHITE}Settings.TXT Manual editing explantion: (first number is line in file, second number is line when processed,{RESET}\n{BGREEN}{WHITE}notes about each line are on the right){RESET}\n'
                              f'{BWHITE}{BLACK}Line 1, 0: Saved Version (From 1.13 to 1.19.2, no snapshots){RESET}\n'
                              f'{BWHITE}{BLACK}Line 2, 1: Output File (Must be a valid file to be accepted){RESET}\n'
                              f'{BWHITE}{BLACK}Line 3, 2: Move or Copy when making Resource Packs{RESET}\n'
                              f'{BWHITE}{BLACK}Line 4, 3: Debug Mode{RESET}\n'
                              f'{BWHITE}{BLACK}Line 5, 4: Disable ANSI/Unicode Coloring (useful if ANSI coding breaks custom terminals){RESET}\n'
                              f'{BWHITE}{BLACK}Line 6, 5: Default Text Editor (these last 3 have to be in Powershell/SUDO command form due to how PyPacker opens files){RESET}\n'
                              f'{BWHITE}{BLACK}Line 7, 6: Default Texture Editor{RESET}\n'
                              f'{BWHITE}{BLACK}Line 8, 7: Default Audio Editor{RESET}\n'
                              f'{BWHITE}{BLACK}Press enter to continue.{RESET}\n'
                              f'{CYAN}\n')
                    
                    elif lastMain == "restart":
                        input(RESET + BYELLOW + "Press enter to restart PyPacker." + RESET + "\n")
                        utils.ClearConsole()
                        os.startfile(sys.argv[0])
                        sys.exit()
                    
                    elif lastMain == "":
                        utils.ClearConsole()
                                    
                    else:
                        utils.ClearConsole()
                        print(f"{RESET}{RED}Invalid argument. Please send a valid input.\n{RESET}\n")
            
            elif lastMain == "link":
                utils.ClearConsole()
                validMain = "links"
                while validMain == "links":
                    lastMain = input(f'{BGREEN}{WHITE}Project Links:{RESET}\n'
                                    f'{BWHITE}{BLACK}PyPacker Github > git {RESET}\n'
                                    f'{BWHITE}{BLACK}My Twitter > twit {RESET}\n'
                                    f'{BWHITE}{BLACK}Discord Server > disc {RESET}\n'
                                    f'{BGREEN}{WHITE}Other Links:{RESET}\n'
                                    f'{BWHITE}{BLACK}Carpet Mod Github > car {RESET}\n'
                                    f'{BWHITE}{BLACK}Scarpet Docs > scar {RESET}\n'
                                    f'{BGREEN}{WHITE}Inspiration:{RESET}\n'
                                    f'{BWHITE}{BLACK}DataPackGen > dpg {RESET}\n'
                                    f'{BWHITE}{BLACK}DataCreate.py > dcp {RESET}\n\n'
                                    f'{BWHITE}{BLACK}Main Menu > quit {RESET}\n'
                                    f'{CYAN}\n\n')
                    if lastMain == "git":
                        webbrowser.open("https://github.com/GirlInPurple/Py-Packer")
                        utils.ClearConsole()
                    elif lastMain == "twit":
                        webbrowser.open("https://twitter.com/blurpl3d")
                        utils.ClearConsole()
                    elif lastMain == "disc":
                        webbrowser.open("https://discord.gg/2PxCfY9jRd")
                        utils.ClearConsole()
                    elif lastMain == "car":
                        webbrowser.open("https://github.com/gnembon/fabric-carpet")
                        utils.ClearConsole()
                    elif lastMain == "scar":
                        webbrowser.open("https://github.com/gnembon/fabric-carpet/blob/master/docs/scarpet/Documentation.md")
                        utils.ClearConsole()
                    elif lastMain == "dpg":
                        webbrowser.open("https://misode.github.io/")
                        utils.ClearConsole()
                    elif lastMain == "dcp":
                        webbrowser.open("https://github.com/OrigamingWasTaken/DataCreate")
                        utils.ClearConsole()
                    elif lastMain == "quit":
                        validMain = "mainmenu"
                        utils.ClearConsole()
                    else:
                        utils.ClearConsole()
                        print(f"{RESET}{RED}Invalid argument. Please send a valid input.\n{RESET}\n")
            
            elif lastMain == "files": #datapack file creator
                lastMain = "filecreate"
                while validMain == "filecreate":
                    pass
                #files.DPfiles()
                
            elif lastMain == "edit": #resourcepack file creator
                print(RESET + BYELLOW + "launching RP file generator" + RESET + CYAN)
                lastMain = "editors"
                while validMain == "editors":
                    pass
                #files.RPfiles()
            
            elif lastMain == "quit": #closes the program
                input(RESET + BYELLOW + "Press enter to quit." + RESET + "\n")
                utils.ClearConsole()
                sys.exit()
            
            elif lastMain == "restart": #closes the program
                input(RESET + BYELLOW + "Press enter to restart PyPacker." + RESET + "\n")
                utils.ClearConsole()
                os.startfile(sys.argv[0])
                sys.exit()
            
            elif lastMain == "": #fixes a stupid bug that spams the custom error below
                utils.ClearConsole()
                            
            else:
                utils.ClearConsole()
                print(f"{RESET}{RED}Invalid argument. Please send a valid input.\n{RESET}\n")
                   
class files: #file makers
    def __init__():
        pass
    
    def DPfiles():
        packName = input(f'{BMAGENTA}Welcome to DataCreate! How do you want to name your datapack? (enter "quit" now to abort){RESET}\n\n{CYAN}')
        if packName != "quit":
            time.sleep(0.5)
            dataName = input(f"{RESET}{BYELLOW}How do you want to name your namespace?{RESET}\n\n{CYAN}").lower()
            validName = "false"
            while validName == "false":
                if(bool(re.match('^[a-zA-Z0-9_]*$',dataName))==True):
                    validName = "true"
                else:
                    dataName = input(RESET + RED + "Namespace not valid. Namespaces can not use specials characters. Please give a valid name.\n" + RESET + CYAN)
            time.sleep(0.5)
            dataVer = input(RESET + BMAGENTA + "What is the minecraft version of your pack? (Leave blank for your chosen default version, currently: " + settings[0] + ")" + RESET + "\n\n" + CYAN)

            if dataVer == "":
                dataVer = settings[0]
                
            foundVersion = "false"
            while foundVersion == "false":
                for ver,verid in mineVersions.items():
                    if ver == dataVer:
                        dataVer = verid
                        foundVersion = "true"

                    if foundVersion == "false":
                        dataVer = input(RESET + RED + "Version not found. Please give a supported version.\n" + RESET + CYAN)
            time.sleep(0.5)
            dataDesc = input(RESET + BWHITE + "What is the description of your datapack?" + RESET + "\n\n" + CYAN)
            time.sleep(0.5)
            dataPath = input(RESET + BRED + "Where do you want to create your datapack? (Leave blank for your chosen default filepath, currently: " + filePath + ")" + RESET + "\n\n" + CYAN)

            if dataPath == "":
                dataPath = filePath

            validDir = "false"
            while validDir == "false":
                if dataPath:
                    isDirectory = os.path.isdir(dataPath)
                    if isDirectory == False:
                        dataPath = input(RESET + RED + "The path you provided is invalid. Please give a valid path. (Leave blank to create in the script's folder)\n" + RESET + CYAN)
                    else:
                        validDir = "true"

            os.chdir(dataPath)
            utils.append_mkdir("",packName)
            os.chdir(packName)
            utils.append_mkdir("","data")
            packMcmeta = open("pack.mcmeta", "w")
            packMcmeta.write('{\n\t"pack": {\n\t\t"pack_format":'+dataVer+',\n\t\t"description": "'+dataDesc+'"\n\t}\n}') #an F-string is unusable here as far as i know
            packMcmeta.close()
            os.chdir("data")
            utils.append_mkdir("","minecraft")
            os.mkdir(dataName)
            os.chdir("minecraft")
            os.mkdir("tags")
            os.chdir("tags")
            os.mkdir("functions")
            os.chdir("functions")
            tickJ = open("tick.json", "w")
            tickJ.write('{"values": ["' + dataName + ':tick"]}')
            tickJ.close()
            loadJ = open("load.json", "w")
            loadJ.write('{"values": ["' + dataName + ':load"]}')
            loadJ.close()
            os.chdir(dataPath + '/' + packName + '/data/' + dataName)
            os.mkdir("advancements")
            os.mkdir("dimension")
            os.mkdir("dimension_type")
            os.mkdir("functions")
            os.chdir("functions")
            tickM = open("tick.mcfunction", "w")
            tickM.write('##Write below every commands you want to execute each ticks.')
            tickM.close()
            loadM = open("load.mcfunction", "w")
            loadM.write('##Write below every commands you want to execute on each reload.\ntellraw @a {"text":"' + packName + ' has reloaded","color":"blue"}')
            loadM.close()
            os.chdir("..")
            os.mkdir("loot_tables")
            os.mkdir("predicates")
            os.mkdir("recipes")
            os.mkdir("structures")
            os.mkdir("item_modifiers")
            os.mkdir("tags")
            os.mkdir("worldgen")
            os.chdir("worldgen")
            os.mkdir("biome")
            os.mkdir("configured_carver")
            os.mkdir("configured_feature")
            os.mkdir("configured_structure_feature")
            os.mkdir("configured_surface_builder")
            os.mkdir("noise_settings")
            os.mkdir("processor_list")
            os.mkdir("template_pool")
            lastDP = input(RESET + BGREEN + "Your datapack has been generated! What do you want to do?" + RESET + "\n" + BWHITE + BLACK + "Open folder > open\nQuit PyPacker > quit" + RESET + "\n" + BWHITE + BLACK + "Edit Datapack > edit" + RESET + CYAN + "\n\n")
            time.sleep(10)
            validDP = "false"
            while validDP == "false":
            
                if lastDP == "open":
                    if sys.platform=='win32':
                        os.system("start "+ dataPath)

                    if sys.platform=='darwin':
                        os.system("open " + dataPath)

                    input(RESET + BYELLOW + "File has been opened, press enter to choose another option. (Original DPfiles made by Origaming)" + RESET)
                    lastDP = ""
                elif lastDP == "quit":
                    input(RESET + BYELLOW + "Press enter to quit. (Original DPfiles made by Origaming)" + RESET)
                    sys.exit()
                elif lastDP == "open":
                    input(RESET + BYELLOW + "Press enter to enter editor, Alt+F4 to abort. (Original DPfiles made by Origaming)" + RESET)
                    #os.system("DP_editor")
                    sys.exit()
                else:
                    lastDP = input(RESET + RED + "Invalid argument. Please send a valid word.\n" + RESET + CYAN)
        else:
            print(BYELLOW + 'launching main menu' + RESET)
            main.main()
                
    def RPfiles():
        pass
    
    def SCfiles():
        pass

class editors: #file editors, notes here going forward
    class test:
        def __init__():
            #so you can put a class in a class, i was wondering if this could be an issue, thankfully it looks not: https://www.geeksforgeeks.org/inner-class-in-python/
            pass
    
    #this will come later, not sure how im gonna do this part yet
    
    #pros of pygame: simple to create and maintain long-term
    #cons of pygame: can't maximize window(?), needs downloading
    #link: https://www.pygame.org/news
    
    #pros of elctron.py: can port the whole program over to a much better system
    #cons of electron.py: i have no clue how to code good HTML/CSS/JS, only the basics i picked up while messing with F12 on random sites
    #link: https://github.com/fyears/electron-python-example
    #note: Eel looks like a better option if i end up going for this: https://github.com/python-eel/Eel
    
    #pros of PyGt5: good ui generator with alot of features
    #cons of PyQt5: its gonna be a bit complex to implement a system of this size in it, needs downloading
    #link: https://riverbankcomputing.com/software/pyqt/intro
    
    #pros of the command line: simple, understandable for most people with even a little computer knowlage
    #cons of the command line: hard to work with at times (unicode, drawing graphs, more complex visuals), not everyone understands it
    #link: n/a
    
    #pros of python arcade: Very similar to alot of game/gui libraies, including Pygame from the looks of it.
    #cons of python arcade: Learned about it just a few hours ago, so ill have to look more into it to proporly rate this, but keeping it here for refrence
    #link: https://api.arcade.academy/en/latest/index.html
    
    def __init__(self):
        pass

#project formating and plans (moved from main.main() for convenience)    
#text colors:
#   user information: BGREEN, BLACK
#   debug information: BYELLOW
#   options: BWHITE, BLACK
#   user input: RESET, CYAN
#settings: (also a settings.txt explanation)
#   default version ("1.19.2" by default)
#   default file location ("local" by default)
#   move or copy files when creating resource packs ("Move" by default)
#   display debug args ("False" by default)
#   color toggle ("False" by default)
#file creators:
#   DPfiles() for datapacks
#   RPfiles() for resource packs/texture packs
#   SCfiles() for scarpet files
#editors:
#   DPedit() DataPack Editor
#   RPedit() Resource Pack Editor, adding indivual files then ziping it without the need of WinRAR
#   SCedit() Scarpet Editor, Carpet Mod API coding lanuage 
#   MinDust() an idea i had for a Mindustry Processor editor with the same codebase as SCedit(), not sure it it would fit but i might add it if i have time

if __name__ == "__main__":

    #ansi color coding for terminals
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
    
    #check if settigns file exists, if not make it
    if bool(os.path.exists(utils.LocalFiles("") + "\settings.txt")) != True:       
        #print(f'{BYELLOW}{WHITE}No "settings.txt" file exists in this programs directory, one will automatically be created, but it will be set to built in defaults.{RESET}')
        os.chdir(utils.LocalFiles(""))
        with open("settings.txt", "x") as NewSettings:
            NewSettings.write("1.19.2\nlocal\nMove\nFalse\nFalse\nnotepad /a\nmspaint\nstart Audacity\n0")
            NewSettings.close()

    #check if standard output file exists, if not make it
    if bool(os.path.exists(utils.LocalFiles("") + "\output")) != True:
        #print(f'{BYELLOW}{WHITE}No "output" folder exists in this programs directory, one will automatically be created.{RESET}')
        os.chdir(utils.LocalFiles(""))
        os.mkdir('output')
        
    #check if example photo exists, if not grab it from Wikipedia
    #yes, i hit randomize a few times and found this page, a harmless building in England, perfect for this
    #full rights to the copyright holder of this photo, if it needs to be removed i will gladly do so.
    if bool(os.path.exists(utils.LocalFiles("") + "\Aberdeen_Tolbooth.jpg")) != True:
        #print(f'{BYELLOW}{WHITE}No "output" folder exists in this programs directory, one will automatically be created.{RESET}')
        imgURL = "https://upload.wikimedia.org/wikipedia/commons/6/62/Aberdeen_Tolbooth.jpg"
        imgLOCAL = utils.LocalFiles("") + "\Aberdeen_Tolbooth.jpg"
        urllib.request.urlretrieve(imgURL, imgLOCAL)
    
    #check if example audio tracks exist, if not, do nothing
    if bool(os.path.exists("C:\Windows\Media\Alarm01")) == True:
        print(f'')
    
    utils.ClearConsole() #just in case some graphichal bugs happen when starting up
    
    PPutils = utils() #general utils, needs to be loaded first or everything breaks
    PPmain = main() #for settings handling and create main menu
    main.main() #launches the UI, branches from there