# MP4 to GIF Converter

This application provides a simple graphical user interface for converting MP4 videos to GIF format using ffmpeg.

## Prerequisites

Before running this application, ensure you have the following installed:

1. Python 3.6 or higher
2. ffmpeg (must be installed separately and available in your system PATH)

## Installation

1. Clone this repository or download the source code.

2. Navigate to the project directory in your terminal or command prompt.

3. Install the required Python packages by running:

   ```
   pip install -r requirements.txt
   ```

   This will install all necessary Python dependencies.

## Usage

1. After installing the dependencies, run the script with:

   ```
   python main.py
   ```

2. Use the GUI to:
   - Select an input MP4 file
   - Choose an output folder
   - Set the output filename
   - Adjust FPS and image height as needed
   - Click "Convert" to create your GIF

3. The application supports both light and dark themes. Use the "Dark Mode" toggle to switch between themes.

## Troubleshooting

- If you encounter any errors related to ffmpeg, ensure it's properly installed and added to your system PATH.
- For any Python-related errors, make sure you've installed all dependencies using the `requirements.txt` file.

## License

MIT License

## Contributing

Feel free to fork the repository and submit pull requests with improvements or new features.
