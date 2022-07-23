from mytoken import TeleToken
from telebot import TeleBot
from rich import print
import pyfiglet as pg

bot = TeleBot(TeleToken())
banner = pg.figlet_format('HubberBot')

def Help(message):
    bot.send_message(message.chat.id, '''
        -------------------- ☾ 🤖 *COMMANDS MENU* 🤖☽ --------------------
        *!scan* -> Extract text from an image
                  _exemple_ : *!scan + imagem*
        *!qrcode* -> Returns image of the qrcode through the link
                  _exemple_ : *!qrcode + link*
        *!creator* -> Return developer contact
        ''', parse_mode='Markdown'
                )

def Connected():
    print(f'[bold]{banner}[/]')
    print(f'[blue]:heavy_check_mark: Connected!\n')


def Welcome_():
    print(
        '-------------------------------------'
        '\nMethod: [purple]Welcome[/]\n'
                )

def Delallmessage(message):
    print(
        '-------------------------------------'
        f'\nUsername: [cyan]{message.from_user.first_name}[/]\n'
        f'Message: [blue][italic]{message.text}[/]\n'
        f'Method: [purple]Delete Message[/]\n'
            )

def Scan(message):
    print(
        '-------------------------------------'
        f'\nUsername: [cyan]{message.from_user.first_name}[/]\n'
        f'Command: [blue][italic]{message.caption}[/]\n'
        f'Method: [purple]Scanner[/]\n'
            )

def QRCODE(message):
    print(
    '-------------------------------------'
    f'\nUsername: [cyan]{message.from_user.first_name}[/]\n'
    f'Site: [blue][italic]{message.text}[/]\n'
    f'Method: [purple]QRcode[/]\n'
        )
    
def Creator(message):
    print(
    '-------------------------------------'
    f'\nUsername: [cyan]{message.from_user.first_name}[/]\n'
    f'Command: [blue][italic]{message.caption}[/]\n'
    f'Method: [purple]Creator[/]\n'
        )

def Calculator(message):
    print(
    '-------------------------------------'
    f'\nUsername: [cyan]{message.from_user.first_name}[/]\n'
    f'Site: [blue][italic]{message.text}[/]\n'
    f'Method: [purple]Calculator[/]\n'
        )
