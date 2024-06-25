from modules.impedances import (z_lines,z_sht)
from modules.ybus import functionYbus as fbus

def main():
    y_bus = fbus(z_lines,z_sht)

if __name__ == "__main__":
    main()
