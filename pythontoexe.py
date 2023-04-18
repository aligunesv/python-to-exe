import os
import PyInstaller.__main__
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select Python File",
        filetypes=(("Python Files", "*.py"), ("All Files", "*.*"))
    )
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def select_output_dir():
    output_dir = filedialog.askdirectory(
        title="Select Output Directory",
        initialdir=str(Path.home() / "Desktop")
    )
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, output_dir)

def convert_to_exe():
    file_path = file_entry.get()
    output_dir = output_dir_entry.get()
    output_path = os.path.join(output_dir, "MyApp.exe")
    PyInstaller.__main__.run([
        '--name=MyApp', '--onefile',
        f'--distpath={output_dir}', f'--specpath={output_dir}',
        '--clean', file_path
    ])
    result_label.config(text="Conversion complete!\nOutput path: "+output_path)

# Create a Tkinter window
window = tk.Tk()
window.title("Python to EXE Converter")

# Create a file selection widget
file_label = tk.Label(window, text="Select a Python file:")
file_label.pack()
file_entry = tk.Entry(window)
file_entry.pack()
browse_file_button = tk.Button(window, text="Browse", command=select_file)
browse_file_button.pack()

# Create an output directory selection widget
output_dir_label = tk.Label(window, text="Select an output directory:")
output_dir_label.pack()
output_dir_entry = tk.Entry(window)
output_dir_entry.pack()
browse_output_dir_button = tk.Button(window, text="Browse", command=select_output_dir)
browse_output_dir_button.pack()

# Create a conversion button
convert_button = tk.Button(window, text="Convert to EXE", command=convert_to_exe)
convert_button.pack()

# Create a label for the conversion result
result_label = tk.Label(window, text="")
result_label.pack()

# Run the Tkinter event loop
window.mainloop()
