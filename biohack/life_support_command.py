from biometric_auth import validate_biometric

user_input = "retina-scan-encoded"  # Try changing this to simulate failure

command = "Activate oxygen recycling"

if validate_biometric(user_input):
    print(f"✅ Biometric verified — executing: {command}")
else:
    print("🚨 Access denied — biometric mismatch")
