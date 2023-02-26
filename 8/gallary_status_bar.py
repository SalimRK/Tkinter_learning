from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("gallery.py")
root.iconbitmap("D:\MyPC\Projects\coding\python\Tkinter_learning\\8\Photo-icon.ico")

# Define the image directory and a list to store the image file paths
directory = "D:\MyPC\Projects\coding\python\Tkinter_learning\\8\images"
image_paths = []

# Loop through the files in the directory and add the file paths to the list
for root_path, _, files in os.walk(directory):
    for filename in files:
        filepath = os.path.join(root_path, filename)
        image_paths.append(filepath)


# Define the show_image() function to display the current image
def show_image():
    global current_image_index

    # Load the image and resize it to fit the label
    image = Image.open(image_paths[current_image_index])
    image = image.resize((300, 300), resample=Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Set the label's image to the loaded image and update the display
    image_label.config(image=photo)
    image_label.image = photo

    # Enable or disable the navigation buttons based on the current image index
    if current_image_index == 0:
        backward_button.config(state=DISABLED)
    else:
        backward_button.config(state=NORMAL)

    if current_image_index == len(image_paths) - 1:
        forward_button.config(state=DISABLED)
    else:
        forward_button.config(state=NORMAL)


# Define the next_image() function to display the next image
def next_image():
    global current_image_index
    current_image_index += 1
    show_image()
    status = Label(root, text=f"image {current_image_index+1} of {len(image_paths)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(column=0, row=3, columnspan=3, sticky=W+E)

# Define the prev_image() function to display the previous image
def prev_image():
    global current_image_index
    current_image_index -= 1
    show_image()
    status = Label(root, text=f"image {current_image_index+1} of {len(image_paths)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(column=0, row=3, columnspan=3, sticky=W + E)


# Create an empty label to display the images
image_label = Label(root)
image_label.grid(column=0, row=0, rowspan=3, pady=5)

# Create the navigation buttons and disable them until an image is displayed
exit_button = Button(root, text="Exit", command=root.quit)
forward_button = Button(root, text=">>", command=next_image, state=DISABLED)
backward_button = Button(root, text="<<", command=prev_image, state=DISABLED)

forward_button.grid(column=1, row=0)
exit_button.grid(column=1, row=1)
backward_button.grid(column=1, row=2)

# Set the current image index and display the first image
current_image_index = 0
show_image()
status = Label(root, text=f"image {current_image_index+1} of {len(image_paths)}", bd=1, relief=SUNKEN, anchor=E)
status.grid(column=0, row=3, columnspan=3, sticky=W+E)
# Start the main event loop
root.mainloop()
