from biometric_auth import validate_biometric

# Simulated incoming biometric scan
user_input = "retina-scan-encoded"  # Try changing this to simulate failure

# Simulated command to life support system
command = "Activate oxygen recycling"

# Validate biometric before executing command
if validate_biometric(user_input):
    print(f"✅ Biometric verified — executing: {command}")
else:
    print("🚨 Access denied — biometric mismatch")
