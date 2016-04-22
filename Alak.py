"""Alak!  Rated E for Everyone.  It's a simple and amusing game.  Can be played without any players, with one player as well as two.

How to run the game:
1) Instantiate the class
2) Insert number of credits for number of players (0, 1, 2)
3) Choose your side (x, o)
4) Make your moves!

To run the testing method:
1) Alak.testing()

"""

from __future__ import print_function, division
from random import choice
import numpy as np
from IPython import display
import pickle
from colorama import Fore, Back, Style
from pdb import set_trace
import re
np.set_printoptions(formatter={'float': '{:.5f}'.format})

class Alak:
    def __init__(self):
        self.step = []     #Used to store moves that happen throughout the game.
        self.board = np.array(['x', 'x', 'x', 'x', '_', '_', 'o', 'o', 'o', 'o'])     #Game board.
        
        self.test = ''     #Arbitrary initialization for the testing method.
        
        self.p1 = ''     #Arbitrary initialization to avoid future error if following if statement is not executed.
        self.p2 = ''     #Arbitrary initialization to avoid future error if following if statement is not executed.
        self.create_players()     #Will ask if you want 0, 1, or 2 players.
        
        self.turn = np.random.choice(['x', 'o'])     #Randomly chooses which side starts the game.
        print('{}-side starts the game!'.format(self.turn))
        
        #Self.defeat created for fun
        self.defeat = ['defeated', 'beaten to a pulp', 'crushed', 'overpowered', 'hulk-smashed', 'KO-ed', 'pummeled to pieces',\
                      'round-house-kicked in the face', 'chicken-dinnered by the winner', 'royal-flushed down the drain',\
                      "kamehameha'd", 'kill-Billed', 'blasted off at the speed of light', 'team-rocketed', 'shake-n-baked']
        
        self.fight()     #Runs the game
         
    def create_players(self):     #Creates players with user interface.
        num_players = int(raw_input('Insert Credits:\n(0) Computer\n(1) Single Player\n(2) Two Players\n'))
        if num_players == 2:     #If 2, then the game initializes two players.
            self.p1 = raw_input('Please choose a side, x or o: ')
            if self.p1 == 'x':
                self.p2 = 'o'
            else:
                self.p2 = 'x'
            print('Player 1: {}-side!'.format(self.p1))
            print('Player 2: {}-side!'.format(self.p2))
        if num_players == 1:     #If 1, then creates only player 1.
            self.p1 = raw_input('Please choose a side, x or o: ')
            print('Player 1: {}-side!'.format(self.p1))
        
    def change_turn(self):     #Changes which side's turn it is.
        x, o = 'x', 'o'
        if self.turn == x:
            self.turn = o
        else:
            self.turn = x
        
    def next_move(self):     #Determines the next move to make, either randomly for the computer or by choice of user.
        if self.turn != self.p1 and self.turn != self.p2:     #If not user, then computer moves self.turn side to random empty space.
            rand_empty = np.random.choice(np.where(self.board == '_')[0])     #Checks board for empty spaces, then chooses among all empty spaces.

            piece_pos = np.where(self.board == self.turn)[0]    #Indices of x/o pieces.
            rand_piece = np.random.choice(piece_pos)     #Among pieces, choose random piece to move to new, empty position, rand_empty.

            self.board[rand_empty], self.board[rand_piece] = self.board[rand_piece], self.board[rand_empty]     #Assign rand_piece to rand_empty.

            step = "{}: {} --> {}".format(self.turn, rand_piece, rand_empty)     #String that indicates which side's turn, moving rand_piece to rand_empty.
            self.step.append(step)     #Appends step to self.step to store turn information.
        else:     #User interface part.  Allows for user to choose particular piece and move to specified location.
            legal_spaces = np.where(self.board == '_')[0]     #Determines allowed spaces to move to.
            legal_pieces = np.where(self.board == self.turn)[0]     #Determines allow pieces to move.
            
            _break = True     #Initialized to break the following while loop if user inputs legal moves.
            while _break:
                pos_piece = int(raw_input("{}-side, select piece to move: ".format(self.turn)))     #User specifies piece to move.
                empty_space = int(raw_input("Move to: "))     #User specifies an empty space to move to.
                if pos_piece in legal_pieces and empty_space in legal_spaces:
                    self.board[empty_space], self.board[pos_piece] = self.board[pos_piece], self.board[empty_space]     #Swaps empty space with piece chosen.
                    step = "{}: {} --> {}".format(self.turn, pos_piece, empty_space)
                    self.step.append(step)     #Records step information in list, self.step.
                    _break = False
                else:     #Used to catch if user choices were illegal.
                    print("{} to {} is not a legal move, please choose among the legal moves.".format(pos_piece, empty_space))
                    print("Legal Pieces: {}".format(legal_pieces))
                    print("Legal Spaces: {}".format(legal_spaces))
                    
    
    def check_dead(self, test=False):     #Checks for kills made throughout the game.
        if test:     #Conditional for the testing method only.
            dead_pat = re.search('xo+x', ''.join(self.test))
            while dead_pat != None:
                dead_se = [(m.start(0), m.end(0)) for m in re.finditer(dead_pat.group(), ''.join(self.test))]
                for elem in dead_se:
                    np.put(self.test, range(elem[0]+1, elem[1]-1), '_')
                dead_pat = re.search('xo+x', ''.join(self.test))
            dead_pat = re.search('ox+o', ''.join(self.test))
            while dead_pat != None:
                dead_se = [(m.start(0), m.end(0)) for m in re.finditer(dead_pat.group(), ''.join(self.test))]
                for elem in dead_se:
                    np.put(self.test, range(elem[0]+1, elem[1]-1), '_')
                dead_pat = re.search('ox+o', ''.join(self.test))
        if self.turn == 'x':     #Searches for kills during 'x' turn.
            dead_pat = re.search('xo+x', ''.join(self.board))     #Searches board for the regular expression pattern.
            while dead_pat != None:     #While loop to catch multiple matches.
                dead_se = [(m.start(0), m.end(0)) for m in re.finditer(dead_pat.group(), ''.join(self.board))]     #Determines where the pattern starts and ends.
                for elem in dead_se:
                    np.put(self.board, range(elem[0]+1, elem[1]-1), '_')     #Replaces killed pieces on board.
                dead_pat = re.search('xo+x', ''.join(self.board))     #dead_pat reassigned until dead_pat returns None.
            dead_pat = re.search('ox+o', ''.join(self.board))     #Runs same code as above, but to check for suicide kills.
            while dead_pat != None:
                dead_se = [(m.start(0), m.end(0)) for m in re.finditer(dead_pat.group(), ''.join(self.board))]
                for elem in dead_se:
                    np.put(self.board, range(elem[0]+1, elem[1]-1), '_')
                dead_pat = re.search('ox+o', ''.join(self.board))
        else:     #Searches for kills during 'o' turn.
            dead_pat = re.search('ox+o', ''.join(self.board))
            while dead_pat != None:
                dead_se = [(m.start(0), m.end(0)) for m in re.finditer(dead_pat.group(), ''.join(self.board))]
                for elem in dead_se:
                    np.put(self.board, range(elem[0]+1, elem[1]-1), '_')
                dead_pat = re.search('ox+o', ''.join(self.board))
            dead_pat = re.search('xo+x', ''.join(self.board))
            while dead_pat != None:
                dead_se = [(m.start(0), m.end(0)) for m in re.finditer(dead_pat.group(), ''.join(self.board))]
                for elem in dead_se:
                    np.put(self.board, range(elem[0]+1, elem[1]-1), '_')
                dead_pat = re.search('xo+x', ''.join(self.board))

    def fight(self):     #Actual start of game.
        print(*self.board)     #Print initial board
        print(*range(10))     #Print indices for easy location choices.
        print()
        Round = 1
        step_n = 0

        while len(np.unique(self.board)) > 2:     #Keeps game running until np.unique drops to 2 and below.
            print("Round: {}\n".format(Round))     #Prints current round.
            Round += 1
        ############################################
            for run in range(2):     #Used to run the following code twice in order to accommodate both sides.
                self.next_move()     #Determines which piece to move and moves it to an empty space
                
                print(self.step[step_n])     #Prints move made.
                step_n += 1
                
                self.check_dead()     #Checks to see if a kill is made
                
                print(*self.board)
                print(*range(10))

                self.change_turn()     #Changes turn so opponent can make move.
                    
                if (self.board == 'x').sum() <= 1:     #Checks for game-over.
                    print(Back.YELLOW + "Game over! x-side has {} piece(s) left! x-side has been {}!".format((self.board == 'x').sum(), np.random.choice(self.defeat)))
                    return
                if (self.board == 'o').sum() <= 1:     #Checks for game-over.
                    print(Back.YELLOW + "Game over! o-side has {} piece(s) left! o-side has been {}!".format((self.board == 'o').sum(), np.random.choice(self.defeat)))
                    return
            print()
    
    def testing(self):     #Tests "special" cases of Alak game (i.e. suicide, double-kill, etc.).
        passed = 0
        failed = 0
        special_cases = np.array([list('xx_xox_ooo'), list('_xox_xx_oo'), list('_xoox_ox__'),\
                         list('xoxoxx_oo_'), list('xooox__oxx'), list('xoooox__xx')])
        expected_results = np.array([list('xx_x_x_ooo'), list('_x_x_xx_oo'), list('_x__x_ox__'),\
                         list('x_x_xx_oo_'), list('x___x__oxx'), list('x____x__xx')])
        for i in range(len(special_cases)):
            self.test = np.array(special_cases[i])
            try:
                self.check_dead(test=True)
                assert np.array_equal(self.test, expected_results[i])
            except:
                failed += 1
            else:
                passed += 1
        if failed != 0:
            print("{} out of 6 tests passed!".format(passed))
            print(Fore.RED + "{} out of 6 tests failed!".format(failed))
        else:
            print("{} out of 6 tests passed!".format(passed))
        print(Style.RESET_ALL)
        
Alak = Alak()