import pytz
import datetime
from datetime import timezone

print(datetime.datetime.now(timezone.utc) + datetime.timedelta(hours=3))
