import os
import tkinter.filedialog
import shutil
import datetime

pasta = tkinter.filedialog.askdirectory()

arquivos = os.listdir(pasta)

print(arquivos)

backup = "backup"
backupCompleto = f"{pasta}/{backup}"
if not os.path.exists(backupCompleto):
    os.mkdir(backupCompleto)


agora = datetime.datetime.today().strftime("%Y-%m-%d %H%M")

for arquivo in arquivos:
    nomeCompleto = f"{pasta}/{arquivo}"
    destino = f"{backupCompleto}/{agora}/{arquivo}"

    if not os.path.exists(f"{backupCompleto}/{agora}"):
        os.mkdir(f"{backupCompleto}/{agora}")


    if "." in arquivo:
        shutil.copy2(nomeCompleto,destino)
    elif "backup" != arquivo:
        shutil.copytree(nomeCompleto,destino)