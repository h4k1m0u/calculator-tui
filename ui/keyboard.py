#!/usr/bin/env python
"""
Inspired by menu class from: https://stackoverflow.com/a/14205494/2228912
"""
import curses
from .button import Button


class Keyboard:
    """
    Calculator keyboard
    """
    def __init__(self, stdscr: 'curses._CursesWindow', labels):
        """
        @param stdscr parent window
        @param labels  2D list of labels for keyboard buttons
        """
        # leave two characters on all sides for borders
        self.border = 1

        # position menu at center of main screen (padding around for borders)
        self.labels = labels
        self.n_rows = len(self.labels)
        self.n_cols = len(self.labels[0])
        self.depth = len(self.labels[0][0]) + self.border

        # current cursor position (row, column)
        self.row = 0
        self.col = 0

        # subwin: window shares memory with parent (no need for its repainting)
        self.height = self.n_rows + 2 * self.border
        self.width = self.n_cols * self.depth + 2 * self.border
        self.window = stdscr.subwin(
            self.height,
            self.width,
            1 + 2 * self.border, 0)

        # instantiate buttons
        self.__create_buttons()

    def move_vertically(self, step):
        """
        Move cursor to menu item `step` items below or above current one

        @param step Step by which to move cursor
                    Sign determines whether to move up/down
        """
        if self.row + step < 0 or \
           self.row + step > len(self.labels) - 1:
            return

        self.row = self.row + step

    def move_horizontally(self, step):
        """
        Move cursor to menu item `step` items to right/left of current one

        @param step Step by which to move cursor
                    Sign determines whether to move right/left
        """
        if self.col + step < 0 or \
           self.col + step > len(self.labels[0]) - 1:
            return

        self.col = self.col + step

    def get_key(self):
        """
        Get label of currently highlighted calculator key
        @returns button label
        """
        return self.labels[self.row][self.col]

    def __create_buttons(self):
        """
        Private method for instantiating keyboard buttons
        """
        self.buttons = []
        for i_row in range(self.n_rows):
            for i_col in range(self.n_cols):
                label = self.labels[i_row][i_col]
                row = i_row + self.border
                col = i_col * self.depth + self.border

                self.buttons.append(
                    Button(self.window, row, col, label))

    def draw(self):
        """
        Render menu items & highlight currently selected one
        """
        # render calculator keys (active/inactive)
        for i_row in range(self.n_rows):
            for i_col in range(self.n_cols):
                if i_row == self.row and i_col == self.col:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                self.buttons[i_row * self.n_cols + i_col].draw(mode)

        # border around window
        self.window.box()
