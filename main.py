#!/usr/bin/env python
"""
Render a terminal UI with menu & status bar
"""
import curses

from keyboard import Keyboard
from screen import Screen
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

    # calculator keyboard & screen
    items = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['0', '.', '=', '+'],
    ]
    keyboard = Keyboard(stdscr, items)
    screen = Screen(stdscr)
    key_pressed = ''

    # main loop
    while True:
        # clear only internal screen
        stdscr.erase()

        # render calculator keyboard & screen
        stdscr.attron(curses.A_BOLD | curses.color_pair(1))
        keyboard.draw()
        screen.draw(key_pressed)

        # status bar
        draw_status_bar(stdscr)

        # wait for keypress
        character = stdscr.getch()

        # keyboard navigation with arrow keys presses
        if character == curses.KEY_UP:
            keyboard.move_vertically(step=-1)
        elif character == curses.KEY_DOWN:
            keyboard.move_vertically(step=1)
        if character == curses.KEY_LEFT:
            keyboard.move_horizontally(step=-1)
        elif character == curses.KEY_RIGHT:
            keyboard.move_horizontally(step=1)
        elif character == ord('\n'):
            key_pressed = keyboard.get_key()
        elif character == ord('q'):
            break

        # stdscr.refresh()


if __name__ == '__main__':
    curses.wrapper(main)
