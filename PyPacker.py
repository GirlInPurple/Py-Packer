import sys
import os
import re
import time

class utils: #startup and other universal utils
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
        
        try:
            if ColorToggle != "false":
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
                RESET = '\u001b[0m'
                BOLD = '\033[1m'
                UNDERLINE = '\033[4m'
            else:
                BLACK = '\u001b[0m'
                RED = '\u001b[0m'
                BRED = '\u001b[0m'
                GREEN = '\u001b[0m'
                BGREEN = '\u001b[0m'
                YELLOW = '\u001b[0m'
                BYELLOW = '\u001b[0m'
                BLUE = '\u001b[0m'
                MAGENTA = '\u001b[0m'
                BMAGENTA = '\u001b[0m'
                CYAN = '\u001b[0m'
                WHITE = '\u001b[0m'
                BWHITE = '\u001b[0m'
                RESET = '\u001b[0m'
                BOLD = '\u001b[0m'
                UNDERLINE = '\u001b[0m'
        except:
            print("Color Handling Failed, errors might occour later")
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
            RESET = '\u001b[0m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'


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
    
    def VersionHandler(self, version):
        foundVersion = "false"
        while foundVersion == "false":
            for ver, verid in mineVersions.items():
                if ver == version:
                    foundVersion = "true"
                    print("ver")
                    return ver

            if foundVersion == "false":
                return "failed"
    def LocalFiles(self):
        return os.path.dirname(os.path.realpath(__file__))

class main: #the main program
    def __init__(self):
        
        data = []
        global settings
        settings = []
        
        try:
            with open("settings.txt","r") as f:
                data = f.readlines() #readlines() returns a list of items in said file
                print(data)

            for i in range(0, 5): #list loop, the console is (unintentionally) spammed for a bit
                print(data[i])
                settings.append(data[i])
                print(settings)
            
            #begin settings handlers:
            
            #version, needs to be completly redone it jsut spitting out constant errors
            global Dversion
            if utils.VersionHandler(self, settings[0]) == "failed":
                print("error while setting default version, setting to 1.19.2")
                Dversion = "1.19.2"
            else:
                Dversion = data[0]
                print("loaded default version:" + Dversion)
            
            #filepath
            global filePath
            if settings[1] == "local\n":
                filePath = utils.LocalFiles("")
                print('filepath set to "local"')
            else:
                filePath = settings[1]
                print("chosen filepath:" + filePath)
            
            #color
            global ColorToggle
            if settings[2] == "true":
                ColorToggle = "false"
                print("colored text off")
            else:
                ColorToggle = "true"
                print("colored text on")  
            
        except:
            print("error while handling settings, loading default settings, some errors might occour later")
            settings.append("1.19.2\n")
            settings.append("local\n")
            settings.append("true\n")
            settings.append("1\n")
            settings.append("false")
            

    def main():
        
        #settings: (also a settings.txt explanation)
        #   default version (set to 1.19.2 by default)
        #   default file location (set to local by default)
        #   color toggle
        #   first login (with a reset button in case a package or this breaks)
        #   debug mode (useless atm)
        #opens:
        #   DPfiles() for datapacks
        #   RPfiles() for resrouce packs/texture packs
        #   SCfiles() for scarpet files
        #editors:
        #   Dp, Rp, and Sc editors are
        #mc utils:
        #   portal cords, 3d space, and circle calculators all in one
        
        print(BGREEN + 'Welcome to PyPacker! Where would you like to start?\n(Case sensitve, all lowercase; "open" and "output" not guaranteed to work on all Lunix distros)' + RESET)
        #"[name] > [command]"+ RESET +"\n"+ BWHITE + BLACK + paste this between a "black+" and begining of the next command name.
        lastMain = input(BWHITE + BLACK + "Open Program Folder > open"+ RESET +"\n"+ BWHITE + BLACK + "Open Output Folder > output"+ RESET +"\n"+ BWHITE + BLACK +"Launch Datapack File Generator > dpfiles"+ RESET +"\n"+ BWHITE + BLACK +"Quit PyPacker > quit\n" + RESET + "\n\n" + CYAN)
        validMain = "false"
        while validMain == "false":
        
            if lastMain == "open":
                if sys.platform=='win32':
                    os.system("start " + utils.LocalFiles(""))

                if sys.platform=='darwin':
                    os.system("open " + utils.LocalFiles(""))

                input(RESET + BYELLOW + "Program File has been opened, press enter to choose another option." + RESET + CYAN)
                lastMain = ""
                
            elif lastMain == "output":
                if sys.platform=='win32':
                    os.system("start " + filePath)

                if sys.platform=='darwin':
                    os.system("open " + filePath)

                input(RESET + BYELLOW + "Output File has been opened, press enter to choose another option." + RESET + CYAN)
                lastMain = ""
                
            elif lastMain == "quit":
                input(RESET + BYELLOW + "Press enter to quit." + RESET + CYAN)
                sys.exit()
                
            elif lastMain == "settings":
                print(RESET + BYELLOW + "settings not impelmented yet" + RESET + CYAN)
                lastMain = ""
                
            elif lastMain == "dpfiles":
                print(RESET + BYELLOW + "launching DP file generator, ALT+F4 at any time to abort" + RESET + CYAN)
                files.DPfiles()
                
            elif lastMain == "rpfiles":
                return
            
            else:
                lastMain = input(RESET + RED + "Invalid argument. Please send a valid word.\n" + RESET + CYAN)
        
class files: #file makers
    def __init__():
        pass
    
    def DPfiles():
        packName = input(BGREEN + "Welcome to DataCreate! How do you want to name your datapack?" + RESET + "\n\n" + CYAN)
        time.sleep(0.5)
        dataName = input(RESET + BYELLOW + "How do you want to name your namespace?" + RESET + "\n\n" + CYAN).lower()
        validName = "false"
        while validName == "false":
            if(bool(re.match('^[a-zA-Z0-9_]*$',dataName))==True):
                validName = "true"
            else:
                dataName = input(RESET + RED + "Namespace not valid. Namespaces can not use specials characters. Please give a valid name.\n" + RESET + CYAN)
        time.sleep(0.5)
        dataVer = input(RESET + BMAGENTA + "What is the minecraft version of your pack? (Leave blank for your chosen default version, currently: " + Dversion + ")" + RESET + "\n\n" + CYAN)

        if dataVer == "":
            dataVer = Dversion
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
        os.mkdir(packName)
        os.chdir(packName)
        os.mkdir("data")
        packMcmeta = open("pack.mcmeta", "w")
        packMcmeta.write('{"pack": {"pack_format": ' + dataVer + ',"description": "' + dataDesc + '"}}')
        packMcmeta.close()
        os.chdir("data")
        os.mkdir("minecraft")
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
        lastDP = input(RESET + BGREEN + "Your datapack has been generated! What do you want to do?" + RESET + "\n" + BWHITE + BLACK + "Open folder > open\nQuit PyPacker > quit\nEdit Datapack > Edit" + RESET + CYAN + "\n\n")
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

PPmain = main()
PPutils = utils()
main.main()