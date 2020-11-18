import os
import time
from PIL import Image, ImageFilter

directory = "images"
image_files = os.listdir(directory)
dir_save = "thumbnails"



t1 = time.perf_counter()
size = (1200, 1200)

for f in image_files:
    image = Image.open(os.path.join(directory, f))
    image = image.filter(ImageFilter.GaussianBlur(radius=15))
    image.thumbnail(size)
    image.save(os.path.join(dir_save, f))
    print("{} processed.".format(f))

t2 = time.perf_counter()
print("script finished in {:.2f}(s).".format(t2-t1))
