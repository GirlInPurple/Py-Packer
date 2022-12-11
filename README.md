# Py-Packer

A work in progress CUI (Console User Interface) based creation tool for 1.13.0 through 1.19.2 Java Minecraft.

<b>This project is being completely rewriten and is very unstable, it is recommended to not use it currently. PyPacker Legacy is still here in its incompleted state and still works fine, but is incompatable with PyPackerRewrite and may break a majoity of future releases.</b>

## Short Term Plans (this project's main plans.)

- [ ] Resource and Behavior/Datapack Creation simplification
- [ ] Scarpet code generator
- [ ] [PojavLaucher](https://github.com/PojavLauncherTeam/PojavLauncher) Custom Controls creator <i>(In Progress!)</i>
- [ ] Update to 1.19.3/1.20 ASAP <i>(In Progress!)</i>
- [ ] Make a functional settings page <i>(In Progress!)</i>

## Long Term Plans (up in the air and may not happen at all)

- [ ] Localization to French, Spanish, and German (most likely in that order)
- [ ] Add a [Mindustry](https://github.com/Anuken/Mindustry) [Logic](https://mindustrygame.github.io/wiki/logic/0-introduction/) <i>(those are two different links)</i> code generator using the codebase of the Scarpet generator as they have some similarities
- [ ] Linux/OSX Support

## Main Contributors

- <b> @OrigamingWasTaken </b> (Original creator of [DataCreate.py](https://github.com/OrigamingWasTaken/DataCreate), a part of this projects foundation)
- <b> @AnhNguyenlost13 </b> (Helping with testing)

## Known Issues

- Due to OS limitations, you cant have 2 of the same "data" folder without manualy creating it. The current fix is adding "_0" to the file name, but it requries you to go into the files and edit the folder names manually.
- This project will not work on most - if not all - Linux distros. Porting it over to Linux/OSX is in the plans, but quite far off due to the console based nature of this program.

## First Startup

<b>Do not run [PyPacker.py](https://github.com/GirlInPurple/Py-Packer/blob/main/PyPacker.py), as it is deprecated and may break the new version, [PyPackerRewrite.py](https://github.com/GirlInPurple/Py-Packer/blob/main/PyPackerRewrite.py)</b>

When you first launch PyPacker, you can review the settings or just skip past it immediately, no matter what it will have to restart to put you on the main menu.

While launching PyPacker, 5 files will be created:

- Two folder will be created, "output" and "assets"
- A "settings.json" file will be created then writen in immediately, the settings are msotly self explanatory, feel free to mess around with it
- A random photo grabbed off Wikipedia as a [test image](https://en.wikipedia.org/wiki/The_Tolbooth,_Aberdeen) later
- ["God Save The King"](https://en.wikipedia.org/wiki/God_Save_the_King), the United Kingdom's nation anthem

The 2 example files will be saved to the "assets" folder and are used to test your chosen editors for files the 3 kinds of files this program can handle; text/json, image, and audio. The `settings.json` is not saved to the assets folder as to save on having to move it around later for Python to access it. 

PyPacker has been tested on Python versions `3.10.8`, `3.10.9`, and `3.11.1`. It may work on other versions up to `3.0`, but no gaurentees.

## Contributing

Anyone is free to modify, contribute, or change this program in any way you see fit, it's MIT lisense for a reason. But if you do contribute, please try to keep the code in this format so we can all understand it and edit it cleanly. If you happen to make any of these examples faster, feel free to paste them here so everything can be changed over.

- Menus (Large `input()`/`print()` statements):

```python
utils.ClearConsole()
validMain = "Page Name"
while validName == "Page Name"

    if Override == False:
        MenuingInput = input(f'{Background Color}{Text Color}Page Name{RESET}\n' #try and keep the text looking like it is what is renders like
            f'{Background Color}{Text Color}Page Description{RESET}\n'
            f'{Background Color}{Text Color}Section Name{RESET}\n'
            f'{Background Color}{Text Color}Text{RESET}\n'
            f'{Background Color}{Text Color}Text{RESET}\n'
            f'{Background Color}{Text Color}Text{RESET}\n'

            f'\n{Background Color}{Text Color}Section Name{RESET}\n' #separate sections like this
            f'{Background Color}{Text Color}Text{RESET}\n'
            f'{Background Color}{Text Color}Text{RESET}\n'
            f'{Background Color}{Text Color}Text{RESET}\n'

            f'{Background Color}{Text Color}Back to [whatever last page was] > quit{RESET}\n' #must be on every page
            f'{Background Color}{Text Color}Restart PyPacker > restart {RESET}\n' #if nessasary on the page
            f'{CYAN}\n') #input text is cyan, only add if the print is part of a input()
    else:
        MenuingInput = "Override Command" #this is used to get sent immediatly to a certain page/command

    if MenuingInput == "Nested Page Command":
        utils.ClearConsole()
        validMain = "Nested Page Name"
        while validName == "Nested Page Name"
            MenuingInput = input(f'{Background Color}{Text Color}Page Name{RESET}\n'
                f'{Background Color}{Text Color}Page Description{RESET}\n'

                f'\n{Background Color}{Text Color}Section Name{RESET}\n'
                f'{Background Color}{Text Color}Text{RESET}\n'
                f'{Background Color}{Text Color}Text{RESET}\n'
                f'{Background Color}{Text Color}Text{RESET}\n'

                f'{Background Color}{Text Color}Back to [whatever last page was] > quit{RESET}\n' #must be on every page
                f'{Background Color}{Text Color}Restart PyPacker > restart {RESET}\n' #if nessasary on the page
                f'{CYAN}\n')

            if MenuingInput == "choice0":
                #do something
            elif MenuingInput == "choice1":
                #do another something
            elif MenuingInput == "choice2":
                #faire quelque chose
            elif MenuingInput == "":
                utils.ClearConsole()
            else:
                utils.ClearConsole()
                print(f"{RESET}{RED}Invalid argument. Please send a valid input.{RESET}\n\n")
    elif MenuingInput == "choice1":
        #do another something
    elif MenuingInput == "choice2":
        #faire quelque chose
    elif MenuingInput == "":
        utils.ClearConsole() #A fix for a but that whenever you press enter with nothing entered it would say "Invalid Input"
    else:
        utils.ClearConsole()
        print(f"{RESET}{RED}Invalid argument. Please send a valid input.{RESET}\n\n")
```

- ANSI Coloring System:

```python
#user information: BGREEN, BLACK
#debug information: BYELLOW, BLACK
#options: BWHITE, BLACK
#user input: RESET, CYAN

#ANSI Refrence Table (Please, don't use bare ANSI codes in strings, save us our time and sanity.)

#Used:
RESET = "\u001b[0m"
BYELLOW = '\u001b[43;1m'
BLACK = '\u001b[30m'
BWHITE = '\u001b[47;1m'
CYAN = '\u001b[36;1m'
BGREEN = '\u001b[42;1m'
BRED = '\u001b[41;1m' #I keep reading this as "Bread"

#Unused:
RED = '\u001b[31m'
GREEN = '\u001b[32m'
WHITE = '\u001b[37m'
YELLOW = '\033[92m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
BMAGENTA = '\u001b[45;1m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
```

- Filepaths (utils.LocalFiles("") is just shorthand for the filepath from system root to the programs location.)

```python
fr'{utils.LocalFiles("")}\file_name.extention'

#or

utils.LocalFiles("") + r'\file_name.extention'
```
