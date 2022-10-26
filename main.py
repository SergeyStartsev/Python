import telebot
from telebot import types

bot = telebot.TeleBot('TOKEN')
field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def winning_positions(field):
    winning_coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for all in winning_coordinates:
        if field[all[0]] == field[all[1]] == field[all[2]]:
            return field[all[0]]
    return False

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
    button1 = types.KeyboardButton(f'{field[0]}')
    button2 = types.KeyboardButton(f'{field[1]}')
    button3 = types.KeyboardButton(f'{field[2]}')
    button4 = types.KeyboardButton(f'{field[3]}')
    button5 = types.KeyboardButton(f'{field[4]}')
    button6 = types.KeyboardButton(f'{field[5]}')
    button7 = types.KeyboardButton(f'{field[6]}')
    button8 = types.KeyboardButton(f'{field[7]}')
    button9 = types.KeyboardButton(f'{field[8]}')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
    send_msg = f'Привет, {message.from_user.first_name}. приглашаем в игру крестики-нолики!'
    bot.send_message(message.chat.id, send_msg, reply_markup = markup)

@bot.message_handler(content_types = ['text'])
def mes(message):
    offer_draw = 0
    get_msg_bot = message.text.split()
    try:
        button = int(get_msg_bot[0]) 
    except:
        button = 0
    if button != 0 and button < 10:
        field[button - 1] = 'X'
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
        button1 = types.KeyboardButton(f'{field[0]}')
        button2 = types.KeyboardButton(f'{field[1]}')
        button3 = types.KeyboardButton(f'{field[2]}')
        button4 = types.KeyboardButton(f'{field[3]}')
        button5 = types.KeyboardButton(f'{field[4]}')
        button6 = types.KeyboardButton(f'{field[5]}')
        button7 = types.KeyboardButton(f'{field[6]}')
        button8 = types.KeyboardButton(f'{field[7]}')
        button9 = types.KeyboardButton(f'{field[8]}')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
        
        button = 0
        i = 0
        while button == 0: 
            try:
                button = int(field[i])
            except:
                if i < 9:
                    i += 1
                else:
                    break
        if button == 0:
            final_msg = f'Ничья!'
            offer_draw = 1
            bot.send_message(message.chat.id, final_msg)
            for i in range(9):
                field[i] = str(i + 1)
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
            button1 = types.KeyboardButton(f'{field[0]}')
            button2 = types.KeyboardButton(f'{field[1]}')
            button3 = types.KeyboardButton(f'{field[2]}')
            button4 = types.KeyboardButton(f'{field[3]}')
            button5 = types.KeyboardButton(f'{field[4]}')
            button6 = types.KeyboardButton(f'{field[5]}')
            button7 = types.KeyboardButton(f'{field[6]}')
            button8 = types.KeyboardButton(f'{field[7]}')
            button9 = types.KeyboardButton(f'{field[8]}')
            markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
            final_msg = f'Начинаем новую игру'
            bot.send_message(message.chat.id, final_msg, reply_markup = markup) 
                
        
        temp = winning_positions(field) # проверка на выигрыш человека
        if temp:
            final_msg = f'Вы выиграли!'
            bot.send_message(message.chat.id, final_msg)
            for i in range(9):
                field[i] = str(i + 1)
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
            button1 = types.KeyboardButton(f'{field[0]}')
            button2 = types.KeyboardButton(f'{field[1]}')
            button3 = types.KeyboardButton(f'{field[2]}')
            button4 = types.KeyboardButton(f'{field[3]}')
            button5 = types.KeyboardButton(f'{field[4]}')
            button6 = types.KeyboardButton(f'{field[5]}')
            button7 = types.KeyboardButton(f'{field[6]}')
            button8 = types.KeyboardButton(f'{field[7]}')
            button9 = types.KeyboardButton(f'{field[8]}')
            markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
            final_msg = f'Начинаем новую игру'
            bot.send_message(message.chat.id, final_msg, reply_markup = markup)

        else: 
            if offer_draw == 0: 
                best = [4, 0, 2, 6, 8, 1, 3, 5, 7]
                i = 0
                button = 0
                while button == 0:
                    try:
                        button = int(field[best[i]])
                    except:
                        i += 1
                field[button - 1] = 'O'
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
                button1 = types.KeyboardButton(f'{field[0]}')
                button2 = types.KeyboardButton(f'{field[1]}')
                button3 = types.KeyboardButton(f'{field[2]}')
                button4 = types.KeyboardButton(f'{field[3]}')
                button5 = types.KeyboardButton(f'{field[4]}')
                button6 = types.KeyboardButton(f'{field[5]}')
                button7 = types.KeyboardButton(f'{field[6]}')
                button8 = types.KeyboardButton(f'{field[7]}')
                button9 = types.KeyboardButton(f'{field[8]}')
                markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
                temp = winning_positions(field) 
                if temp:
                    final_msg = f'Выиграл бот!'
                    bot.send_message(message.chat.id, final_msg)
                    for i in range(9):
                        field[i] = str(i + 1)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
                    button1 = types.KeyboardButton(f'{field[0]}')
                    button2 = types.KeyboardButton(f'{field[1]}')
                    button3 = types.KeyboardButton(f'{field[2]}')
                    button4 = types.KeyboardButton(f'{field[3]}')
                    button5 = types.KeyboardButton(f'{field[4]}')
                    button6 = types.KeyboardButton(f'{field[5]}')
                    button7 = types.KeyboardButton(f'{field[6]}')
                    button8 = types.KeyboardButton(f'{field[7]}')
                    button9 = types.KeyboardButton(f'{field[8]}')
                    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
                    final_msg = f'Начинаем новую игру'
                    bot.send_message(message.chat.id, final_msg, reply_markup = markup)
                final_msg = f'Следующий ход' 
                bot.send_message(message.chat.id, final_msg, reply_markup = markup)

    else: 
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
        button1 = types.KeyboardButton(f'{field[0]}')
        button2 = types.KeyboardButton(f'{field[1]}')
        button3 = types.KeyboardButton(f'{field[2]}')
        button4 = types.KeyboardButton(f'{field[3]}')
        button5 = types.KeyboardButton(f'{field[4]}')
        button6 = types.KeyboardButton(f'{field[5]}')
        button7 = types.KeyboardButton(f'{field[6]}')
        button8 = types.KeyboardButton(f'{field[7]}')
        button9 = types.KeyboardButton(f'{field[8]}')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
        final_msg = f'Выбери, пожалуйста, на неиспользованную кнопку.'
        bot.send_message(message.chat.id, final_msg, reply_markup = markup)

bot.polling(non_stop = True)