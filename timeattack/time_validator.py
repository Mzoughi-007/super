from datetime import datetime

def validate_timestamp(sent: datetime, received: datetime, window_seconds=5) -> bool:
    """
    Check if received timestamp is within ±window_seconds of sent timestamp.
    """
    delta = abs((received - sent).total_seconds())
    return delta <= window_seconds
