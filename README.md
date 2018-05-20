# icon-resizer
iOS app icon resizing tool
![Icons](https://developer.apple.com/ios/human-interface-guidelines/images/CustomIcon_Sizes.svg)

Resize app icons and glyphs to Apple's required sizes for iOS app development.

## Installation
icon-resizer requires `Python3` and can be installed using `pip`.
```bash
$ pip install icon-resizer
```
## Example
```bash
# Saves resized images in a folder called output in the current directory.
$ icon appicon resize my-icon.png
```
## Usage 
Type `icon --help` for the usage pattern.
```bash
Usage: icon [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version  Show current version
  --help         Show this message and exit.

Commands:
  appicon  Manipulate raw app icon image
  tabbar   Manipulate raw tab bar glyph
```
