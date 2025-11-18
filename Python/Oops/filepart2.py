from pathlib import Path
path = Path()
# glob gives all current files or directories with * means everything
print(path.glob('*.*'))
print(path.glob('*.py'))      # sreach all py files
# now iterate over map object
for file in path.glob('*.py'):
    print(file)
# glob to search file using patters as (*) all files etc 