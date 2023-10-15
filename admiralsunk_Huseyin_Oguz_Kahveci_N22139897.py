import random
import string
import sys
# 1 yıldızdan 5 yıldıza kadar gemileri üretmek için fonksiyonlarımızı yazdık
def create_ships():
    ships = ["*" * i for i in range(1, 6)]
    return ships
# board'u oluşturduk
def create_board():
    board = [[" "] * 10 for _ in range(10)]
    return board
# gemileri Horizontal ve Veritcal olarak 10 10 matrisin içine yerleştirdik
def place_ships(board, ships):
    for ship in ships:
        while True:
            orientation = random.choice(["H", "V"])
            if orientation == "H":
                row = random.randint(0, 9)
                col = random.randint(0, 10 - len(ship))
                if " " * len(ship) in "".join(board[row][col:col+len(ship)]):
                    for i in range(len(ship)):
                        board[row][col + i] = ship[i]
                    break
            else:
                row = random.randint(0, 10 - len(ship))
                col = random.randint(0, 9)
                if " " * len(ship) in "".join(board[i][col] for i in range(row, row + len(ship))):
                    for i in range(len(ship)):
                        board[row + i][col] = ship[i]
                    break
    return board
# tahta durumunu yazdırma fonksiyonunu hazırladık
def print_user_board(board):
    print("   " + " ".join(string.ascii_uppercase[:10]))
    for i, row in enumerate(board, start=1):
        print(f"{i:2} {' '.join(row)}")
# girdide hata olmaması adına inputta verilen işlemleri row ve coloumn olarak parçalayabilmek için fonskiyonumuzu yazdık
def convert_input(user_input):
    split_input = user_input.strip().upper().split()
    col = string.ascii_uppercase.index(split_input[0])
    row = int(split_input[1]) - 1
    return row, col
# geçerli bir girdi girilip girilmediğini kontrol etme fonksiyonu
def validate_input(user_input):
    try:
        split_input = user_input.strip().upper().split()
        col = string.ascii_uppercase.index(split_input[0])
        row = int(split_input[1]) - 1
        if row < 0 or row > 9 or col < 0 or col > 9:
            return False
        else:
            return True
    except (IndexError, ValueError):
        return False
#oyunu başlatıyoruz
def play_game():
    shots = 0
    ships = create_ships()
    board = create_board()
    board = place_ships(board, ships)

    user_board = create_board()
    while True:
        print_user_board(user_board)
        while True:
            user_input = input("Bir koordinat girin (örn: B 5), 'r' tuşuna basın durumu kontrol etmek için, 'q' tuşuna basın oyunu bitirmek için: ")
            if user_input.lower() == 'r':
                print(f"Atış denemeleriniz: {shots}")
                continue
            elif user_input.lower() == 'q':
                print("Oyun bitti. Hoşça kal!")
                sys.exit()
            elif validate_input(user_input):
                break
            else:
                print("Geçersiz giriş, lütfen tekrar deneyin.")
        row, col = convert_input(user_input)
        shots += 1
        if board[row][col] == " ":
            print("Iska!")
            user_board[row][col] = "X"
        else:
            print("Amiral yara aldı!")
            user_board[row][col] = "*"
            board[row][col] = " "
        if all("*" not in row for row in board):
            print("Denizaltı battı!!")
            break

play_game()
