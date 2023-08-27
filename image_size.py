import os
import shutil
from PIL import Image


start_directory = 'static/pics'

def size_to_string(size):
    if size > 1000000:
        return str(size/1000000) + " MB"
    if size > 1000:
        return str(size/1000) + " KB"
    return str(size) + " B"

for dir_name in sorted(os.listdir(start_directory)):
    if os.path.isdir(os.path.join(start_directory, dir_name)):
        print(dir_name)
        #os.mkdir( os.path.join("static/backup", dir_name), )
        files = os.listdir(os.path.join(start_directory, dir_name))
        sorted_files = sorted(files, key=lambda name: name.lower())
        for file_name in sorted_files:
            size = os.path.getsize(os.path.join(start_directory, dir_name, file_name))
            if size == 0 or size > 3000000:
                print(file_name + ": ", size_to_string(size))
                src = os.path.join(start_directory, dir_name, file_name)
                #dst = os.path.join("static/backup", dir_name, file_name)
                # shutil.copy2(src, dst)


                img = Image.open(src)  # My image is a 200x374 jpeg that is 102kb large
                (width, height) = img.size
                factor = width/1200
                new_width = int(width/factor)
                new_height = int(height/factor)
                resized = img.resize((new_width,new_height),Image.Resampling.BICUBIC)
                resized.save(src, optimize=True, quality=95)  # The saved downsized image size is 22.9kb
                space = os.path.getsize(src)
                print("Size: (" + str(width) + " , " + str(height) + ") Factor: " + str(factor) + " New size (" + str(new_width) + " , " + str(new_height) + ") New Disc Space: " + size_to_string(space))
                # downsize the image with an ANTIALIAS filter (gives the highest quality)