#!/usr/bin/python2

import nose
import unittest
from c4board import c4board


class test_c4board_misc(unittest.TestCase):
    def test_create_board(self):
        ''' Verify that a board can be created '''
        test_board = c4board()

    def test_str(self):
        ''' Verify that the __str__ method executes '''
        test_board = c4board()
        str(test_board)

    def test_repr(self):
        ''' Verify that the __repr__ method executes '''
        test_board = c4board()
        repr(test_board)

    def test_no_win_empty(self):
        ''' Verify that an empty board has no wins '''
        test_board = c4board()
        self.assertFalse(test_board.has_win())


class test_c4board_errors(unittest.TestCase):

    def test_invalid_color_play(self):
        ''' Verify that an invalid color produces an exception '''
        test_board = c4board()
        self.assertFalse(test_board.has_win())
        with self.assertRaises(ValueError):
            test_board.play_token(1, 'blue')

    def test_column_too_small(self):
        ''' Verify that an invalid (small) column produces an exception '''
        test_board = c4board()
        self.assertFalse(test_board.has_win())
        with self.assertRaises(IndexError):
            test_board.play_token(0, 'black')

    def test_column_too_big(self):
        ''' Verify that an invalid (big) column produces an exception '''
        test_board = c4board()
        self.assertFalse(test_board.has_win())
        with self.assertRaises(IndexError):
            test_board.play_token(19, 'red')

    def test_nonalternating_colors(self):
        ''' Verify that an out-of-order play produces an exception '''
        test_board = c4board()
        self.assertFalse(test_board.has_win())
        self.assertFalse(test_board.play_token(4, 'red'))
        self.assertFalse(test_board.play_token(5, 'black'))
        with self.assertRaises(ValueError):
            test_board.play_token(5, 'black')

    def test_full_column(self):
        ''' Verify that playing in a full column produces an exception '''
        test_board = c4board()
        self.assertFalse(test_board.has_win())
        self.assertFalse(test_board.play_token(4, 'red'))
        self.assertFalse(test_board.play_token(4, 'black'))
        self.assertFalse(test_board.play_token(4, 'red'))
        self.assertFalse(test_board.play_token(4, 'black'))
        self.assertFalse(test_board.play_token(4, 'red'))
        self.assertFalse(test_board.play_token(4, 'black'))
        with self.assertRaises(IndexError):
            test_board.play_token(4, 'black')


class test_c4board_wins(unittest.TestCase):
    def test_vertical_win_vertical_red(self):
        ''' Test a basic vertical win '''
        test_board = c4board()
        self.assertFalse(test_board.has_win())
        self.assertFalse(test_board.play_token(4, 'red'))
        self.assertFalse(test_board.play_token(3, 'black'))
        self.assertFalse(test_board.play_token(4, 'red'))
        self.assertFalse(test_board.play_token(3, 'black'))
        self.assertFalse(test_board.play_token(4, 'red'))
        self.assertFalse(test_board.play_token(3, 'black'))
        self.assertTrue(test_board.play_token(4, 'red'))

    def test_vertical_win_vertical_black(self):
        ''' Test a basic vertical win with black winning '''
        test_board = c4board()
        self.assertFalse(test_board.has_win())
        self.assertFalse(test_board.play_token(3, 'black'))
        self.assertFalse(test_board.play_token(4, 'red'))
        self.assertFalse(test_board.play_token(3, 'black'))
        self.assertFalse(test_board.play_token(4, 'red'))
        self.assertFalse(test_board.play_token(3, 'black'))
        self.assertFalse(test_board.play_token(4, 'red'))
        self.assertTrue(test_board.play_token(3, 'black'))

    def test_horizontal_win_right(self):
        ''' Test a basic horizontal win '''
        test_board = c4board()
        self.assertFalse(test_board.has_win())
        self.assertFalse(test_board.play_token(4, 'red'))
        self.assertFalse(test_board.play_token(4, 'black'))
        self.assertFalse(test_board.play_token(5, 'red'))
        self.assertFalse(test_board.play_token(5, 'black'))
        self.assertFalse(test_board.play_token(6, 'red'))
        self.assertFalse(test_board.play_token(6, 'black'))
        self.assertTrue(test_board.play_token(7, 'red'))

    def test_diag_win_upright(self):
        ''' Test a basic up-to-the-right diagonal win '''
        test_board = c4board()
        self.assertFalse(test_board.has_win())
        self.assertFalse(test_board.play_token(1, 'red'))
        self.assertFalse(test_board.play_token(2, 'black'))
        self.assertFalse(test_board.play_token(2, 'red'))
        self.assertFalse(test_board.play_token(3, 'black'))
        self.assertFalse(test_board.play_token(3, 'red'))
        self.assertFalse(test_board.play_token(7, 'black'))
        self.assertFalse(test_board.play_token(3, 'red'))
        self.assertFalse(test_board.play_token(4, 'black'))
        self.assertFalse(test_board.play_token(4, 'red'))
        self.assertFalse(test_board.play_token(4, 'black'))
        self.assertTrue(test_board.play_token(4, 'red'))

    def test_diag_win_downright(self):
        ''' Test a basic down-to-the-right diagonal win '''
        test_board = c4board()
        self.assertFalse(test_board.has_win())
        self.assertFalse(test_board.play_token(1, 'red'))
        self.assertFalse(test_board.play_token(1, 'black'))
        self.assertFalse(test_board.play_token(1, 'red'))
        self.assertFalse(test_board.play_token(1, 'black'))
        self.assertFalse(test_board.play_token(2, 'red'))
        self.assertFalse(test_board.play_token(2, 'black'))
        self.assertFalse(test_board.play_token(7, 'red'))
        self.assertFalse(test_board.play_token(2, 'black'))
        self.assertFalse(test_board.play_token(3, 'red'))
        self.assertFalse(test_board.play_token(3, 'black'))
        self.assertFalse(test_board.play_token(7, 'red'))
        self.assertTrue(test_board.play_token(4, 'black'))


