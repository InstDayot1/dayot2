
from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait
import os
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
import time
from time import sleep
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
app = Client('dedinside-session', api_id=1016382, api_hash='c27834e5683d50a9bacf835a95ec4763')

app.start()

app.stop()
print('''
      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
      ┃       Made by dayot               Созданно dayot        ┃
      ┃  Instagram: @d.dayot1     ┃
      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


''')
print("После ввода задержки напишите в любой телеграм чат команду \n --Команды-- \n.dd 0 \n.night 0 \n.love 0\n.heart 0\n.inside 0\n.toxic 0")
print("\n МЫ НЕ НЕСЕМ ОТВЕТСВЕННОСТИ ЗА ВАШИ ДЕЙСТВИЯ!")
print()
cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
if cool == 0:
    print("Слишком быстро!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
if cool > 10:
    print("Слишком медленно!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
if cool < 5:
    print("Слишком быстро!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость(Норма 8):  "))


@app.on_message(filters.command("dd", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = textded.split("\n")
    e = True
    etime = int(msg.text.split('.dd ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</>')
                sleep(0.5)
                msg.delete()
            except:
               pass
        else:
            try:
                msg.edit(f'❤️{i} ❤️')
                sleep(time/cool)
                msg.edit(f'🧡 {i} 🧡')
                sleep(time/cool)
                msg.edit(f'💛 {i} 💛')
                sleep(time/cool)
                msg.edit(f'💚 {i} 💚')
                sleep(time/cool)
                msg.edit(f'💙 {i} 💙')
                sleep(time/cool)
                msg.edit(f'💜 {i} 💜')
                sleep(time/cool)
                msg.edit(f'🖤 {i} 🖤')
                sleep(time/cool)
                msg.edit(f'🤍 {i} 🤍')
                sleep(time/cool)
            except:
                pass
    msg.edit(f'<b> ⭐ inst: d.dayot1</b>')

textded = '''
<b>доброе утро зайка</b> 
<b>доброе утро солнышко</b> 
<b>доброе утро котёнок</b> 
<b>доброе утро цветочек</b> 
<b>доброе утро ангелочек</b> 
<b>доброе утро принцесса</b> 
<b>доброе утро красотка</b> 
<b>доброе утро милашк</b> 
<b>доброе утро симпатяжка</b> 
<b>доброе утро бусинка</b> 
❤ <b>я</b> ❤
<b>💚 тебя 💚</b>
<b>💙 очень 💙</b>
<b>💛 сильно 💛</b>
<b>💜 люблю 💜</b>
'''

textded1 = '''
<b>спокойной ночи зайка</b> 💚
<b>спокойной ночи солнышко</b> 💛
<b>спокойной ночи котёнок</b> ❤
<b>спокойной ночи цветочек</b> 💙
<b>спокойной ночи ангелочек</b> 💜
<b>спокойной ночи принцесса</b> 💓
<b>спокойной ночи красотка</b> 💕 
<b>спокойной ночи милашк</b>а 💖 
<b>спокойной ночи симпатяжка</b> 💗
<b>спокойной ночи бусинка</b> 💘
❤ <b>я</b> ❤
<b>💚 тебя 💚</b>
<b>💙 очень 💙</b>
<b>💛 сильно 💛</b>
<b>💜 люблю 💜</b>
'''

@app.on_message(filters.command("night", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = textded1.split("\n")
    e = True
    etime = int(msg.text.split('.night ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    msg.edit(f'<b> ⭐ inst: d.dayot1</b>')

textded2 ='''
<b>ты лучшая</b> 💚
<b>ты солнышко</b> 💛
<b>ты котёнок</b> ❤
<b>ты милашкarrrr</b> 💙
<b>ты ангелочек</b> 💜
<b>ты принцесса</b> 💓
<b>ты красотка</b> 💕 
<b>ты милашк</b>а 💖 
<b>ты симпатяжка</b> 💗
<b>ты бусинка</b> 💘
❤ <b>я</b> ❤
<b>💚 тебя 💚</b>
<b>💙 очень 💙</b>
<b>💛 сильно 💛</b>
<b>💜 люблю 💜</b>
<b>🫀 и уважаю 🫀</b>
'''

@app.on_message(filters.command("rep", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = textded2.split("\n")
    e = True
    etime = int(msg.text.split('.rep ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    msg.edit(f'<b> ⭐ inst: d.dayot1</b>')
    
@app.on_message(filters.command("love", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = love.split("\n")
    e = True
    etime = int(msg.text.split('.love', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    msg.edit(f'<b> ⭐ inst : d.dayot1</b>')

love = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
<b>Загрузка любви...</b>
❤️🤍🤍🤍🤍🤍🤍🤍🤍🤍
❤️❤️🤍🤍🤍🤍🤍🤍🤍🤍
❤️❤️❤️🤍🤍🤍🤍🤍🤍🤍
❤️❤️❤️❤️🤍🤍🤍🤍🤍🤍
❤️❤️❤️❤️❤️🤍🤍🤍🤍🤍
❤️❤️❤️❤️❤️❤️🤍🤍🤍🤍
❤️❤️❤️❤️❤️❤️❤️🤍🤍🤍
❤️❤️❤️❤️❤️❤️❤️❤️🤍🤍
❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
'''
end_message = '<b> ⭐ inst : d.dayot</b>'

@app.on_message(filters.command("heart", prefixes=".") & filters.me)
def betalove(_, msg):
    time = 0.6
    for i in range(3):
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
        sleep(1)
        msg.edit(f'<b>⭐️ inst : d.dayot1</b>')
        msg.edit(f'<b>⭐️ inst : d.dayot1</b>')

@app.on_message(filters.command("inside", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = inside.split("\n")
    e = True
    etime = int(msg.text.split('.inside ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    msg.edit(f'<b> ⭐ inst: d.dayot1</b>')

inside = '''
<b>солнышко не грусти пожалуйста!</b> ❤️
<b>леончик не грусти пожалуйста!</b> 💗
<b>бусинка не грусти пожалуйста!</b> 🤍
<b>леончик не грусти пожалуйста!</b> 💜
<b>булочка не грусти пожалуйста!</b> 💖
<b>принцесска не грусти пожалуйста!</b> 💘
<b>красоточка не грусти пожалуйста!</b> 💕
<b>симпатяжечка не грусти пожалуйста!</b> 💓
<b>ты мне<b> 🖤
<b>очень сильно<b> 💙
<b>нравишься!!!<b>💚
<b> не грусти пожалуйста!!!<b> 💛
'''

@app.on_message(filters.command("toxic", prefixes=".") & filters.me)
def valentine(app, message):
    app.send_message(message.chat.id,f'''
<b>помолчи хуета, сиди в обиде ребёнок мертвой шалавы</b>
''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии.</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>пиздобратия мандопроушечная, уебище залупоглазое</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>дрочепиздище хуеголовое, пробиздоблядская мандопроушина</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>гнидопаскудная хуемандовина</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>ах ты блядь семитаборная чтоб тебя всем столыпином харили</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>охуевшее блядепиздопроёбище чтоб ты хуем поперхнулся долбоебическая пиздорвань</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>хуй тебе в глотку через анальный проход</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>распизди тебя тройным перебором через вторичный переёб пиздоблятское хуепиздрическое мудовафлоебище сосущее километры трипперных членов</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>трихломидозопиздоеблохуе блядеперепиздическая спермоблевотина</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>гандон с гонореей...</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>да разъебись ты троебучим проебом сперматоблятская пиздапроебина </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>охуевающая в своей пидарастической сущности похожаю на ебущегося в жопу енота </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>сортирующего яйца в пизде кастрированной кобылы</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>хуелептический пиздопрозоид, еблоухий мандохвост</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ебун хуеголовый, пидрасня ебаная. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Залупоголовая блядоящерица. .</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Трипиздоблядская промудохуина! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Распроеб твою в крестище через коромысло в копейку мать! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Что за блядская пиздопроебина, охуевающая своей пидорестической заебучестью невъебенной степени охуения. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Мордоблядина залупоглазая.  блядского невъебения! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Шлюшья мразота приохуебенивающая от собственного недохуеплетского злоетрахания. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Да произпездуй с 2000 этажа своей припиздоблядской тушей на землю в труху! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Трипиздоблядское мудопроебное трипиздие, ебоблядище охуевающее от собственной злоебучести.  </b>
     ''')
     sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ебаквакнутый распиздаеб... </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Хуесосляблядивый расхуйдяй припиздоблядского четвертоногого происхождения </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>прошу завали свой хуеобрыганский блядозвукоговоритель. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Промудохуепиздамразоблядское злоепиздие </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ебоблядищая пиздопроебина сама ахуевающее от того какая оно пездоблядехуепроклятое.</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Обосробосанная пиздоблядмна двадцати головая семихуюлина припиздовывающее от хуеглотности своей трипиздговноглоталки.</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Облямудевшая хуеблядина четырестохуйная</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>вестипёздная мразотоблядская шлюхасосалка. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Хуесосная мудохуепиздопроебная мудаблядина сука безмаманя </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>блядь шмара козельуебок сдохни </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>хуесоска  ебланафт чмырь пидорска манда тупая гандопляс пидрила ебалай долбоеб обмудок овцееб дауниха  </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ненавижу гомодрилла сучка шлюха трахарила гавносос миньетчик </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>пидэраст пиздоеб хуеплет кончиглот ебище сын шлюхи гавноеб мудяра </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>еботрон вафлеглот ебалдуй захуятор имбицил подонок пиздопромудище </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>выебок ахуяэетер ебозер пиздолиз злоуебок хуиман ебил долбоебина пиндос мудазвон </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>хуеб амеба хуйло хуила пиздорвань смесь ебланства и говна ебанат </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>умалишенный дегенерат мандопроушина очкоблут порванный обрубок хуяраспиздяй свинозалупа</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>семиголовый восьмихуй ебоблядище свинохуярище вафлепиздище хуй лохматый жопа рванная мудопроеб </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>страхапиздище ебосос дурфанка косоуебище долбоногий лихохуетень</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>⭐️ inst : d.dayot1</b>

app.run()
