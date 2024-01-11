BOARD_SIZE = 10

class Board:
    def __init__(self):
        self.array = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]

class Klasa1:
    def __init__(self, board_object):
        self.board = board_object

    def modyfikuj_board(self, nowa_wartosc):
        self.board.array[0][0] = nowa_wartosc

class Klasa2:
    def __init__(self, board_object):
        self.board = board_object

# Tworzenie obiektu klasy Board
board = Board()

# Tworzenie instancji obu klas z tym samym obiektem klasy Board
obiekt1 = Klasa1(board)
obiekt2 = Klasa2(board)

print(obiekt1.board.array[0][0])  # Output: 42
print(obiekt2.board.array[0][0])  # Output: 42

# Wywołanie metody modyfikuj_board na instancji obiekt1
obiekt1.modyfikuj_board(42)

# Wyświetlenie wartości w obiektach obiekt1 i obiekt2
print(obiekt1.board.array[0][0])  # Output: 42
print(obiekt2.board.array[0][0])  # Output: 42
