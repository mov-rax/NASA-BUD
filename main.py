from connect_gui import ConnectGui
from gui import MainGui
from server_lib import Server
from threading import Thread


c_gui = ConnectGui()
stopper = [False]
status_data = [0, 0, 0]  # [pitch, roll, temp]
command_data = [None]

while True:
    if c_gui.run():
        ip, port = c_gui.get_socket_info()
        server = Server(ip, port)
        thread = Thread(target=server.connect, args=[stopper, status_data])
        thread.start()
        m_gui = MainGui(c_gui.get_connected_name(), ip, port)
        m_gui.run()  # Shows the GUI (thread-blocking)
        stopper = [True]  # disconnects from the server
        print("Something happened I think!")
    else:
        print("Window closed!")
        break
    stopper = [False]

