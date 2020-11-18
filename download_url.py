import os
import requests
import shutil

this_file = os.path.abspath(__file__)
BASEDIR =  os.path.dirname(this_file)


file_dir = os.path.join(BASEDIR, "Download_image")
os.makedirs(file_dir, exist_ok=True)
#emplate_location =get_cwd +  "//template//template.txt"

url = "https://i.nextmedia.com.au/News/kali%20linux.png"

dl_path =  os.path.basename(url)
print(dl_path)
download_img_path = os.path.join(file_dir, dl_path)


#makes new directory

#Will keep the download stream open and small file
# r = requests.get(url, stream = True)
# r.raise_for_status()

# with open(download_img_path, 'wb') as imgobj:
# 	imgobj.write(r.content)


with requests.get(url, stream = True) as r:
	with open(download_img_path, 'wb') as imgobj:
		shutil.copyfileobj(r.raw, imgobj)
		





