def read_line(file):
    return file.readline().strip().split('=')[1]

def read_settings():
    Settings = {}
    with open("settings.txt", 'r') as file:
        Settings["seed"] = int(read_line(file))
        Settings["font_size"] = int(read_line(file))
        Settings["node_scaling"] = int(read_line(file))
    return Settings


