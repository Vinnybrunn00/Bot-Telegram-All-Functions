from debug import Help, Connected, Scan, QRCODE, Creator, Calculator
from rich.console import Console
from mytoken import TeleToken
from rich import print
import pytesseract
import telebot
import qrcode
import time
import cv2
import os

clear = 'clear' if os.name == 'posix' else 'cls'
os.system(clear)

with Console().status('Starting...'):
    time.sleep(1.5)

bot = telebot.TeleBot(TeleToken())
@bot.message_handler(commands=['start', 'help'])
def Start(message):
    Help(message)

Connected()
@bot.message_handler(content_types=['photo'])
def Scanner(message):
    # Extract text from image
    if not message.caption != '!scan':
        Scan(message)
        foto = bot.get_file(message.photo[1].file_id)
        download = bot.download_file(foto.file_path)

        with open('image.jpg', 'wb') as photo:
            photo.write(download)
        
        try:
            img = cv2.imread('image.jpg')
            string = pytesseract.image_to_string(img)
            if not string == '':
                bot.reply_to(message, string)
            else:
                bot.reply_to(message, 'Scanner error')

        except telebot.apihelper.ApiTelegramException:
            print(
                '[red] > Excepiton error < [/]\n'
                )
            bot.reply_to(message, 'Nothing to scan here!')

        photo.close()

@bot.message_handler(content_types=['text'])
def All_func_text(message):
    # QRcode
    try:
        if '!qrcode' in message.text:
            text_user = message.text
            link = text_user[8:]
            QRCODE(message) # debug in ./debug.py

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.ERROR_CORRECT_L,
                box_size=10,
                border=4
            )
            qr.add_data(link)
            qr.make(fit=True)
            img = qr.make_image(
                fill_color='black',
                back_color='white'
            )
            img.save('QRCODE.png')
            imagem = open('QRCODE.png', 'rb')
            bot.send_photo(message.chat.id, imagem)
    except:
        bot.send_message(message.chat.id, 'Use um link válido')
        print(
            '[red] > Excepiton error < [/]\n'
            )

    # creator       
    if '!creator' in message.text:
        try:
            Creator(message)
            bot.send_message(message.chat.id, 'Aqui estar o contado do meu criador')
            bot.send_contact(message.chat.id, '5574988562578', message.chat.first_name)
        except:
            print(
                '[red] > Excepiton error < [/]\n'
                )

    # Calculator
    operadores = '+-÷x'
    for operador in operadores:
        try:
            if operador in message.text:
                value = message.text
                mensagem = str(value)
                Calculator(message) # debug in ./debug.py

                if '+' in mensagem:
                    posicao = mensagem.find('+')
                    soma = (int(value[:posicao]) + int(value[posicao+1:]))
                    bot.reply_to(message, f'Resolvi sua equação 🤖\n\n{int(value[:posicao])}+{int(value[posicao+1:])} = {soma}')

                elif '-' in mensagem:
                    posicao1 = mensagem.find('-')
                    sub = (int(value[:posicao1]) - int(value[posicao1+1:]))
                    bot.reply_to(message, f'Resolvi sua equação 🤖\n\n{int(value[:posicao1])}-{int(value[posicao1+1:])} = {sub}')

                elif '÷' in mensagem:
                    posicao2 = mensagem.find('÷')
                    div = (int(value[:posicao2]) / int(value[posicao2+1:]))
                    bot.reply_to(message, f'Resolvi sua equação 🤖\n\n{int(value[:posicao2])}÷{int(value[posicao2+1:])} = {div}')

                elif '*' in mensagem:
                    posicao3 = mensagem.find('*')
                    multi = (int(value[:posicao3]) * int(value[posicao3+1:]))
                    bot.reply_to(message, f'Resolvi sua equação 🤖\n\n{int(value[:posicao3])}x{int(value[posicao3+1:])} = {multi}')

        except:
            print(
                '[red]> Exception error <[/]'
                )
            bot.send_message(message.chat.id, 'error')

bot.infinity_polling()