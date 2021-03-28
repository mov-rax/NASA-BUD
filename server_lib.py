from dataclasses import dataclass
import socket
import struct
from time import sleep


@dataclass
class ServerDataTypes:
    accel: str = "a"
    gyro: str = "g"
    command_extend: str = "e"
    command_close: str = "c"
    command_track: str = "t"
    rotate_left: str = "l"
    rotate_right: str = "r"
    tilt_up: str = "p"
    tilt_down: str = "n"


class Server:
    ip: str
    port: int
    is_extended = False
    is_tracking = False

    def __init__(self, ip: str, port: int = 4201):
        self.ip = ip
        self.port = port

    def connect(self, stopper, status_data, command_data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((self.ip, self.port))
                while not stopper:
                    s.sendall(b'u')  # u = update
                    data = struct.unpack("<hhh", s.recv(6))  # unpack 3 16-bit signed integers
                    status_data[0] = data[0]
                    status_data[1] = data[1]
                    status_data[2] = data[2]
                    if command_data[0] is not None:
                        if command_data[0] == ServerDataTypes.command_extend:
                            print("Extending")
                        elif command_data[0] == ServerDataTypes.command_close:
                            print("Closing")
                        elif command_data[0] == ServerDataTypes.command_track:
                            print("Sun-tracking enabled")
                        elif command_data[0] == ServerDataTypes.rotate_left:
                            print("Rotating Left")
                        elif command_data[0] == ServerDataTypes.rotate_right:
                            print("Rotating Right")
                        elif command_data[0] == ServerDataTypes.tilt_up:
                            print("Tilting Up")
                        elif command_data[0] == ServerDataTypes.tilt_down:
                            print("Tilting Down")
                        else:
                            print("Unknown server command.")
                        s.sendall(bytes(command_data[0]))

            except InterruptedError:
                print(f"ERROR. Could not connect to {self.ip}:{self.port}")
                return

    def host(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.ip, self.port))
            s.listen()
            print(f"Waiting for a connection to {self.ip}:{self.port}")
            conn, addr = s.accept()
            with conn:
                print(f"Connection from {self.port}")
                while True:
                    data = str(conn.recv(1))
                    if data == "u":
                        conn.sendall(struct.pack("<hhh", 69, 420, 190))  # will change
                    elif data == ServerDataTypes.command_extend:
                        print("Extending")
                    elif data == ServerDataTypes.command_close:
                        print("Closing")
                    elif data == ServerDataTypes.command_track:
                        print("Sun-tracking")
                    elif data == ServerDataTypes.rotate_left:
                        print("Rotating Left")
                    elif data == ServerDataTypes.rotate_right:
                        print("Rotating Right")
                    elif data == ServerDataTypes.tilt_up:
                        print("Tilting Up")
                    elif data == ServerDataTypes.tilt_down:
                        print("Tilting Down")
                    else:
                        print("Unknown Command")
