#!/usr/bin/env python
"""
Render a terminal UI with menu & status bar
"""
import curses

from ui.keyboard import Keyboard
from ui.screen import Screen
from ui.status_bar import draw_status_bar


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
    screen = Screen(stdscr, keyboard.width)

    # operands & operation
    operand1 = operand2 = 0
    operation = ''
    screen_content = ''

    # main loop
    while True:
        # clear only internal screen
        stdscr.erase()

        # render calculator keyboard/screen
        stdscr.attron(curses.A_BOLD | curses.color_pair(1))
        keyboard.draw()
        screen.draw()

        # status bar
        draw_status_bar(stdscr)

        # wait for keypress
        key = stdscr.getch()

        # keyboard navigation with arrow keys presses
        if key == curses.KEY_UP:
            keyboard.move_vertically(step=-1)
        elif key == curses.KEY_DOWN:
            keyboard.move_vertically(step=1)
        elif key == curses.KEY_LEFT:
            keyboard.move_horizontally(step=-1)
        elif key == curses.KEY_RIGHT:
            keyboard.move_horizontally(step=1)
        elif key == ord('\n'):
            character = keyboard.get_key()

            if character.isdigit():
                # one of two operands
                screen_content += character
            elif character in ['/', '*', '-', '+']:
                # save first operand and operation & clean screen
                operand1 = int(screen_content)
                operation = character
                screen_content = ''
            elif character == '=':
                # evaluate operation between two operands
                operand2 = int(screen_content)
                screen_content = str(
                    eval('{} {} {}'.format(operand1, operation, operand2)))

            # update screen with operands or result
            screen.set_content(screen_content)
        elif key == ord('q'):
            break


if __name__ == '__main__':
    curses.wrapper(main)
