import sys
import os
import re

class utils: #startup and other universal utils
    def __init__(self):
        pass
    
    #colours
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
    
    #constants
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

class main: #the main program
    def __init__(self):
        os.system("clear")
        global filePath
        filePath = os.path.dirname(os.path.realpath(__file__))
        
    def main(self):
        
        files.DPfiles() #set this as the default for now as i build up main.main()
        #settings: (also a settings.txt explanation)
        #   default version (set to 1.19.2 by default)
        #   default file location (set to local by default)
        #   color toggle
        #   first login (with a reset button in case a plugin breaks)
        #opens:
        #   DPfiles() for datapacks
        #   RPfiles() for resrouce packs/texture packs
        #   SCfiles() for scarpet files
        #editors:
        #   Dp, Rp, and Sc editors are
        #mc utils:
        #   portal cords, 3d space, and circle calculators all in one
        #   remote server connect via a 
        return
        
    def TXThandler(self, file):
        #stores txt
        pass
        
class files: #file makers
    def __init__(self):
        pass
    
    def DPfiles():
        packName = input(utils.BGREEN + "Welcome to DataCreate! How do you want to name your datapack?" + utils.RESET + "\n\n" + utils.CYAN)
        dataName = input(utils.RESET + utils.BYELLOW + "How do you want to name your namespace?" + utils.RESET + "\n\n" + utils.CYAN).lower()
        validName = "false"
        while validName == "false":
            if(bool(re.match('^[a-zA-Z0-9_]*$',dataName))==True):
                validName = "true"
            else:
                dataName = input(utils.RESET + utils.RED + "Namespace not valid. Namespaces can not use specials characters. Please give a valid name.\n" + utils.RESET + utils.CYAN)

        dataVer = input(utils.RESET + utils.BMAGENTA + "What is the minecraft version of your pack?" + utils.RESET + "\n\n" + utils.CYAN)

        foundVersion = "false"
        while foundVersion == "false":
            for ver,verid in utils.mineVersions.items():
                if ver == dataVer:
                    dataVer = verid
                    foundVersion = "true"

            if foundVersion == "false":
                dataVer = input(utils.RESET + utils.RED + "Version not found. Please give a supported version.\n" + utils.RESET + utils.CYAN)

        dataDesc = input(utils.RESET + utils.BWHITE + "What is the description of your datapack?" + utils.RESET + "\n\n" + utils.CYAN)
        dataPath = input(utils.RESET + utils.BRED + "Where do you want to create your datapack? (Leave blank to create in the script's folder)" + utils.RESET + "\n\n" + utils.CYAN)

        validDir = "false"
        while validDir == "false":
            if dataPath:
                isDirectory = os.path.isdir(dataPath)
                if isDirectory == False:
                    dataPath = input(utils.RESET + utils.RED + "The path you provided is invalid. Please give a valid path. (Leave blank to create in the script's folder)\n" + utils.RESET + utils.CYAN)
                else:
                    validDir = "true"
            else:
                dataPath = filePath

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
        lastR = input(utils.RESET + utils.BGREEN + "Your datapack has been generated! What do you want to do?" + utils.RESET + "\n\n" + utils.BWHITE + utils.BLACK + "Open folder > open\nQuit PyPacker > quit\nEdit Datapack > Edit" + utils.RESET + utils.CYAN + "\n\n")
        validR = "false"
        while validR == "false":
        
            if lastR == "open":
                if sys.platform=='win32':
                    os.system("start "+ dataPath)

                if sys.platform=='darwin':
                    os.system("open " + dataPath)

                input(utils.RESET + utils.BYELLOW + "File has been opened, press enter to choose another option. (Made by Origaming)" + utils.RESET)
                lastR = ""
            elif lastR == "quit":
                input(utils.RESET + utils.BYELLOW + "Thanks for using DataCreate! Press enter to quit. (Made by Origaming)" + utils.RESET)
                sys.exit()
            elif lastR == "open":
                input(utils.RESET + utils.BYELLOW + "Thanks for using DataCreate! Press enter to enter editor, Alt+F4 to abort. (Made by Origaming)" + utils.RESET)
                #os.system("DP_editor")
                sys.exit()
            else:
                lastR = input(utils.RESET + utils.RED + "Invalid argument. Please send a valid word.\n" + utils.RESET + utils.CYAN)
                
    def RPfiles():
        pass
    
    def SCfiles():
        pass

class editors: #file editors, note here
    
    #this will come later, not sure how im gonna do this part yet
    
    #pros of pygame: simple to create and maintain long-term
    #cons of pygame: can't maximize window(?), needs downloading
    
    #pros of elctron.py: can port the whole program over to a much better system
    #cons of electron.py: i have no clue how to code good HTML/CSS/JS, only the basics i picked up while messing with F12 on random sites
    
    #pros of PyGt5: good ui generator with alot of features
    #cons of PyQt5: its gonna be a bit complex to implement a system of this size in it, needs downloading
    
    #pros of the command line: simple, understandable for most people with even a little computer knowlage
    #cons of the command line: hard to work with at times (unicode, drawing graphs, more complex visuals), not everyone understnads it
    
    def __init__(self):
        pass
    
main.main()