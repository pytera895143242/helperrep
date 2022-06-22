from aiogram import types
from misc import dp, bot
import sqlite3
from .sqlit import info_members, cheak_traf, cheak_chat_id, reg_links, get_links, obnovatrafika1, obnovatrafika2, obnovatrafika3, \
    obnovatrafika4, obnovatrafika5, obnovatrafika6, obnovatrafika7, obnovatrafika8
import asyncio
import random
from .sqlit import delite_user
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import BotBlocked, ChatNotFound

ADMIN_ID = [1307813926, 494588959]


class reg(StatesGroup):
    name = State()
    fname = State()


class st_reg(StatesGroup):
    st_name = State()
    st_fname = State()
    step_q = State()
    step_regbutton = State()


class del_user(StatesGroup):
    del_name = State()
    del_fname = State()


class generate(StatesGroup):
    step1 = State()
    step2 = State()


class reg_trafik(StatesGroup):
    traf1 = State()
    traf2 = State()


class reg_trafik2(StatesGroup):
    traf1 = State()
    traf2 = State()


class reg_trafik3(StatesGroup):
    traf1 = State()
    traf2 = State()


class reg_trafik4(StatesGroup):
    traf1 = State()
    traf2 = State()


class reg_trafik5(StatesGroup):
    traf1 = State()
    traf2 = State()


class reg_trafik6(StatesGroup):
    traf1 = State()
    traf2 = State()


class reg_trafik7(StatesGroup):
    traf1 = State()
    traf2 = State()


class reg_trafik8(StatesGroup):
    traf1 = State()
    traf2 = State()


@dp.message_handler(commands=['admin'])
async def admin_ka(message: types.Message):
    id = message.from_user.id
    if id in ADMIN_ID:
        markup = types.InlineKeyboardMarkup()

        bat_generator = types.InlineKeyboardButton(text='Генерация строк', callback_data='generate_strok')
        # bat_vie_stat = types.InlineKeyboardButton(text='Просмотр статистики строк', callback_data='vie_stat')
        # bat_posting = types.InlineKeyboardButton(text='Пост во все каналы', callback_data='post_all')
        bat_setin = types.InlineKeyboardButton(text='Настройка трафика', callback_data='settings')

        # bat_j = types.InlineKeyboardButton(text='Скачать базу данных', callback_data='baza')

        markup.add(bat_generator)
        # markup.add(bat_vie_stat)
        markup.add(bat_setin)
        # markup.add(bat_posting)
        # markup.add(bat_j)

        await bot.send_message(message.chat.id, 'Выполнен вход в админ панель', reply_markup=markup)

@dp.callback_query_handler(text='vie_stat')
async def vie_stat(call: types.callback_query, state: FSMContext):
    message_text = " "
    for groop in get_links():
        message_text += f"{groop[0]} -- \n"

    print(message_text)


@dp.callback_query_handler(text='generate_strok')
async def generate_strok1(call: types.callback_query, state: FSMContext):
    await bot.send_message(chat_id=call.message.chat.id, text="Введите имя кнопки")
    await generate.step1.set()