class test_no_win(unittest.TestCase):
    def test_no_win_full(self):
        ''' Test a full board with no wins '''
        test_board = c4board()
        self.assertFalse(test_board.has_win())
        self.assertFalse(test_board.play_token(1, 'red'))
        self.assertFalse(test_board.play_token(2, 'black'))
        self.assertFalse(test_board.play_token(3, 'red'))
        self.assertFalse(test_board.play_token(4, 'black'))
        self.assertFalse(test_board.play_token(5, 'red'))
        self.assertFalse(test_board.play_token(6, 'black'))
        self.assertFalse(test_board.play_token(7, 'red'))

        self.assertFalse(test_board.play_token(1, 'black'))
        self.assertFalse(test_board.play_token(2, 'red'))
        self.assertFalse(test_board.play_token(3, 'black'))
        self.assertFalse(test_board.play_token(4, 'red'))
        self.assertFalse(test_board.play_token(5, 'black'))
        self.assertFalse(test_board.play_token(6, 'red'))
        self.assertFalse(test_board.play_token(7, 'black'))

        self.assertFalse(test_board.play_token(1, 'red'))
        self.assertFalse(test_board.play_token(7, 'black'))
        self.assertFalse(test_board.play_token(2, 'red'))
        self.assertFalse(test_board.play_token(3, 'black'))
        self.assertFalse(test_board.play_token(6, 'red'))
        self.assertFalse(test_board.play_token(4, 'black'))
        self.assertFalse(test_board.play_token(5, 'red'))

        self.assertFalse(test_board.play_token(2, 'black'))
        self.assertFalse(test_board.play_token(1, 'red'))
        self.assertFalse(test_board.play_token(4, 'black'))
        self.assertFalse(test_board.play_token(3, 'red'))
        self.assertFalse(test_board.play_token(6, 'black'))
        self.assertFalse(test_board.play_token(5, 'red'))
        self.assertFalse(test_board.play_token(7, 'black'))

        self.assertFalse(test_board.play_token(2, 'red'))
        self.assertFalse(test_board.play_token(1, 'black'))
        self.assertFalse(test_board.play_token(3, 'red'))
        self.assertFalse(test_board.play_token(4, 'black'))
        self.assertFalse(test_board.play_token(6, 'red'))
        self.assertFalse(test_board.play_token(5, 'black'))
        self.assertFalse(test_board.play_token(7, 'red'))

        self.assertFalse(test_board.play_token(1, 'black'))
        self.assertFalse(test_board.play_token(3, 'red'))
        self.assertFalse(test_board.play_token(2, 'black'))
        self.assertFalse(test_board.play_token(4, 'red'))
        self.assertFalse(test_board.play_token(5, 'black'))
        self.assertFalse(test_board.play_token(6, 'red'))
        self.assertFalse(test_board.play_token(7, 'black'))

        ''' Now, verify that all columns are full '''
        with self.assertRaises(IndexError):
            test_board.play_token(1, 'red')
        with self.assertRaises(IndexError):
            test_board.play_token(2, 'black')
        with self.assertRaises(IndexError):
            test_board.play_token(3, 'red')
        with self.assertRaises(IndexError):
            test_board.play_token(4, 'black')
        with self.assertRaises(IndexError):
            test_board.play_token(5, 'red')
        with self.assertRaises(IndexError):
            test_board.play_token(6, 'black')
        with self.assertRaises(IndexError):
            test_board.play_token(7, 'red')
