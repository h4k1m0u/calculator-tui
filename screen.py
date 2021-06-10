#!/usr/bin/env python
"""
Calculator screen
"""
import curses


class Screen:
    def __init__(self, stdscr: 'curses._CursesWindow'):
        """
        @param stdscr parent window
        """
        # window just above status bar
        n_rows_stdscr, n_cols_stdscr = stdscr.getmaxyx()
        self.n_rows, self.n_cols = 1, n_cols_stdscr
        self.window = stdscr.subwin(
            self.n_rows, self.n_cols, n_rows_stdscr - 2, 0)
        self.content = ''

    def set_content(self, text):
        """
        Set screen content
        @param text string to set screen content to in `draw()`
        """
        self.content = text

    def draw(self):
        """
        Render given text on screen
        """
        self.window.addstr(0, 0, self.content, curses.A_REVERSE)
