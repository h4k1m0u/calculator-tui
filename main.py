#!/usr/bin/env python
"""
Render a terminal UI with menu & status bar
"""
import curses

from menu import Menu
from status_bar import draw_status_bar


def main(stdscr: 'curses._CursesWindow'):
    """
    Called by curses.wrapper() & restores terminal state at end of execution
    Explicit type hint for `stdscr` for autocomplete

    @param stdscr Main screen (Window) to print onto
    """
    # initialize & define terminal colors
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)

    # hide cursor & non-blocking `getch()`
    curses.curs_set(0)
    stdscr.nodelay(True)

    # menu
    items = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['0', '.', '=', '+'],
    ]
    menu = Menu(stdscr, items)

    # main loop
    while True:
        # clear only internal screen
        stdscr.erase()

        # render menu
        stdscr.attron(curses.A_BOLD | curses.color_pair(1))
        menu.draw()

        # status bar
        draw_status_bar(stdscr)

        # wait for keypress
        key = stdscr.getch()

        # menu navigation with arrow keys presses
        if key == curses.KEY_UP:
            menu.move_vertically(step=-1)
        elif key == curses.KEY_DOWN:
            menu.move_vertically(step=1)
        if key == curses.KEY_LEFT:
            menu.move_horizontally(step=-1)
        elif key == curses.KEY_RIGHT:
            menu.move_horizontally(step=1)
        elif key == ord('q'):
            break


if __name__ == '__main__':
    curses.wrapper(main)
