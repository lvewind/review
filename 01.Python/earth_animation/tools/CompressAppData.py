import os
import subprocess

bandizip = r"C:\Program Files\Bandizip\Bandizip.exe"


coord_path = os.path.abspath(os.path.join(os.getcwd(), "..", "data/coordinate/"))
coord_zip = os.path.abspath(os.path.join(os.getcwd(), "..", "data/coordinate/64.zip"))

img_path = os.path.abspath(os.path.join(os.getcwd(), "..", "data/image/"))
img_zip = os.path.abspath(os.path.join(os.getcwd(), "..", "data/image/64.zip"))

pwd_coord = "-p:U2FsdGVkX1826P+lqv/SP5kHh4PcuUpf1OgQF4CeuZg="
pwd_img = "-p:U2FsdGVkX1+r0PadCFzr1UrxWnUiM9Clic9C+ze90dY="

if os.path.exists(coord_zip):
    os.remove(coord_zip)

if os.path.exists(img_zip):
    os.remove(img_zip)

subprocess.Popen([bandizip, "c", "-y", pwd_coord, coord_zip, coord_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.Popen([bandizip, "c", "-y", pwd_img, img_zip, img_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
