import hashlib

def orbital_fingerprint(lat: float, lon: float, velocity: float) -> str:
    """
    Generate a SHA-256 fingerprint from orbital telemetry.
    """
    data = f"{lat:.6f}|{lon:.6f}|{velocity:.2f}"
    return hashlib.sha256(data.encode()).hexdigest()

def is_trusted(incoming_fingerprint: str, trusted_fingerprint: str) -> bool:
    return incoming_fingerprint == trusted_fingerprint
