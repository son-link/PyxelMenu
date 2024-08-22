import pyxel


class PyxelMenu:
    """ Pyxel class for generating, displaying and controlling a menu """

    def __init__(
        self, options: list, x: int, y: int,
        limit: int = 7, color: int = 12, cursor: str = '*',
        cursor_color: int = 7
    ):
        self._limit = limit
        self._x = x
        self._y = y
        self._current_pos = 0
        self._cursor = cursor
        self._color = color
        self._cursor_color = cursor_color

        self._options = options

    def get_current_pos(self):
        ''' Return selected option index '''
        return self._current_pos

    def get_current_text(self):
        ''' Return selected option text '''
        return self._options[self._current_pos]

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

            pyxel.text(self._x + 6, starty, option, self._color)
            starty += 8

    def move_up(self):
        ''' Move the cursor up one position '''
        if self._current_pos > 0:
            self._current_pos -= 1

    def move_down(self):
        ''' Move the cursor down one position '''
        if self._current_pos < len(self._options) - 1:
            self._current_pos += 1
