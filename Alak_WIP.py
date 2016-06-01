## WIP
## Implement NN

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
from colorama import Fore, Back, Style
from pdb import set_trace
import re
import os.path
import datetime
import json
import itertools
from itertools import combinations, product

import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.cross_validation import train_test_split

import time
from functools import wraps

import winsound

np.set_printoptions(formatter={'float': '{:.5f}'.format})


class Alak:
    def __init__(self, pr=True, training=False, num_players=None, smart=False, beep=False):
        self.training = training
        self.num_players = num_players
        self.smart = smart
        
        self.beep = beep
        
        self.NN_train = True
        
        self.pr = pr
        
        self.win_rate_x = 0
        self.win_rate_o = 0
        
        self.step = []
        self.x_step = []     #Used to store moves that happen throughout the game.
        self.o_step = []
        
        self.board = np.array(['x', 'x', 'x', 'x', '_', '_', 'o', 'o', 'o', 'o'])     #Game board.
#         self.board = np.array(['x', '_', 'x', 'x', 'x', '_', 'o', 'o', 'o', 'o'])
        self.training_board = np.array([1, 1, 1, 1, 0, 0, -1, -1, -1, -1])     #Training game board
        
        self.x_json = []
        self.o_json = []     #Arbitrary initialization to save read json file
        
        x_json_file = 'Alak_json_x.json'     #File name of json file.
        o_json_file = 'Alak_json_o.json'
        if os.path.exists(x_json_file):
            with open(x_json_file) as f:
                self.x_json = json.load(f)
        if os.path.exists(o_json_file):
            with open(o_json_file) as f:
                self.o_json = json.load(f)
        
        self.test = ''     #Arbitrary initialization for the testing method.
        
        self.p1 = ''     #Arbitrary initialization to avoid future error if following if statement is not executed.
        self.p2 = ''     #Arbitrary initialization to avoid future error if following if statement is not executed.
        self.create_players()     #Will ask if you want 0, 1, or 2 players.
        
