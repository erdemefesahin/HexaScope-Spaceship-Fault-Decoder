def analyze_hex_message(hex_code):
    """
    Analyzes a spaceship status report encoded as a hexadecimal value.
    The encoding structure:
    - Last 2 bits: Severity level (0 = Normal, 1 = Warning, 2 = Critical, 3 = Severe)
    - Middle 3 bits: Affected component (0 = None, 1-5 = Components)
    - First 3 bits: Fault type (0 = No issue, 1-6 = Faults)
    """


    try:
        binary_rep = format(int(hex_code, 16), '08b')
    except ValueError:
        print("Invalid input: Please provide a valid hexadecimal value.")
        return

    severity_lvl = int(binary_rep[-2:], 2)
    component_id = int(binary_rep[-5:-2], 2)
    fault_id = int(binary_rep[:-5], 2)

    severity_dict = {
        0: "Operational",
        1: "Warning",
        2: "Critical",
        3: "Severe Malfunction"
    }

    component_dict = {
        0: "None",
        1: "Power system",
        2: "Signal transmitter",
        3: "Signal receiver",
        4: "Optical unit",
        5: "Propulsion module"
    }

    fault_dict = {
        0: "No issue",
        1: "Excessive heat",
        2: "No response",
        3: "Signal disruption",
        4: "High power usage",
        5: "Unknown fault",
        6: "Electrical issue"
    }

    if severity_lvl not in severity_dict or component_id not in component_dict or fault_id not in fault_dict:
        print("Error: The provided data does not match the expected encoding format.")
        return

    print("\n=== Spaceship Diagnostic Report ===")
    print(f"Hexadecimal Input: {hex_code.upper()}")
    print(f"Binary Equivalent: {binary_rep}")
    print(f"Severity Level: {severity_dict[severity_lvl]}")
    print(f"Affected Component: {component_dict[component_id]}")
    print(f"Fault Description: {fault_dict[fault_id]}")
    print("===================================\n")


analyze_hex_message("00")
