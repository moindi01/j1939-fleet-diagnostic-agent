def decode_dm1_hex(hex_payload: str):
    # Convert a string like "04 FF 64 00 01 03 FF FF" into 8 integer bytes
    bytes_list = [int(b, 16) for b in hex_payload.strip().split()]

    # SAE J1939 DM1 bit-unpacking for the first active fault (Bytes 3, 4, 5)
    spn = bytes_list[2] | (bytes_list[3] << 8) | ((bytes_list[4] & 0xE0) << 11)
    fmi = bytes_list[4] & 0x1F
    occurrence_count = bytes_list[5] & 0x7F

    return spn, fmi, occurrence_count

raw_frame = input("Paste an 8-byte J1939 DM1 hex frame (or press Enter for sample): ").strip()
if not raw_frame:
    raw_frame = "04 FF 64 00 01 03 FF FF"  # Sample: SPN 100 (Oil Pressure), FMI 1, Occurred 3 times

spn, fmi, count = decode_dm1_hex(raw_frame)
print(f"\nDecoded Raw Frame : {raw_frame}")
print(f"SPN (Component)   : {spn}")
print(f"FMI (Failure Mode): {fmi}")
print(f"Occurrence Count  : {count} time(s)")