#         self.turn = np.random.choice(['x', 'o'])     #Randomly chooses which side starts the game.
        self.turn = 'o'
        if self.pr:
            print('{}-side starts the game!'.format(self.turn))
        
        #Self.defeat created for fun
        self.defeat = ['defeated', 'beaten to a pulp', 'crushed', 'overpowered', 'hulk-smashed', 'KO-ed', 'pummeled to pieces',\
                      'round-house-kicked in the face', 'chicken-dinnered by the winner', 'royal-flushed down the drain',\
                      "kamehameha'd", 'kill-Billed', 'blasted off at the speed of light', 'team-rocketed', 'shake-n-baked']
        
        self.read_x_json = []
        self.read_o_json = []
        
        self.winner = 1
        
        self.fight()     #Runs the game
        
    def json(self, read_x=None, read_o=None):
        x_json_file = 'Alak_json_x.json'     #File name of json file.
        o_json_file = 'Alak_json_o.json'
        
        if os.path.exists(x_json_file):
            with open(x_json_file) as f:
                self.x_json = json.load(f)
        self.x_json.extend(self.x_step)
        with open(x_json_file, 'w') as f:
            json.dump(self.x_json, f)
            
        if os.path.exists(o_json_file):
            with open(o_json_file) as f:
                self.o_json = json.load(f)
        self.o_json.extend(self.o_step)
        with open(o_json_file, 'w') as f:
            json.dump(self.o_json, f)
         
    def create_players(self):     #Creates players with user interface.
        if self.training:
            num_players = self.num_players
        else:
            if self.beep:
                Freq = 2500 # Set Frequency To 2500 Hertz
                Dur = 1000 # Set Duration To 1000 ms == 1 second
                winsound.Beep(Freq,Dur)
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
    
    def convert_board(self):
        self.training_board = np.zeros(self.board.size)
        self.training_board[self.board=='x'] = 1
        self.training_board[self.board=='o'] = -1
        self.training_board[self.board=='_'] = 0
        
    def next_move(self):     #Determines the next move to make, either randomly for the computer or by choice of user.
        if self.turn != self.p1 and self.turn != self.p2:     #If not user, then computer moves self.turn side to random empty space.
            if self.smart:
                if self.NN_train:
                    self.NN_training()
                    self.NN_train = False
                empty_spaces = np.where(self.board == '_')[0]     #Indices of empty spaces
                piece_pos = np.where(self.board == self.turn)[0]    #Indices of x/o pieces.
                self.possible_moves = list(product(piece_pos, empty_spaces))
                if self.turn == 'x':
                    self.x_decision = np.where(self.clf_x.decision_function(self.possible_moves) == max(self.clf_x.decision_function(self.possible_moves)))[0][0]
                    self.board[self.possible_moves[self.x_decision][0]], self.board[self.possible_moves[self.x_decision][1]]\
                            = self.board[self.possible_moves[self.x_decision][1]], self.board[self.possible_moves[self.x_decision][0]]
            
                    self.x_step.append([[np.asscalar(self.possible_moves[self.x_decision][0]), np.asscalar(self.possible_moves[self.x_decision][1])], 0])
                    step = "{}: {} --> {}".format(self.turn, self.possible_moves[self.x_decision][0], self.possible_moves[self.x_decision][1])     #String that indicates which side's turn, moving rand_piece to rand_empty.
                    self.step.append(step)
                if self.turn == 'o':
                    self.o_decision = np.where(self.clf_o.decision_function(self.possible_moves) == max(self.clf_o.decision_function(self.possible_moves)))[0][0]
                    self.board[self.possible_moves[self.o_decision][0]], self.board[self.possible_moves[self.o_decision][1]]\
                            = self.board[self.possible_moves[self.o_decision][1]], self.board[self.possible_moves[self.o_decision][0]]
            
                    self.o_step.append([[np.asscalar(self.possible_moves[self.o_decision][0]), np.asscalar(self.possible_moves[self.o_decision][1])], 0])
                    step = "{}: {} --> {}".format(self.turn, self.possible_moves[self.o_decision][0], self.possible_moves[self.o_decision][1])     #String that indicates which side's turn, moving rand_piece to rand_empty.
                    self.step.append(step)
            else:
                rand_empty = np.random.choice(np.where(self.board == '_')[0])     #Checks board for empty spaces, then chooses among all empty spaces.
                piece_pos = np.where(self.board == self.turn)[0]    #Indices of x/o pieces.
                rand_piece = np.random.choice(piece_pos)     #Among pieces, choose random piece to move to new, empty position, rand_empty.

                self.board[rand_empty], self.board[rand_piece] = self.board[rand_piece], self.board[rand_empty]     #Assign rand_piece to rand_empty.

                step = "{}: {} --> {}".format(self.turn, rand_piece, rand_empty)     #String that indicates which side's turn, moving rand_piece to rand_empty.
                self.step.append(step)
                if self.turn == 'x':
                    self.x_step.append([[np.asscalar(rand_piece), np.asscalar(rand_empty)], 0])
                else:
                    self.o_step.append([[np.asscalar(rand_piece), np.asscalar(rand_empty)], 0])

        else:     #User interface part.  Allows for user to choose particular piece and move to specified location.
            legal_spaces = np.where(self.board == '_')[0]     #Determines allowed spaces to move to.
            legal_pieces = np.where(self.board == self.turn)[0]     #Determines allow pieces to move.
            
            _break = True     #Initialized to break the following while loop if user inputs legal moves.
            while _break:
                pos_piece = int(raw_input("{}-side, select piece to move: ".format(self.turn)))     #User specifies piece to move.
                empty_space = int(raw_input("Move to: "))     #User specifies an empty space to move to.
                if pos_piece in legal_pieces and empty_space in legal_spaces:
                    self.board[empty_space], self.board[pos_piece] = \
                        self.board[pos_piece], self.board[empty_space]     #Swaps empty space with piece chosen.
                    
                    step = "{}: {} --> {}".format(self.turn, pos_piece, empty_space)
                    self.step.append(step)
                    if self.turn == 'x':
                        self.x_step.append([[np.asscalar(pos_piece), np.asscalar(empty_space)], 0])     #Appends step to self.x_step to store turn information.
                    else:
                        self.o_step.append([[np.asscalar(pos_piece), np.asscalar(empty_space)], 0])

                    _break = False
                else:     #Used to catch if user choices were illegal.
                    print("{} to {} is not a legal move, please choose among the legal moves."\
                                                                      .format(pos_piece, empty_space))
                    print("Legal Pieces: {}".format(legal_pieces))
                    print("Legal Spaces: {}".format(legal_spaces))
                    
    
    def check_dead(self, test=False, side='x'):     #Checks for kills made throughout the game.
        if test:     #Conditional for the testing method only.
            if side == 'x':
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
            else:
                dead_pat = re.search('ox+o', ''.join(self.test))
                while dead_pat != None:
                    dead_se = [(m.start(0), m.end(0)) for m in re.finditer(dead_pat.group(), ''.join(self.test))]
                    for elem in dead_se:
                        np.put(self.test, range(elem[0]+1, elem[1]-1), '_')
                    dead_pat = re.search('ox+o', ''.join(self.test))
                dead_pat = re.search('xo+x', ''.join(self.test))
                while dead_pat != None:
                    dead_se = [(m.start(0), m.end(0)) for m in re.finditer(dead_pat.group(), ''.join(self.test))]
                    for elem in dead_se:
                        np.put(self.test, range(elem[0]+1, elem[1]-1), '_')
                    dead_pat = re.search('xo+x', ''.join(self.test))
                
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
                
    def win_rate(self):
        wins_x = 0
        wins_o = 0

        for elem in self.x_json:
            if elem[1] == 1:
                wins_x += 1
        for elem in self.o_json:
            if elem[1] == 1:
                wins_o += 1

        self.win_rate_x = wins_x/(wins_x + wins_o)
        self.win_rate_o = wins_o/(wins_x + wins_o)
        print("Win rate for x: {}\nWin rate for o: {}".format(self.win_rate_x, self.win_rate_o))

    def fight(self):     #Actual start of game.
        if self.pr:
            print(*self.board)     #Print initial board
            print(*range(10))     #Print indices for easy location choices.
            print()
        self.Round = 1
        step_n = 0

        while len(np.unique(self.board)) > 2:     #Keeps game running until np.unique drops to 2 and below.
            if self.pr:
                print("Round: {}\n".format(self.Round))     #Prints current round.
            self.Round += 1
        ############################################
            for run in range(2):     #Used to run the following code twice in order to accommodate both sides.
                self.next_move()     #Determines which piece to move and moves it to an empty space
                if self.pr:
                    print(self.step[step_n])     #Prints move made.
                step_n += 1
                self.check_dead()     #Checks to see if a kill is made
                if self.pr:
                    print(*self.board)
                    print(*range(10))
                self.change_turn()     #Changes turn so opponent can make move.
                if (self.board == 'x').sum() <= 1:     #Checks for game-over.
                    if self.pr:
                        print("Game over! x-side has {} piece(s) left! x-side has been {}!\n"\
                                .format((self.board == 'x').sum(), np.random.choice(self.defeat)))
                    self.o_step[-1][-1] = self.winner
                    self.json()
                    return
                if (self.board == 'o').sum() <= 1:     #Checks for game-over.
                    if self.pr:
                        print("Game over! o-side has {} piece(s) left! o-side has been {}!\n"\
                                  .format((self.board == 'o').sum(), np.random.choice(self.defeat)))
                    self.x_step[-1][-1] = self.winner
                    self.json()
                    return
            if self.pr:
                print()
    
    def testing_x(self):     #Tests "special" cases of Alak game (i.e. suicide, double-kill, etc.).
        passed = 0
        failed = 0
        special_cases = np.array([list('xoxoxx____'), list('xooxooxx__'), list('__xoo__oxo'), list('__xoo__xox')])
