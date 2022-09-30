#Made by Origaming, full credit to them for this.

#All modules are built-in
import sys
import os
import re
os.system("clear")
filePath = os.path.dirname(os.path.realpath(__file__))

class colors:
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
 
mineVersions = {
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

packName = input(colors.BGREEN + "Welcome to DataCreate! How do you want to name your datapack?" + colors.RESET + "\n\n" + colors.CYAN)
dataName = input(colors.RESET + colors.BYELLOW + "How do you want to name your namespace?" + colors.RESET + "\n\n" + colors.CYAN).lower()
validName = "false"
while validName == "false":
    if(bool(re.match('^[a-zA-Z0-9_]*$',dataName))==True):
        validName = "true"
    else:
        dataName = input(colors.RESET + colors.RED + "Namespace not valid. Namespaces can not use specials characters. Please give a valid name.\n" + colors.RESET + colors.CYAN)

dataVer = input(colors.RESET + colors.BMAGENTA + "What is the minecraft version of your pack?" + colors.RESET + "\n\n" + colors.CYAN)

foundVersion = "false"
while foundVersion == "false":
    for ver,verid in mineVersions.items():
        if ver == dataVer:
            dataVer = verid
            foundVersion = "true"

    if foundVersion == "false":
        dataVer = input(colors.RESET + colors.RED + "Version not found. Please give a supported version.\n" + colors.RESET + colors.CYAN)

dataDesc = input(colors.RESET + colors.BWHITE + "What is the description of your datapack?" + colors.RESET + "\n\n" + colors.CYAN)
dataPath = input(colors.RESET + colors.BRED + "Where do you want to create your datapack? (Leave blank to create in the script's folder)" + colors.RESET + "\n\n" + colors.CYAN)

validDir = "false"
while validDir == "false":
    if dataPath:
        isDirectory = os.path.isdir(dataPath)
        if isDirectory == False:
            dataPath = input(colors.RESET + colors.RED + "The path you provided is invalid. Please give a valid path. (Leave blank to create in the script's folder)\n" + colors.RESET + colors.CYAN)
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
lastR = input(colors.RESET + colors.BGREEN + "Your datapack has been generated! What do you want to do?" + colors.RESET + "\n\n" + colors.BWHITE + colors.BLACK + "Open folder > open\nQuit PyPacker > quit\nEdit Datapack > Edit" + colors.RESET + colors.CYAN + "\n\n")
validR = "false"
while validR == "false":
   
    if lastR == "open":
        if sys.platform=='win32':
            os.system("start "+ dataPath)

        if sys.platform=='darwin':
            os.system("open " + dataPath)

        input(colors.RESET + colors.BYELLOW + "File has been opened, press enter to choose another option. (Made by Origaming)" + colors.RESET)
        lastR = ""
    elif lastR == "quit":
        input(colors.RESET + colors.BYELLOW + "Thanks for using DataCreate! Press enter to quit. (Made by Origaming)" + colors.RESET)
        sys.exit()
    elif lastR == "open":
        input(colors.RESET + colors.BYELLOW + "Thanks for using DataCreate! Press enter to enter editor, Alt+F4 to abort. (Made by Origaming)" + colors.RESET)
        #os.system("DP_editor")
        sys.exit()
    else:
        lastR = input(colors.RESET + colors.RED + "Invalid argument. Please send a valid word.\n" + colors.RESET + colors.CYAN)