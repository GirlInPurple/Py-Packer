import sys, os, re, time, ctypes #all built in, convenient
os.system("") #why does this fix ANSI color coding? god only knows, i have no clue

#window customisation, breaks VScode
os.system('mode con: cols=100 lines=40')
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
        
class main: #the main program
    def __init__(self):
        
        data = []
        global settings
        settings = []
        
        SettingsCompute = "check"
        while SettingsCompute == "check":
            if bool(os.path.exists(utils.LocalFiles(self) + "\settings.txt")) == True:

                openTXT = utils.LocalFiles(self) + "\settings.txt"

                with open(openTXT,"r") as f:
                    data = f.readlines() #readlines() returns a list of items in said file

                for i in range(0, len(data)): #list loop, the console is (unintentionally) spammed for a bit
                    settings.append(data[i].strip('\n'))
                    
                f.close()
                
                #settings handlers:
                
                #colors
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
                BLACK, RED, BRED, GREEN, BGREEN, YELLOW, BYELLOW, BLUE, MAGENTA, BMAGENTA, CYAN, WHITE, BWHITE, RESET, BOLD, UNDERLINE = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
                
                
                if settings[4] == "True":
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
                        
                SettingsCompute = "Done!"
                                        
            else:
                print(f'{BYELLOW}{BLACK}No "settings.txt" file exists in this programs directory, one will automatically be created, but it will be set to built in defaults.{RESET}')
                os.chdir(utils.LocalFiles(self))
                with open("settings.txt", "x") as MakeNew:
                    MakeNew.write("1.19.2\nlocal\nMove\nFalse\nTrue")
                    MakeNew.close()
        
        if settings[3] != "False":
            print(f"{BYELLOW}{BLACK}start debug messages:\n{openTXT}\n{data}\n{settings}{RESET}")
   
        if settings[3] != "False":
            print(f"{BYELLOW}{BLACK}end debug messages\n{RESET}")
        
    def main():
        
        print(f'{BGREEN}Welcome to PyPacker! Where would you like to start?\n(Case sensitve, all lowercase; "open" and "out" not guaranteed to work on all Lunix distros){RESET}')
        
        validMain = "mainmenu"
        while validMain == "mainmenu":
            lastMain = input(f"{BGREEN}{WHITE}PyPacker Main Menu{RESET}\n"
                             f"{BWHITE}{BLACK}Open Program Folder > open{RESET}\n"
                             f"{BWHITE}{BLACK}Open Output Folder > out{RESET}\n"
                             f"{BWHITE}{BLACK}Settings Menu > settings{RESET}\n"
                             f"{BWHITE}{BLACK}File Generators > files{RESET}\n"
                             f"{BWHITE}{BLACK}Pack Editors > edit{RESET}\n"
                             f"{BWHITE}{BLACK}Basic Utilities > utils{RESET}\n"
                             f"{BWHITE}{BLACK}Quit PyPacker > quit\n{RESET}\n"
                             f"{CYAN}") #the input text will be cyan, also really easy to add extra stuff to
        
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
                
            elif lastMain == "settings": #settings page
                print(RESET + BYELLOW + "settings not impelmented yet" + RESET + CYAN)
                utils.ClearConsole()
                
            elif lastMain == "utils": #commonly used utils
                print("")
                utils.ClearConsole()
            
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
                os.startfile(sys.argv[0])
                utils.ClearConsole()
                sys.exit()
            
            elif lastMain == "": #fixes a stupid bug that spams the custom error below
                pass
                            
            else:
                utils.ClearConsole()
                print(f"{RESET}{RED}Invalid argument. Please send a valid input.\n{RESET}\n")
                
            
class files: #file makers
    def __init__():
        pass
    
    def DPfiles():
        packName = input(BGREEN + 'Welcome to DataCreate! How do you want to name your datapack? (enter "quit" now to abort)' + RESET + "\n\n" + CYAN)
        if packName != "quit":
            time.sleep(0.5)
            dataName = input(RESET + BYELLOW + "How do you want to name your namespace?" + RESET + "\n\n" + CYAN).lower()
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
            else:
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
            packMcmeta.write('{\n"pack": {\n"pack_format": ' + dataVer + ',\n"description": "' + dataDesc + '"\n}\n}') #the formating of this is all messed up, a fix is nessasary
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
#file creators:
#   DPfiles() for datapacks
#   RPfiles() for resource packs/texture packs
#   SCfiles() for scarpet files
#editors:
#   DPedit() DataPack Editor
#   RPedit() Resource Pack Editor, adding indivual files then ziping it without the need of WinRAR
#   SCedit() Scarpet Editor, Carpet Mod API coding lanuage 
#   MinDust() an idea i had for a Mindustry Processor editor with the same codebase as SCedit(), not sure it it would fit but i might add it if i have time
#mc utils:
#   portal cords (easy), 3d space, and circle calculators all in one (those last two ill use MatPlotLib i think)

if __name__ == "__main__":
    PPutils = utils() #utils and colors, needs to be loaded first or everything breaks
    PPmain = main() #for settings handling
    print(f"{BYELLOW}PyPacker is Loading!{RESET}\n\n")
    main.main() #launches the main menu