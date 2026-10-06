# vivek-reddy
ic engine calculator
"""Menu-driven calculator for common IC engine performance quantities."""

import math


def calculate_brake_power(speed_rpm: float, torque_nm: float) -> float:
    """Return brake power in kW from engine speed (rpm) and torque (N·m)."""
    return (2 * math.pi * speed_rpm * torque_nm) / 60_000


def calculate_indicated_power(brake_power_kw: float, friction_power_kw: float) -> float:
    """Return indicated power in kW (IP = BP + FP)."""
    return brake_power_kw + friction_power_kw


def calculate_friction_power(indicated_power_kw: float, brake_power_kw: float) -> float:
    """Return friction power in kW (FP = IP - BP)."""
    return indicated_power_kw - brake_power_kw


def calculate_mechanical_efficiency(brake_power_kw: float, indicated_power_kw: float) -> float:
    """Return mechanical efficiency as a percentage."""
    if indicated_power_kw <= 0:
        raise ValueError("Indicated power must be greater than zero.")
    return (brake_power_kw / indicated_power_kw) * 100


def read_number(prompt: str, minimum: float | None = None) -> float:
    """Read a numeric value, repeating until it is valid."""
    while True:
        try:
            value = float(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Please enter a value of at least {minimum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_menu() -> None:
    print("\nIC ENGINE PERFORMANCE CALCULATOR")
    print("1. Calculate brake power")
    print("2. Calculate indicated power")
    print("3. Calculate friction power")
    print("4. Calculate mechanical efficiency")
    print("5. Exit")


def main() -> None:
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            speed = read_number("Engine speed (rpm): ", 0)
            torque = read_number("Brake torque (N·m): ", 0)
            print(f"Brake power = {calculate_brake_power(speed, torque):.3f} kW")
        elif choice == "2":
            bp = read_number("Brake power (kW): ", 0)
            fp = read_number("Friction power (kW): ", 0)
            print(f"Indicated power = {calculate_indicated_power(bp, fp):.3f} kW")
        elif choice == "3":
            ip = read_number("Indicated power (kW): ", 0)
            bp = read_number("Brake power (kW): ", 0)
            if bp > ip:
                print("Brake power cannot exceed indicated power.")
            else:
                print(f"Friction power = {calculate_friction_power(ip, bp):.3f} kW")
        elif choice == "4":
            bp = read_number("Brake power (kW): ", 0)
            ip = read_number("Indicated power (kW): ", 0)
            if bp > ip:
                print("Brake power cannot exceed indicated power.")
            else:
                print(f"Mechanical efficiency = {calculate_mechanical_efficiency(bp, ip):.2f}%")
        elif choice == "5":
            print("Thank you for using the calculator.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
