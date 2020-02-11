import os
import glob
from PIL import Image
import numpy as np 

files = glob.glob('new/*.jpg')

##width = 350

for f in files:
    img = Image.open(f)
    """
    img_resize = img.resize((width, int(width * img.size[1] / img.size[0]))) 
    """
    img_crop = img.crop((0, 0, 350, 233))
    ftitle, fext = os.path.splitext(f)
    img_crop.save(ftitle + fext, quality=95)