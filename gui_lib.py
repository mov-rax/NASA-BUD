import PySimpleGUI as sg


def get_temperature_str(temp):
    return "temperature " + str(temp) + ' °C'


def get_temperature_label(temp):
    return sg.Text(get_temperature_str(temp), key="TEMP")


def get_battery_percentage_str(percentage):
    return "%" + str(percentage)


def get_battery_percentage_label(percentage):
    return sg.Text(get_battery_percentage_str(percentage), size=(10, 1), text_color='green', justification='right',
                   key="BATTERY")


def get_pitch_str(pitch):
    return "pitch: " + str(pitch)


def get_pitch_label(pitch):
    return sg.Text(get_pitch_str(pitch), key="PITCH")


def get_roll_str(yaw):
    return "roll: " + str(yaw)


def get_roll_label(yaw):
    return sg.Text(get_roll_str(yaw), key="ROLL")
