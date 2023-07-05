import tkinter as tk
from tkinter import filedialog
from PIL import Image
import webbrowser

def open_image():
    # Open file dialog to select an image file
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    
    # Load the image
    image = Image.open(filepath)
    
    # Convert the image to RGB mode if it's not already
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Convert image to RGB565 C array
    c_array = '// IMG2RGB565 - By OldMate6288 (github.com/OldMate6288)\n'
    c_array += 'const uint16_t image[] = {\n'
    for pixel in image.getdata():
        r, g, b = pixel
        rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
        c_array += f'0x{rgb565:04X}, '
    c_array += '};'
    
    # Save the C array to file
    save_filepath = filedialog.asksaveasfilename(defaultextension=".c", filetypes=[("C files", "*.c")])
    if save_filepath:
        with open(save_filepath, 'w') as file:
            file.write(c_array)
        print(f"C array saved to: {save_filepath}")
    
    # Display the C array in a text box (SUPER SLOW)
    # text_box.delete(1.0, tk.END)
    # text_box.insert(tk.END, c_array)
    
def open_url(event):
    webbrowser.open("https://github.com/OldMate6288")

# Create the main window
window = tk.Tk()
window.title("IMG2RGB565")

# Set the size of the GUI window
window.geometry("150x290") 

# Load the logo image
logo_image = tk.PhotoImage(file="C:\img\logo2.png")

# Create a label for the logo image
logo_label = tk.Label(window, image=logo_image)
logo_label.pack(pady=10)

# Create a button to open an image
open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack(pady=10)

# Create a label for the hyperlink
hyperlink_label = tk.Label(window, text="Created By OldMate6288", fg="blue", cursor="hand2")
hyperlink_label.pack()

# Bind the label to the hyperlink function
hyperlink_label.bind("<Button-1>", open_url)

# Create a text box to display the C array
# text_box = tk.Text(window, width=40, height=10)
# text_box.pack()

window.mainloop()
