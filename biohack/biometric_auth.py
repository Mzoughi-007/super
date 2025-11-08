import hmac, hashlib

# Step 1: Store biometric hash (e.g., retina scan hash)
# In real systems, this would be securely stored and never hardcoded
stored_hash = hashlib.sha256(b"retina-scan-encoded").hexdigest()

def validate_biometric(input_data: str) -> bool:
    """
    Validate incoming biometric string against stored hash.
    """
    incoming_hash = hashlib.sha256(input_data.encode()).hexdigest()
    return hmac.compare_digest(incoming_hash, stored_hash)
