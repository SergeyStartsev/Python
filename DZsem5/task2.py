# Создайте программу для игры в "Крестики-нолики".

inputed = list(range(1, 10))

def draw_board(field):
    print()
    for i in range(3):
        print(field[0+i*3],  field[1+i*3],
              field[2+i*3], sep=" | ", end='\n')

def check_win(check):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8))
    for each in win_coord:
        if check[each[0]] == check[each[1]] == check[each[2]]:
            return check[each[0]]
    return False

def player_input(token):
    valid = False
    while not valid:
        answer = input("\nХод " + token+" ")
        try:
            answer = int(answer)
        except:
            print("Неверный числовой диапозон")
            continue
        if answer >= 1 and answer <= 9:
            if (str(inputed[answer-1]) not in "XO"):
                inputed[answer-1] = token
                valid = True
            else:
                print("Это поле занято")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

def main(value):
    counter = 0
    temp = False
    while not temp:
        draw_board(value)
        if counter % 2 == 0:
            player_input("X")
        else:
            player_input("O")
        counter += 1
        if counter > 4:
            temp = check_win(value)
            if temp:
                print(temp, "Победил")
                temp = True
                break
        if counter == 9:
            print("Ничья")
            break
    draw_board(value)

main(inputed)

input("\nНажмите Enter для выхода...")