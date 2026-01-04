import socket
import pyautogui
import time

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

DEAD_ZONE_X = 1.0
DEAD_ZONE_Y = 0.5

GAIN_X = 2.2
GAIN_Y = 2.2          # VERY LOW

MAX_STEP_X = 30
MAX_STEP_Y = 30       # Y MUST be limited

ALPHA_Y = 0.55        # heavy smoothing

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

pyautogui.FAILSAFE = False
print("🖱 Practical air-mouse (X free, Y stabilized)")

last_time = time.time()
vx = 0.0
vy = 0.0
smooth_gy = 0.0

while True:
    data, _ = sock.recvfrom(1024)
    now = time.time()
    dt = now - last_time
    last_time = now

    row = data.decode().split(",")

    gx = float(row[4])   # pitch
    gy = float(row[5])   # yaw

    if abs(gy) < DEAD_ZONE_X:
        gy = 0.0
    if abs(gx) < DEAD_ZONE_Y:
        gx = 0.0

    # X axis (free rotation)
    vx += gy * GAIN_X * dt

    # Y axis (heavily stabilized)
    smooth_gy = ALPHA_Y * gx + (1 - ALPHA_Y) * smooth_gy
    vy += smooth_gy * GAIN_Y * dt

    move_x = int(vx)
    move_y = int(vy)

    move_x = max(-MAX_STEP_X, min(MAX_STEP_X, move_x))
    move_y = max(-MAX_STEP_Y, min(MAX_STEP_Y, move_y))

    if move_x != 0 or move_y != 0:
        pyautogui.moveRel(move_x, move_y)
        vx = 0
        vy = 0
