import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import platform

def select_input_file():
    if platform.system() == "Windows":
        file_path = subprocess.check_output(['powershell', '-command', 'Add-Type -AssemblyName System.Windows.Forms; $f = New-Object System.Windows.Forms.OpenFileDialog; $f.Filter = "MP4 files (*.mp4)|*.mp4"; $f.ShowDialog(); $f.FileName']).decode('utf-8').strip()
    elif platform.system() == "Darwin":  # macOS
        file_path = subprocess.check_output(['osascript', '-e', 'tell application "System Events" to POSIX path of (choose file with prompt "Select MP4 file" of type {"mp4"})']).decode('utf-8').strip()
    else:  # Linux and other Unix-like systems
        file_path = subprocess.check_output(['zenity', '--file-selection', '--file-filter=MP4 files | *.mp4']).decode('utf-8').strip()
    
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def select_output_folder():
    if platform.system() == "Windows":
        folder_path = subprocess.check_output(['powershell', '-command', 'Add-Type -AssemblyName System.Windows.Forms; $f = New-Object System.Windows.Forms.FolderBrowserDialog; $f.ShowDialog(); $f.SelectedPath']).decode('utf-8').strip()
    elif platform.system() == "Darwin":  # macOS
        folder_path = subprocess.check_output(['osascript', '-e', 'tell application "System Events" to POSIX path of (choose folder with prompt "Select output folder")']).decode('utf-8').strip()
    else:  # Linux and other Unix-like systems
        folder_path = subprocess.check_output(['zenity', '--file-selection', '--directory']).decode('utf-8').strip()
    
    if folder_path:
        output_folder_entry.delete(0, tk.END)
        output_folder_entry.insert(0, folder_path)

def convert_video():
    input_file = input_entry.get()
    output_folder = output_folder_entry.get()
    output_filename = output_filename_entry.get()
    fps = fps_entry.get()
    image_height = image_height_entry.get()

    if not input_file or not output_folder or not output_filename or not fps or not image_height:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    try:
        fps = int(fps)
        image_height = int(image_height)
    except ValueError:
        messagebox.showerror("Error", "FPS and Image Height must be integers")
        return

    output_path = os.path.join(output_folder, output_filename)
    if not output_path.lower().endswith('.gif'):
        output_path += '.gif'

    ffmpeg_command = [
        'ffmpeg',
        '-i', input_file,
        '-filter_complex', f'fps={fps},scale=-1:{image_height}',
        '-loop', '0',
        output_path
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
        messagebox.showinfo("Success", f"Conversion complete!\nOutput saved to: {output_path}")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Conversion failed. Please make sure ffmpeg is installed and the input file is valid.")

# Create the main window
root = tk.Tk()
root.title("MP4 to GIF Converter")

# Input file selection
tk.Label(root, text="Input MP4 file:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=2, padx=5, pady=5)

# Output folder selection
tk.Label(root, text="Output folder:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_output_folder).grid(row=1, column=2, padx=5, pady=5)

# Output filename input
tk.Label(root, text="Output filename:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
output_filename_entry = tk.Entry(root, width=50)
output_filename_entry.grid(row=2, column=1, padx=5, pady=5)
tk.Label(root, text=".gif").grid(row=2, column=2, sticky="w")

# FPS input
tk.Label(root, text="FPS:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
fps_entry = tk.Entry(root, width=10)
fps_entry.grid(row=3, column=1, sticky="w", padx=5, pady=5)
fps_entry.insert(0, "10")  # Default value

# Image Height input
tk.Label(root, text="Image Height:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
image_height_entry = tk.Entry(root, width=10)
image_height_entry.grid(row=4, column=1, sticky="w", padx=5, pady=5)
image_height_entry.insert(0, "225")  # Default value

# Convert button
tk.Button(root, text="Convert", command=convert_video).grid(row=5, column=1, pady=10)

root.mainloop()
