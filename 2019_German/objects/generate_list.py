# Usage like: python3 object_list_generator_new.py objects/ > list.markdown
import os
import sys

rootdir = sys.argv[1]
os.system("find . -name '*.jpg' -execdir mogrify -resize 200x {} \;")
for subdir, dirs, files in os.walk(rootdir):
    print("# Class %s" % subdir[subdir.find("/")+1:])
    print("""
| Objectname               |  Image                   |
:-------------------------:|:-------------------------:""")
    for file in files:
        print("| %s  |  ![](%s) |" % (file[:file.find(".")], os.path.join(subdir, file)))
    print("\n")

# execute pandoc <filename>.markdown -o <filename>.pdf
