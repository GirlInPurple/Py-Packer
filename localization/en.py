#translation variable names are the state of valid name that the page is for.
#so mainmenu would be used just after mainmenu is instated as validMain
#this is what i mean:

#...
#validMain = "settings"
#utils.ClearConsole()
#while validMain == "settings":
#    MenuingInput = input(LocalizationFunc(f'{SettingsData["Language"]}.{validMain}'))
#...

#all debug output will stay in english, as python is writen in english and would be difficult to implement
#if someone figures out how to change all debug logs to other languages, feel free to add it

mainmenu = """
f'{BGREEN}{WHITE}Welcome to PyPacker! Where would you like to start?{RESET}\n'
f'{BGREEN}{WHITE}PyPacker Main Menu:{RESET}\n'
f'{BGREEN}{WHITE}(All commands case sensitve; "open" and "out" not guaranteed to work on all Lunix distros){RESET}\n'

f'\n{BGREEN}{WHITE}Program Folders:{RESET}\n'
f'{BWHITE}{BLACK}Open Program Folder > open {RESET}\n'
f'{BWHITE}{BLACK}Open Output Folder > out {RESET}\n'

f'\n{BGREEN}{WHITE}PyPacker:{RESET}\n'
f'{BWHITE}{BLACK}Pack File Generators > files (Datapack, Behavior, Resource){RESET}\n'
f'{BWHITE}{BLACK}Pack File Editors > edit (Datapack, Behavior, Resource){RESET}\n'
f'{BWHITE}{BLACK}Other File Editors > edit (Scarpet, PLCCjson, Mlog){RESET}\n'

f'\n{BGREEN}{WHITE}Miscellaneous:{RESET}\n'
f'{BWHITE}{BLACK}Settings Menu > set {RESET}\n'
f'{BWHITE}{BLACK}External Links > link {RESET}\n\n'

f'{BWHITE}{BLACK}Quit PyPacker > quit {RESET}\n'
f'{BWHITE}{BLACK}Restart PyPacker > restart {RESET}\n'
f'{CYAN}\n'
"""
settings = """

"""