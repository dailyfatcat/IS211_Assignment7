import random
import argparse

class Player:
    '''Creates the player for the game, their score, and reset player'''
    def __init__(self, name):
        self.name = name
        self.Score = 0

    def setScore(self, value):
        self.Score += value

    def getScore(self):
        score = self.Score
        return score

    def resetPlayer(self):
        self.Score = 0

class Dice:
    '''Random Dice for the game with 6 sides'''
    def __init__(self, seed):
        random.seed(seed)

    def roll(self):
        return random.randrange(1, 6)


class Game:
    '''Pig Game, rules of the game, game rests, and turns'''
    def __init__(self, numPlayers):
        self.numPlayers = numPlayers
        self.people = []
        self.die = Dice(0)
        self.winner = ""
        self.winningscore = 20

    def resetGame(self):
        self.winner = ""
        for player in self.people:
            player.resetPlayer()

    def assignPlayers(self):
        #create list of players and assign names
        for i in range(self.numPlayers):
            print(f"Enter player {i+1} name: ")
            self.people.append(Player(input()))
        return

    def playerTurn(self, player, die):
        turntotal = 0
        currentscore = player.getScore()
        print(f"Player: {player.name} turn")
        print(f"Start turn: Total game score is : {player.getScore()}")
        print("Enter r to roll, or h to hold")
        choice = input()

        #check for hold
        while choice != "h":
            roll = die.roll()
            #If a player doesn't roll a one, print requirements
            #And continue turn
            if roll != 1:
                turntotal += roll
                print(f"Your current turn score is: {turntotal}")
                print(f"You rolled a: {roll}")
                if currentscore + turntotal >= self.winningscore:
                    self.winner = player.name
                    player.setScore(turntotal + currentscore)
                    return
                print("Enter r to roll, or h to hold")
                choice = input()
            #If the player has rolled a one turn is over
            else:
                print("You rolled a 1, turn over")
                return
        player.setScore(turntotal + currentscore)
        return

    def StartPIG(self):
        #Create the players
        if not self.people:
            self.assignPlayers()
        else:
            self.resetGame()

        #Players turns until game is won
        while 1:
            for player in self.people:
                self.playerTurn(player, self.die)
                if self.winner:
                    return

def main(players):
    '''Start the game'''
    Pig = Game(players)
    playagain = 'y'

    #Extra Credit: Allow for more than one game
    #Create loop to ask players if they want to play again
    while playagain == 'y':
        Pig.StartPIG()
        print("****----------------------****")
        print(f"Winner and Champion is: {Pig.winner}")
        print("****----------------------****")
        print("Do you want to play again? Enter 'y' to play again. Enter something else to leave the game.")
        playagain = input()


if __name__ == '__main__':
    '''Main Entry Point'''
    #Extra Credit: Allow for a configurable number of players viaa the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("--numPlayers", help="Number of Players for Game", type=int, required=True)
    args = parser.parse_args()
    main(args.numPlayers)


