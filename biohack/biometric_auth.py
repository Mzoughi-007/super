import hmac, hashlib

stored_hash = hashlib.sha256(b"retina-scan-encoded").hexdigest()

def validate_biometric(input_data: str) -> bool:
    """
    Validate incoming biometric string against stored hash.
    """
    incoming_hash = hashlib.sha256(input_data.encode()).hexdigest()
    return hmac.compare_digest(incoming_hash, stored_hash)
