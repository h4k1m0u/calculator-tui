#!/usr/bin/env python
"""
Calculator screen
"""
import curses


class Screen:
    def __init__(self, stdscr: 'curses._CursesWindow', width):
        """
        @param stdscr Parent window
        @param width Screen width matches that of calculator keyboard
        """
        # leave two characters on all sides for borders
        self.border = 1

        # screen positionned just above calculator keyboard
        n_rows_stdscr, n_cols_stdscr = stdscr.getmaxyx()
        self.n_rows = 1 + 2 * self.border
        self.window = stdscr.subwin(
            self.n_rows, width, 0, 0)
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
        self.window.addstr(self.border, self.border, self.content, curses.A_REVERSE)

        # border around window
        self.window.box()
