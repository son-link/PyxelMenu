# This example shows the possibility to indicate a different color to highlight the selected option.

import pyxel
from pyxel_menu import PyxelMenu


class Example:
    def __init__(self):
        self.current_text = ''
        self.current_pos = ''
        menu_options = []

        for i in range(1, 21):
            menu_options.append(f'Option {i}')

        self.menu = PyxelMenu(8, 8, menu_options, 10)
        self.menu.set_cursor(color=8)
        self.menu.set_highlight_color(10)

        pyxel.init(166, 120, title='PyxelMenu Example 005: Highlight')

        pyxel.run(self.update, self.draw)

    def update(self):
        if (
            pyxel.btnp(pyxel.KEY_UP) or
            pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP)
        ):
            self.menu.move_up()
        elif (
            pyxel.btnp(pyxel.KEY_DOWN) or
            pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN)
        ):
            self.menu.move_down()
        elif (
            pyxel.btnp(pyxel.KEY_RETURN) or
            pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A)
        ):
            self.current_pos = self.menu.get_current_pos()
            self.current_text = self.menu.get_current_text()

    def draw(self):
        pyxel.cls(0)
        self.menu.draw()
        pyxel.text(64, 8, 'Press enter:', 7)
        pyxel.text(64, 16, f'Position: {self.current_pos}', 2)
        pyxel.text(64, 22, f'Text:     {self.current_text}', 2)


if __name__ == '__main__':
    example = Example()
