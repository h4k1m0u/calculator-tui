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
        self.items = items
        self.window = stdscr.subwin(0, 0)
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

            self.window.addstr(i_item, 0, item, mode)
