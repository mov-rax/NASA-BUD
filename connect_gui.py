import PySimpleGUI as sg
from wifi_connect import WifiConnect

sg.theme("dark")


class ConnectGui:
    _wifi = WifiConnect()

    def run(self):
        self._wifi.scan()

        layout = [[sg.Text("Connect to a Pod", justification="center", size=(30, 1), key="TEXT1")],
                  [sg.Listbox(["Omega", "Beta", "Alpha"], size=(30, 6), no_scrollbar=True, font=("Noto Sans", 14),
                              enable_events=True, key="LISTBOX")],
                  [sg.Button("Scan for nearby Pods", key="SCAN")]]

        window = sg.Window("Pod Connection Utility", layout, font=("Noto Sans", 12), finalize=True)

        while True:
            event, values = window.read()
            print(event)
            if event == "LISTBOX":
                name = str(values['LISTBOX'][0])  # dictionary with the key 'LISTBOX' having the value of an array
                # with size 1.
                if self._wifi.connect(name):
                    window.close()
                    return True
                else:
                    print("ERROR. Could not connect to pod " + name)
                    sg.popup_error(title="Connection error. Could not connect to pod" + name)
                print("OK " + name)
            elif event == "SCAN":
                self._wifi.scan()
                window["LISTBOX"].Update(values=self._wifi.get_list())
            elif event == sg.WINDOW_CLOSED:
                window.close()
                return False

    def get_connected_name(self):
        return self._wifi.get_connected_name()

    def get_socket_info(self):
        return self._wifi.get_socket_info()
