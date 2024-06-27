# image-compression

Import Statements:

Tkinter: Imports the Tkinter library for creating the GUI.
filedialog: Part of Tkinter for opening file and directory dialogs.
Label, Entry, Button, StringVar: Tkinter elements for labels, entry widgets, buttons, and string variables, respectively.
messagebox: For displaying message boxes.
PIL.Image: Part of the Python Imaging Library (PIL), used for working with images.
os: Provides a way to interact with the operating system, including file and folder operations.
Function Definitions:

select_folder(): Opens a dialog to select a source folder and updates the corresponding entry widget.
select_destination_folder(): Opens a dialog to select a destination folder and updates the corresponding entry widget.
select_single_image(): Opens a dialog to select a single image file and updates the corresponding entry widget.
compress_images(): Initiates the image compression process based on user input (single image or source folder).
compress_single_image(img_path, destination_folder): Resizes and compresses a single image and saves it to the destination folder.
Tkinter Setup:

Creates the main Tkinter window (root) and sets its title.
Defines string variables (StringVar) to store paths for source folder, destination folder, and single image.
Creates labels, entry widgets, and buttons for the user interface.
Configures the layout using the grid manager.
User Interface Components:

Title label and instructions label provide information to the user.
Entry widgets and buttons for selecting source folder, single image, and destination folder.
"Compress Images" button triggers the compression process.
Grid Layout:

Organizes the Tkinter widgets in a grid layout for a clean and structured interface.
Main Loop:

Starts the Tkinter main loop, allowing the user to interact with the GUI.
Additional Information:

The code uses the Python Imaging Library (PIL) to open, resize, and save images.
Error messages are displayed using Tkinter's messagebox if there are issues with user input.
In summary, the script provides a user-friendly interface for compressing images either individually or in bulk, with options to specify source and destination folders. The compression is achieved by resizing the images to a specified width while maintaining the aspect ratio.
