# Virtual Mouse with Arduino Nicla Vision

A wireless virtual mouse system that uses the Arduino Nicla Vision's IMU sensor to control a computer's mouse cursor via WiFi and UDP communication.

## Description

This project consists of two components:
- **Nicla Vision firmware** (`main.py`): Collects accelerometer and gyroscope data from the onboard LSM6DSOX IMU and transmits it wirelessly to a host computer.
- **Laptop receiver** (`receive_data.py`): Receives IMU data via UDP, processes gyroscope readings to simulate mouse movement using PyAutoGUI.

The system implements dead zones, gain control, and smoothing to provide stable cursor control through hand gestures.

## Hardware Requirements

- Arduino Nicla Vision board
- WiFi network access
- Computer (laptop/desktop) with Python support

## Software Requirements

### Nicla Vision
- OpenMV firmware (compatible with MicroPython)
- LSM6DSOX IMU library

### Laptop
- Python 3.6+
- PyAutoGUI library: `pip install pyautogui`
- NumPy (automatically installed with PyAutoGUI)

## Setup

### 1. Nicla Vision Configuration

1. Flash the OpenMV firmware onto your Nicla Vision board if not already done.
2. Update the WiFi credentials in `main.py`:
   ```python
   SSID = "your_wifi_ssid"
   KEY = "your_wifi_password"
   ```
3. Set the laptop's IP address in `main.py`:
   ```python
   PC_IP = "your_laptop_ip_address"
   ```
4. Upload `main.py` to the Nicla Vision using OpenMV IDE or similar tool.

### 2. Laptop Configuration

1. **Create and activate a virtual environment** (recommended to avoid package conflicts):
   
   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install required Python packages:
   ```bash
   pip install pyautogui
   ```

3. Ensure your firewall allows UDP traffic on port 5005.

4. Optionally adjust control parameters in `receive_data.py`:
   - `DEAD_ZONE_X` and `DEAD_ZONE_Y`: Minimum gyro values to register movement
   - `GAIN_X` and `GAIN_Y`: Sensitivity multipliers
   - `MAX_STEP_X` and `MAX_STEP_Y`: Maximum pixels to move per frame
   - `ALPHA_Y`: Smoothing factor for Y-axis (0-1, higher = more smoothing)

## Usage

1. Power on the Nicla Vision board. It will connect to WiFi and start transmitting IMU data.

2. On your laptop, run the receiver script:
   ```bash
   python receive_data.py
   ```

3. Move the Nicla Vision board to control the mouse cursor:
   - Pitch (X-axis rotation) controls horizontal mouse movement
   - Yaw (Y-axis rotation) controls vertical mouse movement (with heavy smoothing)

4. The system provides visual feedback via the Nicla Vision's LEDs:
   - Red LED: WiFi connection failed
   - Green LED: WiFi connected and transmitting

## Troubleshooting

- **No mouse movement**: Check WiFi connection, IP addresses, and firewall settings
- **Erratic movement**: Adjust dead zones and gain values in `receive_data.py`
- **Connection issues**: Verify SSID, password, and PC_IP are correct
- **Performance**: The system samples at ~50Hz (20ms intervals)

## License

This project is licensed under the MIT License. See the license header in `main.py` for details.

## Contributing

Feel free to submit issues and enhancement requests.