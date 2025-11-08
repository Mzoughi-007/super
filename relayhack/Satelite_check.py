from orbital_auth import orbital_fingerprint, is_trusted

# Step 1: Define trusted satellite telemetry
trusted_lat = 12.345678
trusted_lon = 98.765432
trusted_velocity = 7.8

# Step 2: Generate trusted fingerprint
trusted_fp = orbital_fingerprint(trusted_lat, trusted_lon, trusted_velocity)

# Step 3: Simulate incoming satellite claim
incoming_lat = 12.345678
incoming_lon = 98.765432
incoming_velocity = 7.8  # Try changing this to 7.9 to simulate spoofing

incoming_fp = orbital_fingerprint(incoming_lat, incoming_lon, incoming_velocity)

# Step 4: Validate
if is_trusted(incoming_fp, trusted_fp):
    print("✅ Satellite identity verified: Trusted")
else:
    print("🚨 Satellite identity mismatch: Spoofed")
