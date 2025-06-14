import imageio.v3 as iio
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_names = []
images = []

print("select the images that you want to for the gif min:2, max:5")

file_path = filedialog.askopenfilenames(
    title="Enter the images for the gif",
    filetypes= [("Image Files", "*.png *.jpg *.jpeg *.bmp")]
)

for file in file_path:
    file_names.append(file)

if 2 <= len(file_names) <= 5:
    for file_name in file_names:
        images.append(iio.imread(file_name))

    gif_name = input("Enter the name of your GIF: ")
    duration = 500    
    while True:
        try:
            duration = int(input("Enter how long each picture should show in the GIF, in milliseconds: "))
            if duration > 0:
                break
        except:
            print("The duration needs to be an integer!!")     
    iio.imwrite(f"{gif_name}.gif", images, duration=duration, loop=0)      
else:
    print("The number of images needs to be between 2 and 5")

   