from tkinter import Tk, filedialog, Label, Entry, Button, StringVar, messagebox
from PIL import Image
import os

def select_folder():
    folder_path = filedialog.askdirectory(title='Select Source Folder')  # shows dialog box and returns the path
    source_folder_var.set(folder_path)

def select_destination_folder():
    folder_path = filedialog.askdirectory(title='Select Destination Folder')  # shows dialog box and returns the path
    destination_folder_var.set(folder_path)

def compress_images():
    source_folder = source_folder_var.get()
    destination_folder = destination_folder_var.get()

    mywidth = 2000

    # Ensure both source and destination folders are selected
    if not source_folder or not destination_folder:
        messagebox.showerror("Error", "Please select both source and destination folders.")
        return

    # Iterate through each file in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # Open the image
            img_path = os.path.join(source_folder, filename)
            img = Image.open(img_path)

            # Calculate the new size
            width_percentage = mywidth / float(img.size[0])
            new_height = int(float(img.size[1]) * width_percentage)

            # Resize the image
            resized_img = img.resize((mywidth, new_height), Image.LANCZOS)

            # Save the resized image to the destination folder
            destination_path = os.path.join(destination_folder, f"compressed_{filename}")
            resized_img.save(destination_path)

    messagebox.showinfo("Complete", "Compression complete.")

# Tkinter setup
root = Tk()
root.title("Image Compression Tool")

# Variables to store folder paths
source_folder_var = StringVar()
destination_folder_var = StringVar()

# GUI components
source_folder_label = Label(root, text="Source Folder:")
source_folder_entry = Entry(root, textvariable=source_folder_var, state='readonly')
source_folder_button = Button(root, text="Browse", command=select_folder)

destination_folder_label = Label(root, text="Destination Folder:")
destination_folder_entry = Entry(root, textvariable=destination_folder_var, state='readonly')
destination_folder_button = Button(root, text="Browse", command=select_destination_folder)

compress_button = Button(root, text="Compress Images", command=compress_images)

# Grid layout
source_folder_label.grid(row=0, column=0, sticky='e', padx=5, pady=5)
source_folder_entry.grid(row=0, column=1, columnspan=2, sticky='we', pady=5)
source_folder_button.grid(row=0, column=3, sticky='w', padx=5, pady=5)

destination_folder_label.grid(row=1, column=0, sticky='e', padx=5, pady=5)
destination_folder_entry.grid(row=1, column=1, columnspan=2, sticky='we', pady=5)
destination_folder_button.grid(row=1, column=3, sticky='w', padx=5, pady=5)

compress_button.grid(row=2, column=0, columnspan=4, pady=10)

# Start the Tkinter main loop
root.mainloop()
