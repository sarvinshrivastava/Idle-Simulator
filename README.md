# AFK

This project simulates keyboard and mouse activity to prevent inactivity detection. It uses the `pynput` library to monitor real user activity and simulate keystrokes and mouse movements when inactivity is detected.

## Features

- Monitors keyboard and mouse activity.
- Simulates keystrokes and mouse movements after a period of inactivity.
- Logs all activities to a file.

## Requirements

- Python 3.x
- `pynput` library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/afk-simulation.git
   cd afk-simulation
   ```

2. Install the required packages:
   ```sh
   pip install pynput
   ```

## Usage

1. Run the script:
   ```sh
   python afk.py
   ```

2. The script will start monitoring keyboard and mouse activity. If no activity is detected for 30 seconds, it will start simulating keystrokes and mouse movements.

## Converting to an Executable

You can convert the script to an executable file using `PyInstaller`:

1. Install `PyInstaller`:
   ```sh
   pip install pyinstaller
   ```

2. Create the executable:
   ```sh
   pyinstaller --onefile --windowed afk.py
   ```

## Logging

All activities are logged to a file in the `logs` directory. Each run creates a new log file with a timestamp in the filename.

## License

This project is licensed under the MIT License.
```

This `README.md` file provides an overview of the project, installation instructions, usage details, and information on converting the script to an executable.