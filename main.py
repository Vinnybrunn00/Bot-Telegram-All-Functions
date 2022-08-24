from debug import Help, Connected, Welcome_, Delallmessage, Scan, QRCODE, Creator, Calculator
from telebot.async_telebot import AsyncTeleBot
from rich.console import Console
from translate import Translator
from telebot import types, util
from mytoken import TeleToken
from gtts import gTTS
import pytesseract
import telebot
import asyncio
import qrcode
import time
import cv2
import os

clear = 'clear' if os.name == 'posix' else 'cls'
os.system(clear)

with Console().status('Starting...'):
    time.sleep(1.5)

bot = AsyncTeleBot(TeleToken())
@bot.message_handler(commands=['start', 'help'])
def Start(message):
    Help(message) # debug in ./debug.py

Connected() # debug in ./debug.py
lista = ['xigamentos']

#Welcome
@bot.message_handler(content_types=['new_chat_members'])
async def Welcome(message):
    Welcome_() # debug in ./debug.py
    try:
        new_member = message.json['new_chat_member']['username']
        info_group = message.json['chat']['title']
        await bot.send_message(
            message.chat.id, f'Boas vindas do Hubber, @{new_member}🤖, você foi adicionado ao grupo: *{info_group}*', parse_mode='Markdown')
    except:
        print('Não consegui dá boas vindas :(')

# delete message
@bot.message_handler(content_types=[f'{util.content_type_service}', 'text'])
async def Delete_message(message: types.Message):
    Delallmessage(message) # debug in ./debug.py
    try:
        for palavrao in lista:
            if palavrao in message.text.lower():
                mensagem_id = message.message_id
                await bot.delete_message(message.chat.id, mensagem_id)
    except:
        await bot.send_message(message.chat.id, 'Me torne admin para eu apagar mensagens não desejadas')

    #qrcode gerator
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
            await bot.send_photo(message.chat.id, imagem)
    except:
        await bot.send_message(message.chat.id, 'Use um link válido')
        print(
            '[red] > Excepiton error < [/]\n'
            )

    # voice with text
    if '!voz' in message.text:
        command = message.text
        save_voice = 'voice.mp3'
        try:
            voice = gTTS(
                text=f'{command[5:]}',
                lang='pt-br'
            )
            voice.save(save_voice)
            await bot.send_voice(message.chat.id, open(f'{save_voice}', 'rb'))
        except:
            print(
            '[red] > Excepiton error < [/]\n'
                )
    # Translate bot           
    if '!translate' in message.text:
        trans = message.text
        try:
            if trans[11:13] != '':
                if trans[11:13] == 'eng':
                    translate_eng = Translator(from_lang='pt-br', to_lang='english')
                    ingles = translate_eng(f'{trans[15:]}')
                    await bot.send_message(message.chat.id, ingles)

                elif trans[11:13] == 'esp':
                    translate_esp = Translator(from_lang='pt-br', to_lang='es-ES')
                    espanhol = translate_esp(f'{trans[15:]}')
                    await bot.send_message(message.chat.id, espanhol)
                
                elif trans[11:13] == 'fra':
                    translate_fra = Translator(from_lang='pt-br', to_lang='fr-FR')
                    frances = translate_fra(f'{trans[15:]}')
                    await bot.send_message(message.chat.id, frances)
                
                elif trans[11:13] == 'ger':
                    translate_ger = Translator(from_lang='pt-br', to_lang='de_DE')
                    alemao = translate_ger(f'{trans[15:]}')
                    await bot.send_message(message.chat.id, alemao)

            else:
                await bot.send_message(message.chat.id, 
                'Inclua o código do idioma\n\nExemplo: !translate eng sua frase')

        except:
            print(
            '[red] > Excepiton error < [/]\n'
                )

    #creator        
    if '!creator' in message.text:
        try:
            Creator(message) # debug in ./debug.py
            await bot.send_message(message.chat.id, 'Aqui estar o contado do meu criador')
            await bot.send_contact(message.chat.id, '5574988562578', message.chat.first_name)
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
                    await bot.reply_to(message, f'Resolvi sua equação 🤖\n\n{int(value[:posicao])}+{int(value[posicao+1:])} = {soma}')

                elif '-' in mensagem:
                    posicao1 = mensagem.find('-')
                    sub = (int(value[:posicao1]) - int(value[posicao1+1:]))
                    await bot.reply_to(message, f'Resolvi sua equação 🤖\n\n{int(value[:posicao1])}-{int(value[posicao1+1:])} = {sub}')

                elif '÷' in mensagem:
                    posicao2 = mensagem.find('÷')
                    div = (int(value[:posicao2]) / int(value[posicao2+1:]))
                    await bot.reply_to(message, f'Resolvi sua equação 🤖\n\n{int(value[:posicao2])}÷{int(value[posicao2+1:])} = {div}')

                elif '*' in mensagem:
                    posicao3 = mensagem.find('*')
                    multi = (int(value[:posicao3]) * int(value[posicao3+1:]))
                    await bot.reply_to(message, f'Resolvi sua equação 🤖\n\n{int(value[:posicao3])}x{int(value[posicao3+1:])} = {multi}')

        except:
            print(
                '[red]> Exception error <[/]'
                )
            await bot.send_message(message.chat.id, 'error')

# Extract text from image
@bot.message_handler(content_types=['photo'])
async def Scanner(message):
    if not message.caption != '!scan':
        Scan(message) # debug in ./debug.py
        foto = bot.get_file(message.photo[1].file_id)
        download = bot.download_file(foto.file_path)

        with open('image.jpg', 'wb') as photo:
            photo.write(download)
        
        try:
            img = cv2.imread('image.jpg')
            string = pytesseract.image_to_string(img)
            if not string == '':
                await bot.reply_to(message, string)
            else:
                await bot.reply_to(message, 'Scanner error')

        except telebot.apihelper.ApiTelegramException:
            print(
                '[red] > Excepiton error < [/]\n'
                )
            await bot.reply_to(message, 'Nothing to scan here!')

        photo.close()
    
asyncio.run(bot.polling(non_stop=True))
