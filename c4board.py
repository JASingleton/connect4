#!/usr/bin/python2

from exceptions import *


class c4board(object):
    ''' Structure is a dictionary of populated "holes" in a Connect4 board.
        Locations are numbered with:
            - Rows being numbered 1-6 (left to right on the board)
            - Columns being numbered 1-7 (bottom to top on the board)
        The value of the contents are strings representing the colors, i.e.
        'red' or 'black'

        Each hole has a key of (row, column); values are 'red' and 'black';
        empty holes are simply absent in the dictionary. The dictionary is
        used as a way to get a hashed (hence, fast) lookup for a specific
        row/column.

        Structure also contains a list of "max_column" values, each indicating
        the topmost currently-filled position in that column. (Index 0 is
        unused, so that indices match column numbers described above.)


        Notes:
        * The interface supports variations in the number of rows/columns, but
          the implementation does not yet perform error-checking to ensure a
          valid board configuration.
    '''
    def __init__(self, board_rows=6, board_columns=7):
        ''' Create a list of empty columns. '''
        self.board_rows = board_rows
        self.board_columns = board_columns

        ''' Make _full_columns big enough that we can index by
            column value. (index 0 will be ignored.)
        '''
        self._full_columns = [0 for i in range(1, self.board_columns + 2)]
        self._holes = dict()
        self._last_play_row = None
        self._last_play_column = None
        self._last_play_color = None

    def play_token(self, column, color):
        ''' Play the token of the indicated color in the indicated column.
            Raises exceptions for any invalid moves.
            Returns True if the play results in a win; False otherwise.
        '''
        if column > self.board_columns:
            ''' Column value too large for the board. '''
            raise IndexError('Column {0} is larger than the board.'.format(
                              column))
        elif column < 1:
            ''' Invalid (too small) column value. '''
            raise IndexError('Column {0} is invalid.'.format(column))
        elif (color != 'red' and color != 'black'):
            raise ValueError('Invalid piece color {0}'.format(color))
        elif self._full_columns[column] >= self.board_rows:
            ''' If the column was already full, cannot place this piece. '''
            raise IndexError('Column {0} is already full.'.format(column))
        elif (self._last_play_color is not None and
              self._last_play_color == color):
            raise ValueError('Two {0} tokens played consecutively; colors '
                             'must alternate during play.'.format(color))

        ''' Insert the piece '''
        row_to_insert = self._full_columns[column] + 1
        location = (row_to_insert, column)
        self._full_columns[column] += 1
        self._holes[location] = color
        self._last_play_row = row_to_insert
        self._last_play_column = column
        self._last_play_color = color

        ''' Check for a win. '''
        return self._has_win(row_to_insert, column, color)

    def __str__(self):
        ''' row_string is a list of strings, each representing the contents
            of a row.
        '''

        row_strings = ['' for i in range(self.board_rows + 1)]
        for row in range(1, self.board_rows + 1):
            for column in range(1, self.board_columns + 1):
                if (row, column) not in self._holes:
                    row_strings[row] += '-'
                elif self._holes[(row, column)] == 'red':
                    row_strings[row] += 'R'
                elif self._holes[(row, column)] == 'black':
                    row_strings[row] += 'B'
        row_strings.reverse()
        out_str = ''
        for row in row_strings:
            out_str += row + '\n'
        return out_str

    def __repr__(self):
        return str((self._full_columns, self._holes))

    def _calculate_win_range(self, row, column, row_increment,
                             column_increment):
        ''' Produce a sequence of the (valid) positions that could constitute
            a "win" from the row/column provided. row/column_increment
            are as follows:
                1, 1: Sequence diagonally up and to the right (and down-left)
                -1, 1: Sequence diagonally down and to the right (and up-left)
                -1, 0: Sequence vertically up and down
                0, 1: Sequence horizontally.
            No error-checking is performed on the increments, so other
            combinations will produce spurious results. (Inverting the
            signs on both values will product the same sequence elements,
            but in reverse order.)

            The result is a sequence of (row, column) tuples, with the
            indicated row/column being in the middle. Any elements that
            fall outside the size of the board are excluded, so the
            size of the actual sequence returned will vary based on the
            position of the inserted token.
        '''
        start_sequence = [(row + (row_increment * multiplier),
                          column + (column_increment * multiplier)) for
                          multiplier in range(-3, 4)]
        hole_sequence = [(r, c) for (r, c) in start_sequence if
                         ((r > 0 and r <= self.board_rows) and
                          (c > 0 and c <= self.board_columns))]
        return hole_sequence

    def _sequence_has_win(self, sequence, color):
        ''' Determines whether the positions indicated in the sequence
            contain four tokens of the color indicated by the argument.

            Returns True if there are four such sequential tokens,
            False otherwise.
        '''
        color_count = 0
        for (row, column) in sequence:
            if (row, column) in self._holes and \
               self._holes[(row, column)] == color:
                color_count += 1
                if color_count == 4:
                    return True
            else:
                color_count = 0
        return False

    def _has_win(self, row, column, color):
        ''' Get the last play. Check for matches:
            - Horizontally to the left or right
            - Vertically up or down
            - Diagonally in four directions (up-right, down-right, up-left,
              down-left)
        '''
        vertical_sequence = self._calculate_win_range(row, column, -1, 0)
        if self._sequence_has_win(vertical_sequence, color):
            return True
        horizontal_sequence = self._calculate_win_range(row, column, 0, 1)
        if self._sequence_has_win(horizontal_sequence, color):
            return True
        upright_diag_sequence = self._calculate_win_range(row, column, 1, 1)
        if self._sequence_has_win(upright_diag_sequence, color):
            return True
        downright_diag_sequence = self._calculate_win_range(row, column, -1, 1)
        if self._sequence_has_win(downright_diag_sequence, color):
            return True
        return False

    def has_win(self):
        if self._last_play_row is None:
            return False
        return self._has_win(self._last_play_row,
                             self._last_play_column,
                             self._last_play_color)
