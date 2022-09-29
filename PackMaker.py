__pmv__ = "0.0.1"

import tkinter #imports here
import customtkinter
import sys
import os
import re
import json


#globals here
appear = "System" #appear: system (default), light, dark
theme = "blue" #themes: blue (default), dark-blue, green
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

class PackMaker(customtkinter.CTk):
    
    #main window
    def __init__(self):
        super().__init__() #i have no clue what this does but im not gonna question it because it works

        self.geometry("400x240") #default size, cna be resized by user
        self.title("testing") 
        customtkinter.set_appearance_mode(appear)  
        customtkinter.set_default_color_theme(theme) 

        # buttons here, use CTkButton instead of tkinter Button, it will breaK
        def button_function():
            print("button")
        
        button = customtkinter.CTkButton(self, text="CTkButton", command=button_function)
        button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        DMPbutton = customtkinter.CTkButton(self, text="CTkButton", command=self.DatapackMaker)
        DMPbutton.place(relx=0.25, rely=0.25, anchor=tkinter.CENTER)
    
    
    #other windows here
    def DatapackMaker(self):
        
        window = customtkinter.CTkToplevel(self)
        window.geometry("500x600")
        window.title("Pack File Creator")

        e_packN = customtkinter.CTkEntry(window, placeholder_text="Pack Name", width=350, height=25)
        e_packN.pack(padx=20, pady=10)
        packN = e_packN.get()
        
        e_dataN = customtkinter.CTkEntry(window, placeholder_text="Namespace Name (no specials)", width=350, height=25)
        e_dataN.pack(padx=20, pady=10)
        dataN = e_dataN.get()
        
        e_dataV = customtkinter.CTkEntry(window, placeholder_text="Version of MC (ex; 1.19.2, 1.13.1, 1.14.2, 1.15)", width=350, height=25)
        e_dataV.pack(padx=20, pady=10)
        dataV = e_dataV.get()
        
        e_dataD = customtkinter.CTkEntry(window, placeholder_text="Description", width=350, height=25)
        e_dataD.pack(padx=20, pady=10)
        dataD = e_dataD.get()
        
        e_dataP = customtkinter.CTkEntry(window, placeholder_text="File Path (leave blank for local)", width=350, height=25)
        e_dataP.pack(padx=20, pady=10)
        dataP = e_dataD.get()
        
        def DataCheck():
            #check if file path is valid
            if dataP == "no input":
                dataP = dir_path = os.path.dirname(os.path.realpath(__file__))
            
            #check if name is valid
            if(bool(re.match('^[a-zA-Z0-9_]*$',dataN))==True):
                DPMerror = "Invalid Name (No Special Charictars)"
            else:
                
                #check if version is valid
                for ver,verid in mineVersions.items():
                    if ver != dataV:
                        DPMerror = "Invalid Version (" + __pmv__ + "supports from 1.13 to 1.19.2)"
                    else:
                        dataV = verid
            DPMerror = ""
            DataCreate(packN, dataN, dataV, dataD, dataP)
        
        def DataCreate(packN, dataN, dataV, dataD, dataP): #This is a teardown of Origaming's codebase here: https://github.com/OrigamingWasTaken/DataCreate
            #make files, thanks again Origaming
            os.system("clear")
            os.chdir(dataP)
            os.mkdir(packN)
            os.chdir(packN)
            os.mkdir("data")
            packMcmeta = open("pack.mcmeta", "w")
            packMcmeta.write('{"pack": {"pack_format": ' + dataV + ',"description": "' + dataD + '"}}')
            packMcmeta.close()
            os.chdir("data")
            os.mkdir("minecraft")
            os.mkdir(dataN)
            os.chdir("minecraft")
            os.mkdir("tags")
            os.chdir("tags")
            os.mkdir("functions")
            os.chdir("functions")
            tickJ = open("tick.json", "w")
            tickJ.write('{"values": ["' + dataN + ':tick"]}')
            tickJ.close()
            loadJ = open("load.json", "w")
            loadJ.write('{"values": ["' + dataN + ':load"]}')
            loadJ.close()
            os.chdir(dataP + '/' + packN + '/data/' + dataN)
            os.mkdir("advancements")
            os.mkdir("dimension")
            os.mkdir("dimension_type")
            os.mkdir("functions")
            os.chdir("functions")
            tickM = open("tick.mcfunction", "w")
            tickM.write('##Write below every commands you want to execute each ticks.')
            tickM.close()
            loadM = open("load.mcfunction", "w")
            loadM.write('##Write below every commands you want to execute on each reload.\ntellraw @a {"text":"' + packN + ' has reloaded","color":"blue"}')
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

            #open files
            if sys.platform=='win32':
                os.system("start "+ dataP)

            if sys.platform=='darwin': #someone run this on lunix and tell me if it works or not
                os.system("open " + dataP)
            #create the files for a datapack(go to next screen)

        DPMerror = ""
        
        errorLabel = customtkinter.CTkLabel(window, text=DPMerror)
        errorLabel.pack(side="top", fill="both", expand=True, padx=40, pady=40)
        
        c1 = customtkinter.CTkCheckBox(window, text="This will create files on your pc (around 0.4kb), are you sure you want to do this?", onvalue=1, offvalue=0)
        c1.pack(relx=0.6, rely=0.6, anchor=tkinter.N)
        
        DMPcheckbutton = customtkinter.CTkButton(window, text="Create Pack", command=DataCheck)
        DMPcheckbutton.place(relx=0.6, rely=0.6, anchor=tkinter.S)

PackM = PackMaker()
PackM.mainloop()