# Virtual Mouse with Arduino Nicla Vision

## Problem Statement

Traditional computer input devices like mice require physical interaction, which can be limiting in certain scenarios such as presentations, accessibility needs, or hands-free operation. There is a need for a wireless, gesture-based mouse control system that allows users to control the cursor through natural hand movements.

## Goal of the Project

The goal of this project is to develop a wireless virtual mouse system using the Arduino Nicla Vision board's IMU sensor to capture hand gestures and translate them into mouse cursor movements on a computer via WiFi and UDP communication. The system aims to provide stable, responsive cursor control with configurable parameters for optimal user experience.

## Dataset Description

This project does not use a pre-collected dataset. Instead, it processes real-time sensor data from the LSM6DSOX IMU sensor onboard the Arduino Nicla Vision board. The data includes accelerometer readings (Ax, Ay, Az) and gyroscope readings (Gx, Gy, Gz) sampled at approximately 50Hz (every 20ms). The gyroscope data (pitch and yaw) is primarily used for mouse movement control.

## Model Pipeline and Workflow

1. **Data Collection**: The Nicla Vision board collects IMU data from the LSM6DSOX sensor.
2. **Data Transmission**: IMU data is formatted and sent via UDP packets to the host computer.
3. **Data Reception**: The laptop receiver script listens for UDP packets on port 5005.
4. **Data Processing**:
   - Parse gyroscope values (Gx for yaw, Gy for pitch).
   - Apply dead zones to filter out minor movements.
   - Apply gain multipliers for sensitivity adjustment.
   - Implement smoothing (especially for Y-axis) using exponential moving average.
   - Integrate velocity over time for position calculation.
5. **Mouse Control**: Use PyAutoGUI to move the mouse cursor relative to the calculated positions.
6. **Feedback**: Visual indicators via LEDs on the Nicla Vision board for connection status.

## Deployment Details

The system is deployed on two components:
- **Hardware**: Arduino Nicla Vision board with IMU sensor.
- **Software**: MicroPython firmware on the board and Python script on the host computer.
- **Network**: WiFi connection for data transmission, UDP protocol for low-latency communication.
- **Dependencies**: PyAutoGUI library for mouse control, NumPy for potential future enhancements.

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

## Team Member Names

Ashank Gupta,Vatsal,Gurleen Kaur,Sakshi Jadhav,Tanvi Thakre

## License

This project is licensed under the MIT License. See the license header in `main.py` for details.

## Contributing

Feel free to submit issues and enhancement requests.
