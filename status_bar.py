#!/usr/bin/env python
"""
Status bar at the bottom showing running clock
"""
import curses
import time


def draw_status_bar(stdscr):
    """
    Draw status bar
    """
    # subwin: window shares memory with parent (no need for its repainting)
    n_rows_stdscr, n_cols_stdscr = stdscr.getmaxyx()
    y_statusbar = n_rows_stdscr - 1
    window = stdscr.subwin(1, n_cols_stdscr, y_statusbar, 0)
    window.attron(curses.color_pair(2))

    # shortcuts on left of statusbar
    shortcuts = ' up/down: Navigation, enter: Select, q: Quit'
    window.addstr(0, 0, shortcuts)

    # current time on right of statusbar
    current_time = time.strftime('%H:%M:%S', time.localtime())
    window.addstr(
        0, n_cols_stdscr - 1 - len(current_time), current_time)

    # fill space in between
    window.addstr(
        0, len(shortcuts),
        ' ' * (n_cols_stdscr - 1 - (len(shortcuts) + len(current_time))))
