import imageio.v3 as iio
import tkinter as tk
from tkinter import filedialog
from PIL import Image



root = tk.Tk()
root.withdraw()
registering = "NO"
images = []
height = 100
width = 100

 

print("Choose the images that you want for the gif min:2, max:5")

file_names = filedialog.askopenfilenames(
    title="Enter the images for the gif",
    filetypes=[("File Images", "*.png *.jpg *.jpeg *.bmp")]
)


while True:
    try:
        height = int(input("Height in px(positive): "))
        width = int(input("width in px(positive): "))
        if height > 0 and width > 0:
            break
    except:  
        print("The height and wdith needs to be positive Integer")


registering = input("Do you want to register the images in the size(YES/NO): ")

if 2 <= len(file_names) <= 5:

    for i, file in enumerate(file_names):
        img = iio.imread(file)
        pil_image = Image.fromarray(img)
        
        resized_image = pil_image.resize((width, height))  
        if registering.upper() == "YES":
            resized_image.save(f"image{i+1}.jpg") 
        images.append(resized_image)

    gif_name = input("What do you want to name it: ")
    duration = 500
    while True:
        try:
            duration = int(input("what's the duration positive integer: "))
            if duration > 0:
                break
        except ValueError:
            print("the duration need to be a positive integer")

    iio.imwrite(f"{gif_name}.gif", images, duration=duration, loop=0)    