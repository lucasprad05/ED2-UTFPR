import sys

class Game:
    def __init__(self, title=None, producer=None, genre=None, plataform=None, year=None, classification=None, price=None, midia=None, size=None):
        self.title = title
        self.producer = producer
        self.genre = genre
        self.plataform = plataform
        self.year = year
        self.classification = classification
        self.price = price
        self.midia = midia 
        self.size = size

    def setNome(self, name):
        self.name = name

    def getNome(self):
        return (self.name)

def ID(file):
    line = file.readline()
    title, producer, genre, plataform, year, classification, price, midia, size = line.split('|')
    game = Game(title, producer, genre, plataform, year, classification, price, midia, size)
    tempTitle = game.title.strip()
    ID = tempTitle + game.year

def deleteRecord(file, ID):
    tempFile = open('tempGames.txt', 'w')

def main():
    file = open('games.txt', 'r+')

main()