#         special_cases = np.array(list('oxoxoo____'), list('oxxoxxoo__'), list('_xoxx__ox_'), list('x__oxo_x__')])
        expected_results = np.array([list('x_x_xx____'), list('x__x__xx__'), list('__xoo__o_o'), list('__xoo__x_x')])
#         expected_results = np.array([list('o_o_oo____'), list('o__o__oo__'), list('_x_xx__ox_'), list('x__o_o_x__')])
        for i in range(len(special_cases)):
            self.test = np.array(special_cases[i])
            try:
                self.check_dead(test=True)
                assert np.array_equal(self.test, expected_results[i])
                print(self.test)
                print(expected_results[i])
            except:
                failed += 1
            else:
                passed += 1
        if failed != 0:
            print("{} out of {} tests passed!".format(passed, len(special_cases)))
            print(Fore.RED + "{} out of {} tests failed!".format(failed, len(special_cases)))
        else:
            print("{} out of {} tests passed!".format(passed, len(special_cases)))
        print(Style.RESET_ALL)
        
    def testing_o(self):     #Tests "special" cases of Alak game (i.e. suicide, double-kill, etc.).
        passed = 0
        failed = 0
#         special_cases = np.array([list('xoxoxx____'), list('xooxooxx__'), list('__xoo__oxo'), list('__xoo__xox')])
        special_cases = np.array([list('oxoxoo____'), list('oxxoxxoo__'), list('_xoxx__ox_'), list('x__oxo_x__')])
