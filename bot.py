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
    caminho = 'c:\Transcricao'
    folder = BotFilesPlugin()
    arquivos = folder.get_all_file_paths(directory_path=caminho)
    # print(arquivos)

    for tr in arquivos:
        transcricao = tr
        print(transcricao)
        alter1 = transcricao.replace('c:\Transcricao', '')
        alter2 = alter1[1:]
        alter3 = alter2.replace('.pdf','')
        #print(alter3)
        numero = alter3
        
        if not bot.find( "localiza", matching=0.97, waiting_time=10000):
            not_found("localiza")
        bot.double_click_relative(84, 41)
        bot.kb_type(text=numero)
        bot.enter()
        bot.enter()
        bot.enter()
        if bot.find( "digitalizar", matching=0.97, waiting_time=10000):
            bot.click()
            bot.wait(2000)
            bot.type_keys(['alt','e','i'])
            bot.wait(1000)
            bot.type_keys(['alt','t'])
            bot.wait(1000)
            bot.type_key('p')
            bot.wait(1000)
            bot.type_keys(['alt','n'])
            bot.wait(1000)
            bot.kb_type(text=transcricao)
            bot.wait(1000)
            bot.type_keys(['alt','a'])
            bot.wait(1000)
            while bot.find("aguardando"):
                bot.wait(5000)
            else:
                if not bot.find( "sair", matching=0.97, waiting_time=10000):
                    not_found("sair")
                bot.click()

        else:
            print('tem imagem')
            pass

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
