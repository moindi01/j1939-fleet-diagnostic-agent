SPN_CODES = {
    100: "Engine Oil Pressure",
    110: "Engine Coolant Temperature",
    3226: "Aftertreatment DEF / SCR System",
}

FMI_SEVERITY = {
    0: "CRITICAL — Data valid but above normal operational range (STOP ENGINE)",
    1: "CRITICAL — Data valid but below normal operational range (STOP ENGINE)",
    3: "WARNING — Voltage above normal or shorted to high source (Check wiring)",
    4: "WARNING — Voltage below normal or shorted to low source (Check wiring)",
    18: "MODERATE — Data valid but moderately below normal range (Schedule service)",
}

spn = int(input("Enter SPN code (try 100, 110, or 3226): "))
fmi = int(input("Enter FMI code (try 0, 1, 3, or 18): "))

component = SPN_CODES.get(spn, "Unknown Component")
severity = FMI_SEVERITY.get(fmi, "Unknown Failure Mode — consult service manual")

print("\n--- DIAGNOSTIC REPORT ---")
print(f"Component : {component} (SPN {spn})")
print(f"Status    : {severity} (FMI {fmi})")