#         expected_results = np.array([list('x_x_xx____'), list('x__x__xx__'), list('__xoo__o_o'), list('__xoo__x_x')])
        expected_results = np.array([list('o_o_oo____'), list('o__o__oo__'), list('_x_xx__ox_'), list('x__o_o_x__')])
        for i in range(len(special_cases)):
            self.test = np.array(special_cases[i])
            try:
                self.check_dead(test=True, side='o')
                assert np.array_equal(self.test, expected_results[i])
                print(self.test)
                print(expected_results[i])
            except:
                failed += 1
            else:
                passed += 1
        if failed != 0:
            print("{} out of {} tests passed!".format(passed, len(special_cases)))
            print(Fore.RED + "{} out of {} tests failed!".format(failed, len(special_cases)))
        else:
            print("{} out of {} tests passed!".format(passed, len(special_cases)))
        print(Style.RESET_ALL)
        
    def NN_training(self, test_size=0.0):
        X_x = np.array([self.x_json[i][0] for i, j in enumerate(self.x_json)])
        y_x = np.array([self.x_json[i][1] for i, j in enumerate(self.x_json)])
        Xx_train, Xx_test, yx_train, yx_test = train_test_split(X_x, y_x, test_size=test_size, random_state=0)

        X_o = np.array([self.o_json[i][0] for i, j in enumerate(self.x_json)])
        y_o = np.array([self.o_json[i][1] for i, j in enumerate(self.x_json)])
        Xo_train, Xo_test, yo_train, yo_test = train_test_split(X_o, y_o, test_size=test_size, random_state=0)

        self.clf_x = MLPClassifier(algorithm='l-bfgs', alpha=1e-10, hidden_layer_sizes=(10, 4), activation = 'tanh',\
            random_state=5, max_iter=1000000, learning_rate_init = 0.1)
        self.clf_x.fit(Xx_train, yx_train)

        self.clf_o = MLPClassifier(algorithm='l-bfgs', alpha=1e-10, hidden_layer_sizes=(10, 4), activation = 'tanh',\
            random_state=5, max_iter=1000000, learning_rate_init = 0.1)
        self.clf_o.fit(Xo_train, yo_train)