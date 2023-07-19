from botcity.plugins.excel import BotExcelPlugin
from botcity.plugins.files import BotFilesPlugin

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    bot = DesktopBot()
    caminho = 'c:\Tr'
    folder = BotFilesPlugin()
    arquivos = folder.get_all_file_paths(directory_path=caminho)

    for tr in arquivos:
        alter1 = tr.replace('c:\Tr', '')
        extensao = alter1[13:17]
        alter2 = alter1[1:8]

        if 'E' in alter2 and extensao == '.JPG':
            print('EXIGENCIA E PLANTA')
        elif 'E' in alter2 and extensao =='pdf':
            print('EXIGENCIA DOC')
        elif 'R' in alter2:
            print('REGISTRO')
        else:
            print('ALGUM PROBLEMA')


def not_found(label):
    print(f"Element not found: {label}")
if __name__ == '__main__':
    main()