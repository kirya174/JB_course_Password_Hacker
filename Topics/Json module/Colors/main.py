import json


colors = {"rainbow": ["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
          "CMYK": ["cyan", "magenta", "yellow", "key color"],
          "RBG": ["red", "blue", "green"]}

# write your code here
with open("colors.json", "w") as output_file:
    json.dump(colors, output_file)
