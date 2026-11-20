# Knowledge base mapping SPN + FMI to plain-English diagnosis and step-by-step repair checklists
REPAIR_MANUAL = {
    (100, 1): {
        "component": "Engine Oil Pressure",
        "severity": "CRITICAL — STOP ENGINE IMMEDIATELY",
        "checklist": [
            "1. Shut down engine immediately to prevent bearing seizure.",
            "2. Check engine oil dipstick level and inspect for external oil leaks.",
            "3. Inspect oil pressure sensor harness (check for oil intrusion or shorted pins).",
            "4. Verify mechanical oil pressure using a manual test gauge before restarting.",
        ],
    },
    (110, 0): {
        "component": "Engine Coolant Temperature",
        "severity": "CRITICAL — STOP ENGINE / REDUCE LOAD",
        "checklist": [
            "1. Allow engine to idle down safely; do not open radiator cap while hot.",
            "2. Inspect coolant expansion tank level and check for burst hoses.",
            "3. Verify viscous fan clutch engagement and radiator airflow (check for debris).",
            "4. Test thermostat opening temperature and coolant temperature sensor resistance.",
        ],
    },
    (3226, 18): {
        "component": "Aftertreatment DEF / SCR System",
        "severity": "MODERATE — ENGINE DERATE WARNING",
        "checklist": [
            "1. Verify Diesel Exhaust Fluid (DEF) tank level and fluid concentration (32.5% urea).",
            "2. Inspect DEF dosing injector for crystallization buildup.",
            "3. Check downstream NOx sensor wiring and run a parked DPF/SCR regeneration test.",
        ],
    },
}

def decode_dm1_hex(hex_payload: str):
    bytes_list = [int(b, 16) for b in hex_payload.strip().split()]
    spn = bytes_list[2] | (bytes_list[3] << 8) | ((bytes_list[4] & 0xE0) << 11)
    fmi = bytes_list[4] & 0x1F
    occurrence_count = bytes_list[5] & 0x7F
    return spn, fmi, occurrence_count

print("=== HEAVY-DUTY FLEET DIAGNOSTIC AGENT ===")
print("Sample frames you can test:")
print("  - Oil Pressure Critical : 04 FF 64 00 01 03 FF FF")
print("  - Coolant Temp Critical : 04 FF 6E 00 00 01 FF FF")
print("  - DEF/SCR Derate        : 04 FF 9A 0C 12 02 FF FF\n")

raw_frame = input("Paste raw J1939 DM1 hex frame (or press Enter for Oil Pressure sample): ").strip()
if not raw_frame:
    raw_frame = "04 FF 64 00 01 03 FF FF"

spn, fmi, count = decode_dm1_hex(raw_frame)
entry = REPAIR_MANUAL.get((spn, fmi))

print("\n-----------------------------------------")
print(f"RAW HEX FRAME : {raw_frame}")
print(f"DECODED CODE  : SPN {spn} | FMI {fmi} | Count: {count}")

if entry:
    print(f"COMPONENT     : {entry['component']}")
    print(f"SEVERITY      : {entry['severity']}")
    print("\nRECOMMENDED REPAIR CHECKLIST:")
    for step in entry["checklist"]:
        print(f"  {step}")
else:
    print("STATUS        : Code not yet in local manual — escalate to OEM diagnostics.")
print("-----------------------------------------")