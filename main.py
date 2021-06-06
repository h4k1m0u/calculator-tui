#!/usr/bin/env python
"""
Render a terminal UI with menu & status bar
"""
import curses
import curses.panel

from menu import Menu
from panel import make_panel
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
    items = ['Run game', 'Options', 'Quit game']
    menu = Menu(stdscr, items)

    # main loop
    while True:
        # clear only internal screen
        stdscr.erase()

        # render menu
        stdscr.attron(curses.A_BOLD | curses.color_pair(1))
        menu.draw()

        # panels: windows with depth (no linters) - update virtual panels stack
        # panel1 = make_panel(stdscr, 'Panel1', 10, 10, 20, 20)  # noqa: F841,E501 #pylint: disable=unused-variable
        # panel2 = make_panel(stdscr, 'Panel2', 10, 10, 25, 25)  # noqa: F841,E501 #pylint: disable=unused-variable

        # status bar
        draw_status_bar(stdscr)

        # wait for keypress
        key = stdscr.getch()

        # menu navigation with arrow keys presses
        if key == curses.KEY_UP:
            menu.move(step=-1)
        elif key == curses.KEY_DOWN:
            menu.move(step=1)
        elif (key == ord('\n') and menu.position == len(items) - 1) or \
                key == ord('q'):
            break


if __name__ == '__main__':
    curses.wrapper(main)
