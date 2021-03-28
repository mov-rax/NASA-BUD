from gui_lib import *


class MainGui:
    _name: str
    _battery_percentage = 100
    _data = [62, 12, 12]  # [pitch, roll, temp]
    _host: str
    _port: int

    def __init__(self, pod_name: str, ip: str, port: int):
        self._name = pod_name
        self._host = ip
        self._port = port

    def run(self):
        layout = [[sg.Text('welcome to the menu', pad=(5, 5), size=(10, 1), justification="center")],
                  [get_temperature_label(self._data[2])],
                  [get_roll_label(self._data[1])],
                  [get_pitch_label(self._data[0])],
                  [sg.Button('disconnect'), sg.Button('open/close the bud'), sg.Button('increment temp')],
                  [sg.InputText()]
                  ]

        layout2 = [[sg.Text("HELLO THERE")]]

        window = sg.Window('BUD [' + self._name.upper() + '] CONTROL PANEL', layout, resizable=True,
                           font=("Noto Sans", 12), location=(250, 250))

        while True:
            event, values = window.read()
            if event == 'increment temp':
                self._data[2] += 1
                window["TEMP"].Update(value=get_temperature_str(self._data[2]))
                print(self._data[2])
            elif event == sg.WIN_CLOSED or event == 'disconnect':
                break
            print('you entered' + str(values[0]))
        window.close()
