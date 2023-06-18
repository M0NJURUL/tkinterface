from PIL import Image
import os
directory = os.chdir("D:\Shakil-Junior_Teacher\Python\pycharm\\tkinterface\projects\images\image converter")

for filename in os.listdir(directory):
    if filename.endswith(".png"):  
        image = Image.open(filename)
        icon_size = (64, 64)
        resized_image = image.resize(icon_size)
        desired_type = "ico" # jpeg/jpg/ico/png
        resized_image.save(f"converted_{filename[:-4]}.{desired_type}")
        print("Hello")
