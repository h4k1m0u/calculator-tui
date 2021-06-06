#!/usr/bin/env python
"""
Inspired by: https://stackoverflow.com/a/14205494/2228912
"""
import curses
import curses.panel


def make_panel(stdscr, content, row, col):
    """
    Important: return panel & keep a copy, otherwise will be garbage collected
    """
    # subwin: window shares memory with parent (no need for its repainting)
    win = stdscr.subwin(row, col)
    win.box()
    win.addstr(0, 0, content)
    panel = curses.panel.new_panel(win)

    return panel
