# Changelog

## [0.2.0] - 2024-08-29

### Added

- 4 new setters:
	- set_cursor_img: Set an image from the image bank as the cursor.
	- set_cursor_pos: Set cursor position.
	- set_highlight_color: Sets the highlight color for the indicated option.
	- set_options: Set the options for the menu
- 6 examples
- A script to generate the HTML files of the examples and add them to the documentation web site.

### Changed

- The use of characters as cursor has been replaced by the use of three geometric shapes: circle, triangle and square.
- The constructor's options parameter is now optional and becomes the third parameter.
- Better documentation with examples.

## [0.1.1] - 2024-08-24

### Added

- Added two news setters methods:
	- set_text_color: Set the color of the options. Defaults: 7
	- set_cursor: Set the character and/or color for the cursor. Defaults: * an 7
- Added page with documentation
- This changelog

### Changed

- Remove color, cursor and cursor_color parameters in the constructor function
- The number of characters used for the cursor is now taken into account when adding the margin to the options.
- Two methods have been moved to have them in alphabetical order for better readability

## [0.1.0] - 2024-08-22

### Changed

- First release

[0.2.0]:  https://github.com/son-link/PyxelMenu/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/son-link/PyxelMenu/compare/v0.1.0...v0.1.1
