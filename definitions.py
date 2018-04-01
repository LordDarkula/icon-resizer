import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

icon_sizes = [29, 58, 87, 40, 80, 60, 120, 180, 76, 152, 512, 1024]
icon_names = ["Icon-Small.png",
              "Icon-Small@2x.png",
              "Icon-Small@3x.png",
              "Icon-Small-40.png",
              "Icon-Small-40@2x.png",
              "Icon-60.png",
              "Icon-60@2x.png",
              "Icon-60@3x.png",
              "Icon-76.png",
              "Icon-76@2x.png",
              "iTunesArtwork.png",
              "iTunesArtwork@2x.png", ]
icon_dict = dict(zip(icon_names, icon_sizes))

tab_bar_dict = {
    "-Bar": 23,
    "-Bar@2x": 46,
    "-Bar@3x": 69,
}
