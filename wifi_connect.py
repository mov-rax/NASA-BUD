import wifi as w


class WifiConnect:
    _wifi_list = None
    _current_connected_name = None
    _host_ip = None
    _host_port = 1001  # default port

    def __init__(self):
        print("Created wifi")

    # When fully implemented, this should be able to scan for wifi networks
    def scan(self):
        self._wifi_list = ["First", "Second", "Third"]

    def get_list(self):
        return self._wifi_list

    # When fully implemented, this should be able to connect to wifi networks
    def connect(self, pod_name: str):
        self._current_connected_name = pod_name
        self._host_ip = "127.0.0.1"  # this will change
        return True

    def get_connected_name(self):
        return self._current_connected_name

    def get_socket_info(self):
        return self._host_ip, self._host_port
