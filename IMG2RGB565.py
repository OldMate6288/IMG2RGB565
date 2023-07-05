import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageSequence
import os
import webbrowser

def open_image():
    # Open file dialog to select an image file
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

    # Check if the selected file is a GIF
    if filepath.lower().endswith('.gif'):
        # Convert the animated GIF frames to RGB565 C arrays and save them as individual .C files
        convert_gif(filepath)
    else:
        # Convert the single image to RGB565 C array
        convert_image(filepath)

def convert_image(filepath):
    image = Image.open(filepath)

    # Convert the image to RGB mode if it's not already
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Convert image to RGB565 C array
    c_array = generate_c_array(image)

    # Save the C array to a file
    save_filepath = filedialog.asksaveasfilename(defaultextension=".c", filetypes=[("C files", "*.c")])
    if save_filepath:
        with open(save_filepath, 'w') as file:
            file.write(c_array)
        output_path_label.config(text=f"Output Path: {save_filepath}")
        print(f"C array saved to: {save_filepath}")

def convert_gif(filepath):
    # Create a folder to save the individual frames
    save_folder = filedialog.askdirectory(title="Select a folder to save the frames")
    if save_folder:
        gif = Image.open(filepath)

        # Iterate over each frame of the GIF
        for index, frame in enumerate(ImageSequence.Iterator(gif)):
            # Convert the frame to RGB mode if it's not already
            if frame.mode != 'RGB':
                frame = frame.convert('RGB')

            # Convert frame to RGB565 C array
            c_array = generate_c_array(frame)

            # Save the C array to a file
            frame_filename = f"frame_{index}.c"
            frame_filepath = os.path.join(save_folder, frame_filename)
            with open(frame_filepath, 'w') as file:
                file.write(c_array)
            output_path_label.config(text=f"Output Path: {frame_filepath}")
            print(f"Frame {index} saved to: {frame_filepath}")

def generate_c_array(image):
    # Convert image to RGB565 C array
    c_array = '// IMG2RGB565 - By OldMate6288 (github.com/OldMate6288)\n'
    c_array += 'const uint16_t image[] = {\n'
    for pixel in image.getdata():
        r, g, b = pixel
        rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
        c_array += f'0x{rgb565:04X}, '
    c_array += '};'
    return c_array

def open_url(event):
    webbrowser.open("https://github.com/OldMate6288")

# Create the main window
window = tk.Tk()
window.title("IMG2RGB565 v1.1")

# Set the size of the GUI window
window.geometry("400x350")  # Width x Height

# Load the logo image
logo_image = tk.PhotoImage(file="C:\img\logo2.png")

# Create a label for the logo image
logo_label = tk.Label(window, image=logo_image)
logo_label.pack(pady=10)

# Show file output path
output_path_label = tk.Label(window, text="Output Path:")
output_path_label.pack()

# Create a button to open an image
open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack(pady=10)

# Create a label for the hyperlink
hyperlink_label = tk.Label(window, text="Created By OldMate6288", fg="blue", cursor="hand2")
hyperlink_label.pack()

# Bind the label to the hyperlink function
hyperlink_label.bind("<Button-1>", open_url)

window.mainloop()
