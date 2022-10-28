from webbrowser import get
from si_prefix import si_format


class OhmsLaw:
    def __init__(self, voltage=None, current=None, resistance=None):
        self.voltage = voltage
        self.current = current
        self.resistance = resistance
        self.result = None

        if not self.current and self.voltage and self.resistance:
            self.result = self.voltage / self.resistance

        if not self.voltage and self.current and self.resistance:
            self.result = self.current * self.resistance

        if not self.resistance and self.voltage and self.current:
            self.result = self.voltage / self.current

    def __call__(self, *args, **kwds):
        return self.result


def is_float(element) -> bool:
    try:
        float(element)
        return True
    except BaseException as be:
        return False


def get_desired_measurement():
    options = ("V", "I", "R")
    desired_measurement = None
    while not desired_measurement in options:
        desired_measurement = input(
            "Please enter desired measurement [V/I/R]: "
        ).upper()
    return desired_measurement


def get_input(type, units):
    res = None
    counter = 0
    while not is_float(res):
        err = f"" if counter == 0 else f"Not valid numeric input, "
        res = input(f"{err}Please enter {type} [{units}]: ")
        counter += 1
    return float(res)


is_finished = False

while not is_finished:

    mtype = get_desired_measurement()

    if mtype == "V":  # r i
        i = get_input("Current", "I")
        r = get_input("Resistance", "R")

        ohm = OhmsLaw(
            current=i,
            resistance=r,
        )
        print(f"Voltage [V] is: {si_format(ohm(), precision=5)}")

    if mtype == "R":  # r i
        v = get_input("Voltage", "V")
        i = get_input("Current", "I")

        ohm = OhmsLaw(
            current=i,
            voltage=v,
        )
        print(f"Resistance [Ohm] is: {si_format(ohm(), precision=5)}")

    if mtype == "I":  # r i
        v = get_input("Voltage", "V")
        r = get_input("Resistance", "R")

        ohm = OhmsLaw(
            voltage=v,
            resistance=r,
        )
        print(f"Current [A] is: {si_format(ohm(), precision=5)}")

    retry = input("\nAnother calculation?").upper()
    if retry == "N":
        is_finished = True
