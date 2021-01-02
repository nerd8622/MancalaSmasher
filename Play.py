from Game import Game

game = Game()

while not game.gameWon:
    print(game)
    game.move(int(input("Move: ")))
