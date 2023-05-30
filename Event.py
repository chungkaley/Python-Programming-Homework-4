from Date import Date

class Event:
    def __init__(self, event_name, start_hour, end_hour, event_date):
        self.event_name = event_name
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.event_date = event_date

    def __str__(self):
        return f"{self.event_name} ({self.start_hour} to {self.end_hour}) on {self.event_date}"

    @property
    def start_hour(self):
        return self._start_hour

    @start_hour.setter
    def start_hour(self, value):
        if value < 0 or value > 23:
            raise ValueError("Start hour must be between 0 and 23")
        self._start_hour = value

    @property
    def end_hour(self):
        return self._end_hour

    @end_hour.setter
    def end_hour(self, value):
        if value < 0 or value > 23:
            raise ValueError("End hour must be between 0 and 23")
        self._end_hour = value

    def has_overlap(self, other):
        if self.event_date != other.event_date:
            return False
        if self.start_hour < other.end_hour and self.end_hour > other.start_hour:
            return True
        return False

