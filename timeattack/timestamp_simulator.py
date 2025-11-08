from datetime import datetime, timedelta, UTC 

sent_time = datetime.now(UTC)  

received_time = sent_time + timedelta(seconds=3.2)

delta = abs((received_time - sent_time).total_seconds())
print("✅ Timestamp valid — message accepted" if delta <= 5 else "🚨 Timestamp invalid — rejected")

