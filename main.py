import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import subprocess
import os
import platform
from PIL import Image, ImageTk

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

def toggle_theme():
    if root.style.theme.name == "darkly":
        root.style.theme_use("litera")
    else:
        root.style.theme_use("darkly")

# Create the main window
root = ttkb.Window(themename="darkly")
root.title("MP4 to GIF Converter")
root.geometry("600x400")

# Create a style
style = ttkb.Style()

# Create main frame
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill=BOTH, expand=YES)

# Input file selection
input_frame = ttk.Frame(main_frame)
input_frame.pack(fill=X, pady=5)
ttk.Label(input_frame, text="Input MP4 file:").pack(side=LEFT)
input_entry = ttk.Entry(input_frame, width=50)
input_entry.pack(side=LEFT, expand=YES, fill=X, padx=5)
ttk.Button(input_frame, text="Browse", command=select_input_file).pack(side=LEFT)

# Output folder selection
output_frame = ttk.Frame(main_frame)
output_frame.pack(fill=X, pady=5)
ttk.Label(output_frame, text="Output folder:").pack(side=LEFT)
output_folder_entry = ttk.Entry(output_frame, width=50)
output_folder_entry.pack(side=LEFT, expand=YES, fill=X, padx=5)
ttk.Button(output_frame, text="Browse", command=select_output_folder).pack(side=LEFT)

# Output filename input
filename_frame = ttk.Frame(main_frame)
filename_frame.pack(fill=X, pady=5)
ttk.Label(filename_frame, text="Output filename:").pack(side=LEFT)
output_filename_entry = ttk.Entry(filename_frame, width=50)
output_filename_entry.pack(side=LEFT, expand=YES, fill=X, padx=5)
ttk.Label(filename_frame, text=".gif").pack(side=LEFT)

# FPS and Image Height inputs
settings_frame = ttk.Frame(main_frame)
settings_frame.pack(fill=X, pady=5)
ttk.Label(settings_frame, text="FPS:").pack(side=LEFT)
fps_entry = ttk.Entry(settings_frame, width=10)
fps_entry.pack(side=LEFT, padx=(0, 20))
fps_entry.insert(0, "10")
ttk.Label(settings_frame, text="Image Height:").pack(side=LEFT)
image_height_entry = ttk.Entry(settings_frame, width=10)
image_height_entry.pack(side=LEFT)
image_height_entry.insert(0, "225")

# Progress bar
progress_bar = ttk.Progressbar(main_frame, length=400, mode='indeterminate')
progress_bar.pack(pady=10)

# Convert button
convert_button = ttk.Button(main_frame, text="Convert", command=convert_video, style="Accent.TButton")
convert_button.pack(pady=10)

# Theme toggle button
theme_button = ttk.Checkbutton(main_frame, text="Dark Mode", style="Switch.TCheckbutton", command=toggle_theme)
theme_button.pack(pady=10)

root.mainloop()
