#!/usr/bin/env python
"""
Inspired by: https://stackoverflow.com/a/14205494/2228912
"""
import curses


class Menu:
    """
    Menu with fixed items
    """
    def __init__(self, stdscr: 'curses._CursesWindow', items):
        """
        @param items  labels for menu items
        @param stdscr parent window
        """
        # position menu at center of main screen (padding around for borders)
        self.items = items
        n_rows_stdscr, n_cols_stdscr = stdscr.getmaxyx()
        max_len_item = max(len(item) for item in self.items)
        n_rows, n_cols = len(self.items) + 2, max_len_item + 2
        col = n_cols_stdscr // 2 - max_len_item // 2
        row = n_rows_stdscr // 2 - n_rows // 2

        # subwin: window shares memory with parent (no need for its repainting)
        self.window = stdscr.subwin(n_rows, n_cols, row, col)
        self.position = 0

        # needed so curses can interpret arrow keys presses
        self.window.keypad(1)

    def move(self, step):
        """
        Move cursor to menu item `step` items below or above current one

        @param step Step by which to move cursor
                    Sign determines whether to move up/down
        """
        if self.position + step < 0 or \
           self.position + step > len(self.items) - 1:
            return

        self.position = self.position + step

    def draw(self):
        """
        Render menu items & highlight currently selected one
        """
        # render menu items (active/inactive)
        for i_item, item in enumerate(self.items):
            if i_item == self.position:
                mode = curses.A_REVERSE
            else:
                mode = curses.A_NORMAL

            self.window.addstr(i_item + 1, 1, item, mode)

        # border around menu
        self.window.box()
