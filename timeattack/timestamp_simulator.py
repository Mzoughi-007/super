from datetime import datetime, timedelta, UTC  # ✅ Add UTC

# Step 1: Simulate message timestamp
sent_time = datetime.now(UTC)  # ✅ Use timezone-aware UTC

# Step 2: Simulate drifted reception
received_time = sent_time + timedelta(seconds=3.2)

# Step 3: Validate within ±5s window
delta = abs((received_time - sent_time).total_seconds())
print("✅ Timestamp valid — message accepted" if delta <= 5 else "🚨 Timestamp invalid — rejected")
