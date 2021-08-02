import sys


class GameEntry:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

class Scoreboard:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._board = [None] * capacity
        self._n = 0

    def add(self, entry):
        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1

            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]
                j -= 1
            self._board[j] = entry

    def papanScore(self):
        posisi = 1
        for i in self._board:
            if not i == None:
                print("posisi ", posisi, ": ", i.get_name(), i.get_score())
            posisi += 1

scoreBoard = Scoreboard(10)

i = 1
while i>0:
    print("""\n1. Masukan Nama pemain\n2. Lihat Rangking & Score""")
    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        name = str(input("Nama: "))
        point = str(input("Point: "))
        entry = GameEntry(name, point)
        scoreBoard.add(entry)

    elif pilihan == 2:
        scoreBoard.papanScore()
