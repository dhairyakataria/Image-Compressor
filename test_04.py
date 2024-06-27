from tkinter import Tk, filedialog, Label, Entry, Button, StringVar, messagebox, ttk
from PIL import Image
import os

def select_folder():
    folder_path = filedialog.askdirectory(title='Select Source Folder')  # shows dialog box and returns the path
    source_folder_var.set(folder_path)
    single_image_var.set("")  # Reset single image path when a folder is selected

def select_destination_folder():
    folder_path = filedialog.askdirectory(title='Select Destination Folder')  # shows dialog box and returns the path
    destination_folder_var.set(folder_path)

def select_single_image():
    file_path = filedialog.askopenfilename(title='Select Image File', filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    single_image_var.set(file_path)
    source_folder_var.set("")  # Reset source folder when a single image is selected

def compress_images():
    source_folder = source_folder_var.get()
    destination_folder = destination_folder_var.get()
    single_image = single_image_var.get()

    mywidth = 2000

    # Ensure either a source folder or a single image is selected, not both
    if (not source_folder and not single_image) or (source_folder and single_image):
        messagebox.showerror("Error", "Please select either a source folder or a single image file.")
        return

    # If a single image is selected, compress it
    if single_image:
        compress_single_image(single_image, destination_folder)
    else:
        # Iterate through each file in the source folder
        for filename in os.listdir(source_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                # Compress each image in the source folder
                img_path = os.path.join(source_folder, filename)
                compress_single_image(img_path, destination_folder)

    messagebox.showinfo("Complete", "Compression complete.")

def compress_single_image(img_path, destination_folder):
    mywidth = 2000

    # Open the image
    img = Image.open(img_path)

    # Calculate the new size
    width_percentage = mywidth / float(img.size[0])
    new_height = int(float(img.size[1]) * width_percentage)

    # Resize the image
    resized_img = img.resize((mywidth, new_height), Image.LANCZOS)

    # Save the resized image to the destination folder
    filename = os.path.basename(img_path)
    destination_path = os.path.join(destination_folder, f"compressed_{filename}")
    resized_img.save(destination_path)

# Tkinter setup
root = Tk()
root.title("Image Compression Tool")

# Variables to store folder paths
source_folder_var = StringVar()
destination_folder_var = StringVar()
single_image_var = StringVar()

# Title label
title_label = Label(root, text="Image Compression Tool", font=("Helvetica", 16, "bold"), pady=10)

# Instructions label
instructions_label = Label(root, text="Select either a source folder or a single image file, select a destination folder, and then press 'Compress Images'.",
                          font=("Helvetica", 12), pady=10)

# Source folder components
source_folder_label = Label(root, text="Source Folder:", font=("Helvetica", 12))
source_folder_entry = Entry(root, textvariable=source_folder_var, state='readonly', font=("Helvetica", 12))
source_folder_button = Button(root, text="Browse", command=select_folder, font=("Helvetica", 12))

# Single image components
single_image_label = Label(root, text="Single Image File:", font=("Helvetica", 12))
single_image_entry = Entry(root, textvariable=single_image_var, state='readonly', font=("Helvetica", 12))
single_image_button = Button(root, text="Browse", command=select_single_image, font=("Helvetica", 12))

# Destination folder components
destination_folder_label = Label(root, text="Destination Folder:", font=("Helvetica", 12))
destination_folder_entry = Entry(root, textvariable=destination_folder_var, state='readonly', font=("Helvetica", 12))
destination_folder_button = Button(root, text="Browse", command=select_destination_folder, font=("Helvetica", 12))

# Compress button
compress_button = Button(root, text="Compress Images", command=compress_images, font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white")

# Grid layout
title_label.grid(row=0, column=0, columnspan=4, pady=(0, 20))
instructions_label.grid(row=1, column=0, columnspan=4, pady=(0, 20))

source_folder_label.grid(row=2, column=0, sticky='e', padx=5, pady=5)
source_folder_entry.grid(row=2, column=1, columnspan=2, sticky='we', pady=5)
source_folder_button.grid(row=2, column=3, sticky='w', padx=5, pady=5)

single_image_label.grid(row=3, column=0, sticky='e', padx=5, pady=5)
single_image_entry.grid(row=3, column=1, columnspan=2, sticky='we', pady=5)
single_image_button.grid(row=3, column=3, sticky='w', padx=5, pady=5)

destination_folder_label.grid(row=4, column=0, sticky='e', padx=5, pady=5)
destination_folder_entry.grid(row=4, column=1, columnspan=2, sticky='we', pady=5)
destination_folder_button.grid(row=4, column=3, sticky='w', padx=5, pady=5)

compress_button.grid(row=5, column=0, columnspan=4, pady=10)

# Start the Tkinter main loop
root.mainloop()
