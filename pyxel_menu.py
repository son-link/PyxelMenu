import pyxel


class PyxelMenu:
    """ Pyxel class for generating, displaying and controlling a menu """

    def __init__(self, options: list, x: int, y: int, limit: int = 5):
        """Class constructor

        Args:
            options (list): A list with the options to add
            x (int): Position of the menu with respect to the left margin in pixels
            y (int): Position of the menu with respect to the up margin in pixels
            limit (int, optional): The limit of options to display. Defaults to 5.
        """
        self._limit = limit
        self._x = x
        self._y = y
        self._current_pos = 0
        self._cursor = '*'
        self._color = 7
        self._cursor_color = 7

        self._options = options

    def draw(self):
        ''' Draw the menu '''
        starty = self._y

        init = 0
        cursor_pos = self._current_pos

        if self._current_pos < len(self._options):
            if (
                self._current_pos > pyxel.floor(self._limit / 2) and 
                self._current_pos < len(self._options) - pyxel.floor(self._limit / 2)
            ):
                init = self._current_pos - pyxel.floor(self._limit / 2)
                cursor_pos = pyxel.floor(self._limit / 2)

            elif (
                self._current_pos >= len(self._options) - pyxel.floor(self._limit / 2)
            ):
                init = len(self._options) - self._limit
                cursor_pos = self._current_pos - init

        for i, option in enumerate(self._options[init:init + self._limit]):
            if i == cursor_pos:
                pyxel.text(self._x, starty, self._cursor, self._cursor_color)

            pyxel.text(self._x + (4 * len(self._cursor)) + 2, starty, option, self._color)
            starty += 8

    def get_current_pos(self):
        ''' Return selected option index '''
        return self._current_pos

    def get_current_text(self):
        ''' Return selected option text '''
        return self._options[self._current_pos]

    def move_up(self):
        ''' Move the cursor up one position '''
        if self._current_pos > 0:
            self._current_pos -= 1

    def move_down(self):
        ''' Move the cursor down one position '''
        if self._current_pos < len(self._options) - 1:
            self._current_pos += 1

    def set_text_color(self, color: int):
        """Defines the color of the options

        Args:
            color (int): The color index of the Pyxel palette to use for the options (0-15)
        """
        if color < 0 or color > 15:
            return

        self._color = color

    def set_cursor(self, color: int = 7, character: str = '*'):
        """To define the color and/or character of the menu cursor.
            It is not recommended to use more than three characters.

        Args:
            color (int): The color index of the Pyxel palette to use for the options (0-15). Defaults to 7
            character (str, optional): The character, or characters, to use for the cursor. Defaults to '*'.
        """
        self._cursor = character
        self._cursor_color = color

        if color < 0 or color > 15:
            self._cursor_color = 7
