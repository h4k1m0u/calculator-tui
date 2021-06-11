"""
Keyboard button
"""
import curses


class Button:
    """
    Calculator's keyboard button
    """
    def __init__(self, window: 'curses._CursesWindow', row, col, label):
        """
        @param window Window to host button
        @param row y-position of button relative to window
        @param col x-position of button relative to window
        @param label Button label
        """
        self.window = window
        self.row = row
        self.col = col
        self.label = label

    def draw(self, mode):
        """
       @param mode For highlighting the button (A_REVERSE) or not (A_NORMAL)
        """
        # `insstr()` doesn't push cursor outside window (error) like `addstr()`
        self.window.insstr(self.row, self.col, self.label, mode)