@dp.message_handler(state=generate.step1, content_types=['text', 'photo', 'video'])
async def generate_strok2(message: types.Message, state: FSMContext):
    ids = cheak_chat_id()  # Список ID всех каналов

    if random.randint(1,2) == 1:
        print("Первый закрыт")
        link1 = await bot.create_chat_invite_link(chat_id=ids[0], name = message.text, creates_join_request= True)
        link2 = await bot.create_chat_invite_link(chat_id=ids[1], name = message.text)
        link3 = await bot.create_chat_invite_link(chat_id=ids[2], name = message.text, creates_join_request= True)
        link4 = await bot.create_chat_invite_link(chat_id=ids[3], name = message.text)
        link5 = await bot.create_chat_invite_link(chat_id=ids[4], name = message.text, creates_join_request= True)
        link6 = await bot.create_chat_invite_link(chat_id=ids[5], name = message.text)
        link7 = await bot.create_chat_invite_link(chat_id=ids[6], name = message.text, creates_join_request= True)

    else:
        link1 = await bot.create_chat_invite_link(chat_id=ids[0], name=message.text)
        link2 = await bot.create_chat_invite_link(chat_id=ids[1], name=message.text, creates_join_request= True)
        link3 = await bot.create_chat_invite_link(chat_id=ids[2], name=message.text)
        link4 = await bot.create_chat_invite_link(chat_id=ids[3], name=message.text, creates_join_request= True)
        link5 = await bot.create_chat_invite_link(chat_id=ids[4], name=message.text)
        link6 = await bot.create_chat_invite_link(chat_id=ids[5], name=message.text, creates_join_request= True)
        link7 = await bot.create_chat_invite_link(chat_id=ids[6], name=message.text)



    await bot.send_message(chat_id=message.chat.id, text=f"""<b>👑💞ГДЕ-ТО ЗДЕСЬ СПРЯТАН ДОРОГОЙ КОНТЕНТ ИЗ ДАРКНЕТА:</b>
<b>
1️⃣ {link1.invite_link}
2️⃣ {link2.invite_link}
3️⃣ {link3.invite_link}
4️⃣ {link4.invite_link}
5️⃣ {link5.invite_link}
6️⃣ {link6.invite_link}
7️⃣ {link7.invite_link}</b>

<b><i>(купили его за 19.000₽. впускаем в течении часа и удаляем пока не забанили)</i></b>
""",parse_mode='html')


    await bot.send_message(chat_id=message.chat.id, text= f"""<b>
<a href = '{link1.invite_link}'>💕БУХИЕ СТУДЕНТКИ</a>
<a href = '{link2.invite_link}'>🔥ГОРЯЧИЕ ПИСЮХИ</a>
<a href = '{link3.invite_link}'>💦NE SHKОЛЬNИЦЫ</a>
<a href = '{link4.invite_link}'>🩸ТВОИ ПОДРУГИ</a>
<a href = '{link5.invite_link}'>🥶ПОСЛЕ УРОКОВ</a>
<a href = '{link6.invite_link}'>🤬ЛЕНЕ ПОРВАЛИ АНАЛ</a>
<a href = '{link7.invite_link}'>🇷🇺РУССКАЯ ДОМАШКА</a>


(Обязательно загляни во все каналы🙄💕)</b>""",parse_mode='html')
    await state.finish()


# НАСТРОЙКА ТРАФИКА
@dp.callback_query_handler(text='settings')
async def baza12(call: types.callback_query):
    markup_traf = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='Изменить 1 канал', callback_data='change_trafik1')
    bat_a2 = types.InlineKeyboardButton(text='Изменить 2 канал', callback_data='change_trafik2')
    bat_a3 = types.InlineKeyboardButton(text='Изменить 3 канал', callback_data='change_trafik3')
    bat_a4 = types.InlineKeyboardButton(text='Изменить 4 канал', callback_data='change_trafik4')
    bat_a5 = types.InlineKeyboardButton(text='Изменить 5 канал', callback_data='change_trafik5')
    bat_a6 = types.InlineKeyboardButton(text='Изменить 6 канал', callback_data='change_trafik6')
    bat_a7 = types.InlineKeyboardButton(text='Изменить 7 канал', callback_data='change_trafik7')
    bat_a8 = types.InlineKeyboardButton(text='Изменить 8 канал', callback_data='change_trafik8')

    bat_c = types.InlineKeyboardButton(text='ЗАКРЫТЬ', callback_data='otemena')

    markup_traf.add(bat_a)
    markup_traf.add(bat_a2)
    markup_traf.add(bat_a3)
    markup_traf.add(bat_a4)
    markup_traf.add(bat_a5)
    markup_traf.add(bat_a6)
    markup_traf.add(bat_a7)
    # markup_traf.add(bat_a8)

    markup_traf.add(bat_c)  # close

    list = cheak_traf()
    await bot.send_message(call.message.chat.id, text=f'<b>Список активных каналов на данный момент:</b>\n\n'
                                                      f'Первый канал: {list[0]}\n'
                                                      f'Второй канал: {list[1]}\n'
                                                      f'Третий канал: {list[2]}\n\n'
                                                      f'Четвертый канал: {list[3]}\n'
                                                      f'Пятый канал {list[4]}\n'
                                                      f'Шестой канал: {list[5]}\n'
                                                      f'Седьмой канал: {list[6]}\n', parse_mode='html',
                           reply_markup=markup_traf, disable_web_page_preview=True)


