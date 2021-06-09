#!/usr/bin/env python
"""
Inspired by menu class from: https://stackoverflow.com/a/14205494/2228912
"""
import curses


class Keyboard:
    """
    Calculator keyboard
    """
    def __init__(self, stdscr: 'curses._CursesWindow', items):
        """
        @param stdscr parent window
        @param items  2D list of labels for keyboard buttons
        """
        # position menu at center of main screen (padding around for borders)
        self.items = items
        self.n_rows = len(self.items)
        self.n_cols = len(self.items[0])
        self.depth = len(self.items[0][0])
        self.row = 0
        self.col = 0

        # subwin: window shares memory with parent (no need for its repainting)
        self.window = stdscr.subwin(
            self.n_rows, self.n_cols * self.depth + 1, 0, 0)

        # needed so curses can interpret arrow keys presses
        # self.window.keypad(1)

    def move_vertically(self, step):
        """
        Move cursor to menu item `step` items below or above current one

        @param step Step by which to move cursor
                    Sign determines whether to move up/down
        """
        if self.row + step < 0 or \
           self.row + step > len(self.items) - 1:
            return

        self.row = self.row + step

    def move_horizontally(self, step):
        """
        Move cursor to menu item `step` items to right/left of current one

        @param step Step by which to move cursor
                    Sign determines whether to move right/left
        """
        if self.col + step < 0 or \
           self.col + step > len(self.items[0]) - 1:
            return

        self.col = self.col + step

    def get_key(self):
        """
        Get label of currently highlighted calculator key
        """
        key = self.items[self.row][self.col]
        return key

    def draw(self):
        """
        Render menu items & highlight currently selected one
        """
        # render menu items (active/inactive)
        for i_row in range(self.n_rows):
            for i_col in range(self.n_cols):
                if i_row == self.row and i_col == self.col:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                text = self.items[i_row][i_col]
                self.window.addstr(i_row, i_col * self.depth, text, mode)

        # border around menu
        # self.window.box()
