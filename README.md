# Work Recorder - README

## Overview
The **Work Recorder** is a simple application designed to help users record time spent on different activities. Users can select a category and type, start and stop a timer, and log the recorded time. The data is saved in a CSV file named `time_record.csv`, which is generated in the same directory as the executable.

## How It Works
1. Launch the application by running the executable in the `dist` directory.
2. Select a **Category**:
   - Story Work
   - Story Preparation
   - No Story Work
3. Select a **Type**:
   - Meeting
   - Productive
4. Click the **Start Timer** button to begin recording time.
5. Click the **Stop Timer** button to stop the timer and save the recorded time.
6. The logged data will be saved to `time_record.csv`.

### File Output
- The file `time_record.csv` will contain the following columns:
  - Category
  - Type
  - Recorded Time (h:m:s)
  - Date and Time of the recording
  - Weekday of the recording

## Executable Location
The prebuilt executable can be found in the `dist` directory. Double-click the `.exe` file to launch the application.

## Building the Executable for Windows
To build the `.exe` file from the source code, follow these steps:

1. **Set Up a Python Virtual Environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # For Windows
   ```

2. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

3. **Build the Executable**:
   Run the following command in the terminal:
   ```bash
   pyinstaller --onefile --windowed --icon=custom_icon.ico --add-data "custom_icon.png;." workRecorder.py
   ```
   Explanation of the flags:
   - `--onefile`: Bundles everything into a single `.exe` file.
   - `--windowed`: Hides the terminal window when running the application.
   - `--icon=custom_icon.ico`: Sets a custom icon for the executable.
   - `--add-data "custom_icon.png;."`: Includes the `custom_icon.png` file with the executable.

4. **Locate the Executable**:
   After the build process, the `.exe` file will be located in the `dist` folder.

## Building for Other Operating Systems
If you want to build this software for a different operating system, you can use PyInstaller on that platform. The process is the same, but you may need to adjust file paths and flags based on the operating system. For example:
- Use `:` instead of `;` in the `--add-data` flag on Linux/Mac.

Example for Linux/Mac:
```bash
pyinstaller --onefile --windowed --icon=custom_icon.ico --add-data "custom_icon.png:." workRecorder.py
```

## Troubleshooting
- **Missing Files**: If the application throws a `FileNotFoundError`, ensure that the required files (e.g., `custom_icon.png`) are included using the `--add-data` flag.
- **Dependencies**: Ensure all Python libraries are installed in your virtual environment before building the `.exe` file.

## Contact
If you encounter any issues or have questions, feel free to contact the developer or refer to the documentation provided with the application.

