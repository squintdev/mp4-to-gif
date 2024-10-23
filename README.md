# MP4 to GIF Converter

A simple, cross-platform desktop application to convert MP4 videos to GIF format using a graphical user interface.

## Features

- Select input MP4 file and output folder using a file browser
- Customize output filename
- Adjust FPS (Frames Per Second) and output image height
- Cross-platform support (Windows, macOS, Linux)

## Requirements

- Python 3.6 or higher
- ffmpeg (must be installed separately)

## Installation

1. Clone this repository or download the source code.

2. Install the required Python version (3.6 or higher) if not already installed.

3. Install ffmpeg:
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add it to your system PATH.
   - **macOS**: Install using Homebrew: `brew install ffmpeg`
   - **Linux**: Install using your distribution's package manager, e.g., `sudo apt-get install ffmpeg` for Ubuntu/Debian.

4. (Optional) Create and activate a virtual environment:   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`   ```
```

## Usage

1. Run the application:   ```
   python main.py   ```

2. Use the "Browse" buttons to select your input MP4 file and output folder.

3. Enter a name for your output GIF file (without the .gif extension).

4. Adjust the FPS and Image Height as desired.

5. Click the "Convert" button to start the conversion process.

6. Wait for the conversion to complete. A success message will appear when finished.

## Notes

- The application uses ffmpeg for video conversion, so make sure it's properly installed and accessible from the command line.
- Higher FPS and Image Height values will result in larger file sizes and longer conversion times.
- The application will automatically append the .gif extension to the output filename if not provided.

## Troubleshooting

If you encounter any issues:

- Ensure ffmpeg is correctly installed and accessible from the command line.
- Check that you have write permissions in the selected output folder.
- Verify that the input MP4 file is not corrupted and is a valid video file.

For any other problems, please open an issue on the GitHub repository.

## License

[MIT License](LICENSE)
