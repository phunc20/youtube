import os
import time
from PIL import Image, ImageFilter
import concurrent.futures

directory = "images"
image_files = os.listdir(directory)
dir_save = "thumbnails"



t1 = time.perf_counter()
size = (1200, 1200)

def process(filename):
    image = Image.open(os.path.join(directory, filename))
    image = image.filter(ImageFilter.GaussianBlur(radius=15))
    image.thumbnail(size)
    image.save(os.path.join(dir_save, filename))
    print("{} processed.".format(filename))


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(process, image_files)


t2 = time.perf_counter()
print("script finished in {:.2f}(s).".format(t2-t1))
