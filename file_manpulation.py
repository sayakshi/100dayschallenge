import os

#get_cwd = os.getcwd()
#print(get_cwd)

#

this_file = os.path.abspath(__file__)
BASEDIR =  os.path.dirname(this_file)
PROJ_DIR = os.path.dirname(BASEDIR)
#print(f"base dir {BASEDIR} and PROJ_DIR: {PROJ_DIR}")
#relative_path
template_location = os.path.join(BASEDIR, "template","template.txt")
#emplate_location =get_cwd +  "//template//template.txt"

content = ""

with open(template_location, "r") as fobj:
	content = fobj.read()

print(content.format(name = 'sayantan'))