@dp.callback_query_handler(text='change_trafik1')  # Изменение 1-го канала
async def baza12342(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
    markup.add(bat_a)

    await bot.send_message(call.message.chat.id, text='Отправь на 1-й канал\n', parse_mode='html', reply_markup=markup)
    await reg_trafik.traf1.set()


@dp.message_handler(state=reg_trafik.traf1, content_types='text')
async def traf_obnovlenie1(message: types.Message, state: FSMContext):
    await state.update_data(link_one=message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=f'Теперь перешли мне любой пост из этого канала ({message.text})')
    await reg_trafik.traf2.set()


@dp.message_handler(state=reg_trafik.traf2, content_types=['text', 'photo', 'video'])
async def traf_obnovlenie(message: types.Message, state: FSMContext):
    link = await state.get_data()

    link_one = link['link_one']  # Ссылка на канал
    id_channel1 = (message.forward_from_chat.id)  # ID канала

    try:
        obnovatrafika1(link_one, id_channel1)  # Внесение новых каналов в базу данных

        await bot.send_message(chat_id=message.chat.id, text='Обновление успешно')
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        except:
            pass
        await state.finish()

    except:
        await bot.send_message(chat_id=message.chat.id,
                               text='Ошибка! Вы сделали что-то неправильное. Необходимо снова зайти в админ панель и выбрать нужный пункт')
        await state.finish()


# РЕДАКТИРУЕМ ВТОРОЙ КАНАЛ
@dp.callback_query_handler(text='change_trafik2')  # Изменение каналов, на которые нужно подписаться
async def baza12342_2(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
    markup.add(bat_a)

    await bot.send_message(call.message.chat.id, text='Отправь ссылку на второй канал\n', parse_mode='html',
                           reply_markup=markup)
    await reg_trafik2.traf1.set()


@dp.message_handler(state=reg_trafik2.traf1, content_types='text')
async def traf_obnovlenie2(message: types.Message, state: FSMContext):
    await state.update_data(link_one=message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=f'Теперь перешли мне любой пост из этого канала ({message.text})')
    await reg_trafik2.traf2.set()


@dp.message_handler(state=reg_trafik2.traf2, content_types=['text', 'photo', 'video'])
async def traf_obnovlenie_2(message: types.Message, state: FSMContext):
    link = await state.get_data()

    link_one = link['link_one']  # Ссылка на канал
    id_channel2 = (message.forward_from_chat.id)  # ID канала

    try:
        obnovatrafika2(link_one, id_channel2)  # Внесение 2-го новых каналов в базу данных

        await bot.send_message(chat_id=message.chat.id, text='Обновление успешно')
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        except:
            pass
        await state.finish()

    except:
        await bot.send_message(chat_id=message.chat.id,
                               text='Ошибка! Вы сделали что-то неправильное. Необходимо снова зайти в админ панель и выбрать нужный пункт')
        await state.finish()


# РЕДАКТИРУЕМ ТРЕТИЙ КАНАЛ
@dp.callback_query_handler(text='change_trafik3')  # Изменение каналов, на которые нужно подписаться
async def baza12342_3(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
    markup.add(bat_a)

    await bot.send_message(call.message.chat.id, text='Отправь ссылку на третий канал\n', parse_mode='html',
                           reply_markup=markup)
    await reg_trafik3.traf1.set()


@dp.message_handler(state=reg_trafik3.traf1, content_types='text')
async def traf_obnovlenie3(message: types.Message, state: FSMContext):
    await state.update_data(link_one=message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=f'Теперь перешли мне любой пост из этого канала ({message.text})')
    await reg_trafik3.traf2.set()


@dp.message_handler(state=reg_trafik3.traf2, content_types=['text', 'photo', 'video'])
async def traf_obnovlenie_3(message: types.Message, state: FSMContext):
    link = await state.get_data()

    link_one = link['link_one']  # Ссылка на канал
    id_channel3 = (message.forward_from_chat.id)  # ID канала

    try:
        obnovatrafika3(link_one, id_channel3)  # Внесение 3-го новых каналов в базу данных
        await bot.send_message(chat_id=message.chat.id, text='Обновление успешно')
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        except:
            pass
        await state.finish()

    except:
        await bot.send_message(chat_id=message.chat.id,
                               text='Ошибка! Вы сделали что-то неправильное. Необходимо снова зайти в админ панель и выбрать нужный пункт')
        await state.finish()


# РЕДАКТИРУЕМ первый КАНАЛ
@dp.callback_query_handler(text='change_trafik4')  # Изменение каналов, на которые нужно подписаться
async def baza12342_4(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
    markup.add(bat_a)

    await bot.send_message(call.message.chat.id, text='Отправь ссылку четвертый канал\n', parse_mode='html',
                           reply_markup=markup)
    await reg_trafik4.traf1.set()


@dp.message_handler(state=reg_trafik4.traf1, content_types='text')
async def traf_obnovlenie44(message: types.Message, state: FSMContext):
    await state.update_data(link_one=message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=f'Теперь перешли мне любой пост из этого канала ({message.text})')
    await reg_trafik4.traf2.set()


@dp.message_handler(state=reg_trafik4.traf2, content_types=['text', 'photo', 'video'])
async def traf_obnovlenie_4(message: types.Message, state: FSMContext):
    link = await state.get_data()

    link_one = link['link_one']  # Ссылка на канал
    id_channel4 = (message.forward_from_chat.id)  # ID канала

    try:
        obnovatrafika4(link_one, id_channel4)  # Внесение 2-го новых каналов в базу данных

        await bot.send_message(chat_id=message.chat.id, text='Обновление успешно')
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        except:
            pass
        await state.finish()

    except:
        await bot.send_message(chat_id=message.chat.id,
                               text='Ошибка! Вы сделали что-то неправильное. Необходимо снова зайти в админ панель и выбрать нужный пункт')
        await state.finish()


# РЕДАКТИРУЕМ второй КАНАЛ
@dp.callback_query_handler(text='change_trafik5')  # Изменение каналов, на которые нужно подписаться
async def baza12342_5(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
    markup.add(bat_a)

    await bot.send_message(call.message.chat.id, text='Отправь ссылку на новый, пятый по счету канал\n',
                           parse_mode='html', reply_markup=markup)
    await reg_trafik5.traf1.set()


@dp.message_handler(state=reg_trafik5.traf1, content_types='text')
async def traf_obnovlenie5(message: types.Message, state: FSMContext):
    await state.update_data(link_one=message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=f'Теперь перешли мне любой пост из этого канала ({message.text})')
    await reg_trafik5.traf2.set()


@dp.message_handler(state=reg_trafik5.traf2, content_types=['text', 'photo', 'video'])
async def traf_obnovlenie_5(message: types.Message, state: FSMContext):
    link = await state.get_data()

    link_one = link['link_one']  # Ссылка на канал
    id_channel5 = (message.forward_from_chat.id)  # ID канала

    try:
        obnovatrafika5(link_one, id_channel5)  # Внесение 5-го новых каналов в базу данных

        await bot.send_message(chat_id=message.chat.id, text='Обновление успешно')
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        except:
            pass
        await state.finish()

    except:
        await bot.send_message(chat_id=message.chat.id,
                               text='Ошибка! Вы сделали что-то неправильное. Необходимо снова зайти в админ панель и выбрать нужный пункт')
        await state.finish()


# Конец обновлялки каналов

@dp.callback_query_handler(text='baza')
async def baza(call: types.callback_query):
    a = open('server.db', 'rb')
    await bot.send_document(chat_id=call.message.chat.id, document=a)


@dp.callback_query_handler(text='list_members')  # АДМИН КНОПКА ТРАФИКА
async def check(call: types.callback_query):
    a = info_members()  # Вызов функции из файла sqlit
    await bot.send_message(call.message.chat.id, f'<b>Количество пользователей: {a[0]}</b>\n\n'
                                                 f'Прошли прогрев: {a[1]}\n'
                                                 f'Прогреваются: {a[2]}')


# РЕДАКТИРУЕМ третий КАНАЛ
@dp.callback_query_handler(text='change_trafik6')  # Изменение каналов, на которые нужно подписаться
async def baza12342_53(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
    markup.add(bat_a)

    await bot.send_message(call.message.chat.id, text='Отправь ссылку на новый, шестой по счету канал\n',
                           parse_mode='html', reply_markup=markup)
    await reg_trafik6.traf1.set()


@dp.message_handler(state=reg_trafik6.traf1, content_types='text')
async def traf_obnovlenie53(message: types.Message, state: FSMContext):
    await state.update_data(link_one=message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=f'Теперь перешли мне любой пост из этого канала ({message.text})')
    await reg_trafik6.traf2.set()


@dp.message_handler(state=reg_trafik6.traf2, content_types=['text', 'photo', 'video'])
async def traf_obnovlenie_53(message: types.Message, state: FSMContext):
    link = await state.get_data()

    link_one = link['link_one']  # Ссылка на канал
    id_channel5 = (message.forward_from_chat.id)  # ID канала

    try:
        obnovatrafika6(link_one, id_channel5)  # Внесение 5-го новых каналов в базу данных

        await bot.send_message(chat_id=message.chat.id, text='Обновление успешно')
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        except:
            pass
        await state.finish()

    except:
        await bot.send_message(chat_id=message.chat.id,
                               text='Ошибка! Вы сделали что-то неправильное. Необходимо снова зайти в админ панель и выбрать нужный пункт')
        await state.finish()


# РЕДАКТИРУЕМ четвертый КАНАЛ
@dp.callback_query_handler(text='change_trafik7')  # Изменение каналов, на которые нужно подписаться
async def baza12342_54(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
    markup.add(bat_a)

    await bot.send_message(call.message.chat.id, text='Отправь ссылку на новый, седьмой по счету канал\n',
                           parse_mode='html', reply_markup=markup)
    await reg_trafik7.traf1.set()


@dp.message_handler(state=reg_trafik7.traf1, content_types='text')
async def traf_obnovlenie54(message: types.Message, state: FSMContext):
    await state.update_data(link_one=message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=f'Теперь перешли мне любой пост из этого канала ({message.text})')
    await reg_trafik7.traf2.set()


@dp.message_handler(state=reg_trafik7.traf2, content_types=['text', 'photo', 'video'])
async def traf_obnovlenie_54(message: types.Message, state: FSMContext):
    link = await state.get_data()

    link_one = link['link_one']  # Ссылка на канал
    id_channel5 = (message.forward_from_chat.id)  # ID канала

    try:
        obnovatrafika7(link_one, id_channel5)  # Внесение 5-го новых каналов в базу данных

        await bot.send_message(chat_id=message.chat.id, text='Обновление успешно')
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        except:
            pass
        await state.finish()

    except:
        await bot.send_message(chat_id=message.chat.id,
                               text='Ошибка! Вы сделали что-то неправильное. Необходимо снова зайти в админ панель и выбрать нужный пункт')
        await state.finish()


# РЕДАКТИРУЕМ пятый КАНАЛ
@dp.callback_query_handler(text='change_trafik8')  # Изменение каналов, на которые нужно подписаться
async def baza12342_55(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
    markup.add(bat_a)

    await bot.send_message(call.message.chat.id, text='Отправь ссылку на новый, восьмой по счету канал\n',
                           parse_mode='html', reply_markup=markup)
    await reg_trafik8.traf1.set()


@dp.message_handler(state=reg_trafik8.traf1, content_types='text')
async def traf_obnovlenie55(message: types.Message, state: FSMContext):
    await state.update_data(link_one=message.text)
    await bot.send_message(chat_id=message.chat.id,
                           text=f'Теперь перешли мне любой пост из этого канала ({message.text})')
    await reg_trafik8.traf2.set()


@dp.message_handler(state=reg_trafik8.traf2, content_types=['text', 'photo', 'video'])
async def traf_obnovlenie_55(message: types.Message, state: FSMContext):
    link = await state.get_data()

    link_one = link['link_one']  # Ссылка на канал
    id_channel5 = (message.forward_from_chat.id)  # ID канала

    try:
        obnovatrafika8(link_one, id_channel5)  # Внесение 5-го новых каналов в базу данных

        await bot.send_message(chat_id=message.chat.id, text='Обновление успешно')
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        except:
            pass
        await state.finish()

    except:
        await bot.send_message(chat_id=message.chat.id,
                               text='Ошибка! Вы сделали что-то неправильное. Необходимо снова зайти в админ панель и выбрать нужный пункт')
        await state.finish()


# Конец обновлялки каналов

@dp.callback_query_handler(text='baza')
async def baza(call: types.callback_query):
    a = open('server.db', 'rb')
    await bot.send_document(chat_id=call.message.chat.id, document=a)


@dp.callback_query_handler(text='list_members')  # АДМИН КНОПКА ТРАФИКА
async def check(call: types.callback_query):
    a = info_members()  # Вызов функции из файла sqlit
    await bot.send_message(call.message.chat.id, f'Количество пользователей: {a}')


########################  Рассылка  ################################
@dp.callback_query_handler(text='write_message')  # АДМИН КНОПКА Рассылка пользователям
async def check(call: types.callback_query, state: FSMContext):
    murkap = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='Всем', callback_data='rasl_all')
    bat1 = types.InlineKeyboardButton(text='Кто прошел все прогревы', callback_data='rasl_activ')
    bat2 = types.InlineKeyboardButton(text='Кто прогревается', callback_data='rasl_pasiv')
    murkap.add(bat0)
    murkap.add(bat1)
    murkap.add(bat2)

    await bot.send_message(call.message.chat.id, 'Кому будем делать рассылку?', reply_markup=murkap)
    await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text_startswith='rasl_')  # АДМИН КНОПКА Рассылка пользователям
async def check(call: types.callback_query, state: FSMContext):
    if call.data == 'rasl_all':
        await state.update_data(rasl='all')
    if call.data == 'rasl_activ':
        await state.update_data(rasl='activ')
    if call.data == 'rasl_pasiv':
        await state.update_data(rasl='pasiv')

    murkap = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
    murkap.add(bat0)
    await bot.send_message(call.message.chat.id, 'Перешли мне уже готовый пост и я разошлю его всем юзерам',
                           reply_markup=murkap)
    await st_reg.step_q.set()
    await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text='otemena', state='*')
async def otmena_12(call: types.callback_query, state: FSMContext):
    await bot.send_message(call.message.chat.id, 'Отменено')
    await state.finish()
    await bot.answer_callback_query(call.id)


@dp.message_handler(state=st_reg.step_q,
                    content_types=['text', 'photo', 'video', 'video_note', 'voice'])  # Предосмотр поста
async def redarkt_post(message: types.Message, state: FSMContext):
    await st_reg.st_name.set()
    murkap = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
    bat1 = types.InlineKeyboardButton(text='РАЗОСЛАТЬ', callback_data='send_ras')
    bat2 = types.InlineKeyboardButton(text='Добавить кнопки', callback_data='add_but')
    murkap.add(bat1)
    murkap.add(bat2)
    murkap.add(bat0)

    await message.copy_to(chat_id=message.chat.id)
    q = message
    await state.update_data(q=q)

    await bot.send_message(chat_id=message.chat.id, text='Пост сейчас выглядит так 👆', reply_markup=murkap)


# НАСТРОЙКА КНОПОК
@dp.callback_query_handler(text='add_but', state=st_reg.st_name)  # Добавление кнопок
async def addbutton(call: types.callback_query, state: FSMContext):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await bot.send_message(call.message.chat.id, text='Отправляй мне кнопки по принципу Controller Bot')
    await st_reg.step_regbutton.set()
    await bot.answer_callback_query(call.id)


@dp.message_handler(state=st_reg.step_regbutton, content_types=['text'])  # Текст кнопок в неформате
async def redarkt_button(message: types.Message, state: FSMContext):
    arr3 = message.text.split('\n')
    murkap = types.InlineKeyboardMarkup()  # Клавиатура с кнопками

    massiv_text = []
    massiv_url = []

    for but in arr3:
        new_but = but.split('-')
        massiv_text.append(new_but[0][:-1])
        massiv_url.append(new_but[1][1:])
        bat9 = types.InlineKeyboardButton(text=new_but[0][:-1], url=new_but[1][1:])
        murkap.add(bat9)

    try:
        data = await state.get_data()
        mess = data['q']  # ID сообщения для рассылки

        await bot.copy_message(chat_id=message.chat.id, from_chat_id=message.chat.id, message_id=mess.message_id,
                               reply_markup=murkap)

        await state.update_data(text_but=massiv_text)  # Обновление Сета
        await state.update_data(url_but=massiv_url)  # Обновление Сета

        murkap2 = types.InlineKeyboardMarkup()  # Клавиатура - меню
        bat0 = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otemena')
        bat1 = types.InlineKeyboardButton(text='РАЗОСЛАТЬ', callback_data='send_ras')
        murkap2.add(bat1)
        murkap2.add(bat0)

        await bot.send_message(chat_id=message.chat.id, text='Теперь твой пост выглядит так☝', reply_markup=murkap2)


    except:
        await bot.send_message(chat_id=message.chat.id, text='Ошибка. Отменено')
        await state.finish()


# КОНЕЦ НАСТРОЙКИ КНОПОК


@dp.callback_query_handler(text='send_ras', state="*")  # Рассылка
async def fname_step(call: types.callback_query, state: FSMContext):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    data = await state.get_data()
    mess = data['q']  # Сообщения для рассылки
    rasl = data['rasl']  # Сообщения для рассылки

    murkap = types.InlineKeyboardMarkup()  # Клавиатура с кнопками
    try:  # Пытаемся добавить кнопки. Если их нету оставляем клаву пустой
        text_massiv = data['text_but']
        url_massiv = data['url_but']
        for t in text_massiv:
            for u in url_massiv:
                bat = types.InlineKeyboardButton(text=t, url=u)
                murkap.add(bat)
                break

    except:
        pass

    db = sqlite3.connect('server.db')
    sql = db.cursor()
    await state.finish()
    users = sql.execute("SELECT id FROM user_time").fetchall()
    bad = 0
    good = 0
    delit = 0
    await bot.send_message(call.message.chat.id,
                           f"<b>Всего пользователей: <code>{len(users)}</code></b>\n\n<b>Расслыка начата!</b>",
                           parse_mode="html")

    if rasl == 'all':
        users = sql.execute("SELECT id FROM user_time").fetchall()
        for i in users:
            await asyncio.sleep(0.03)
            try:
                await mess.copy_to(i[0], reply_markup=murkap)
                good += 1
            except (BotBlocked, ChatNotFound):
                try:
                    delite_user(i[0])
                    delit += 1

                except:
                    pass
            except:
                bad += 1

    if rasl == 'activ':
        users = sql.execute("SELECT id FROM user_time WHERE status_ref = '0' ").fetchall()
        for i in users:
            await asyncio.sleep(0.03)
            try:
                await mess.copy_to(i[0], reply_markup=murkap)
                good += 1
            except (BotBlocked, ChatNotFound):
                try:
                    delite_user(i[0])
                    delit += 1

                except:
                    pass
            except:
                bad += 1

    if rasl == 'pasiv':
        users = sql.execute("SELECT id FROM user_time WHERE status = '1' ").fetchall()
        for i in users:
            await asyncio.sleep(0.03)
            try:
                await mess.copy_to(i[0], reply_markup=murkap)
                good += 1
            except (BotBlocked, ChatNotFound):
                try:
                    delite_user(i[0])
                    delit += 1

                except:
                    pass
            except:
                bad += 1
    await bot.send_message(
        call.message.chat.id,
        "<u>Рассылка окончена\n\n</u>"
        f"<b>Всего пользователей:</b> <code>{len(users)}</code>\n"
        f"<b>Отправлено:</b> <code>{good}</code>\n"
        f"<b>Удалено пользователей:</b> <code>{delit}</code>\n"
        f"<b>Произошло ошибок:</b> <code>{bad}</code>",
        parse_mode="html"
    )
    await bot.answer_callback_query(call.id)
#########################################################
