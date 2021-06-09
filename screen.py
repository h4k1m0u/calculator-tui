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
        n_rows, n_cols = stdscr.getmaxyx()
        self.window = stdscr.subwin(1, n_cols, n_rows - 2, 0)

    def draw(self, text):
        """
        Render given text on screen
        @param text string to render
        """
        self.window.addstr(0, 0, text, curses.A_REVERSE)
