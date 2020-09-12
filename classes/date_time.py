from skyfield.api import load
from pytz import timezone
from datetime import datetime

class DateTime:
    def __init__(self, js_timestamp):
        self.timestamp = datetime.fromtimestamp(js_timestamp)
        self.set_time()

    def set_time(self):
        timescale = load.timescale()
        central = timezone('Europe/Warsaw')
        d = self.timestamp
        c = central.localize(d)
        self.astrometric_dt = timescale.utc(c)
        self.universal_dt = self.astrometric_dt.utc_datetime()
        self.local_dt = self.astrometric_dt.astimezone(central)

    def get_range(self):

        return month_range