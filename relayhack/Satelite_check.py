from orbital_auth import orbital_fingerprint, is_trusted

trusted_lat = 12.345678
trusted_lon = 98.765432
trusted_velocity = 7.8

trusted_fp = orbital_fingerprint(trusted_lat, trusted_lon, trusted_velocity)

incoming_lat = 12.345678
incoming_lon = 98.765432
incoming_velocity = 7.8  

incoming_fp = orbital_fingerprint(incoming_lat, incoming_lon, incoming_velocity)

if is_trusted(incoming_fp, trusted_fp):
    print("✅ Satellite identity verified: Trusted")
else:
    print("🚨 Satellite identity mismatch: Spoofed")

