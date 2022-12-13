from configparser import ConfigParser

config = ConfigParser()
config.read("config_example.ini")

print(config.sections())
lst = [item for item in config.values()]
print(lst)

lst = [item for item in config.items()]
print(lst)


string_val = config.get("System config", "last")
print(string_val)

bool_val = config.getboolean("System config", "bbb")
print(type(bool_val))
print(bool_val)


int_val = config.getint("System config", "age")
print(int_val)


int_val = config.getfloat("System config", "age")
print(int_val)


arr = config.get("System config", "lst").split(",")
print(arr)
