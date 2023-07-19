from botcity.plugins.excel import BotExcelPlugin
from botcity.plugins.files import BotFilesPlugin
from botcity.plugins.email import BotEmailPlugin
import logging
logging.basicConfig(level=logging.INFO, filename=r'c:\log\log.txt', format="%(asctime)s $ %(message)s", datefmt='%d/%m/%Y %I:%M:%S %p')


# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Instantiate the plugin
    email = BotEmailPlugin()

    # Configure IMAP with the gmail server
    #email.configure_imap("mail.3ribh.com", 993)

    # Configure SMTP with the gmail server
    email.configure_smtp("mail.3ribh.com", 587)

    # Login with a valid email account
    email.login("", "")



    bot = DesktopBot()
    caminho = 'c:\Tr'
    folder = BotFilesPlugin()
    arquivos = folder.get_all_file_paths(directory_path=caminho)

    for tr in arquivos:
        alter1 = tr.replace('c:\Tr', '')
        extensao = alter1[13:17]
        alter2 = alter1[1:8]

        to = ["rafael@3ribh.com", "<RECEIVER_ADDRESS_2>"]
        subject = "Falha na Validação dos Arquivos"
        body = "Verificar o arquivo log com os erros"
        files = ["c:\log\log.txt"]


        if 'E' in alter2 and extensao == '.JPG':
            print('EXIGENCIA E PLANTA')
        elif 'E' in alter2 and extensao =='pdf':
            print('EXIGENCIA DOC')
        elif 'R' in alter2:
            print('REGISTRO')
        else:
            print('ALGUM PROBLEMA')
            logging.warning(f'ARQUIVO {tr}')
            email.send_message(subject, body, to, attachments=files)


def not_found(label):
    print(f"Element not found: {label}")
if __name__ == '__main__':
    main()
