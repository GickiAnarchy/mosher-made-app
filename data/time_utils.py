from datetime import datetime, timedelta



def get_date_verbose():
    # Returns: March 27, 2026
    return datetime.now().strftime("%B %d, %Y")


def get_date_compact():
    # Returns: 3/27/26
    # Note: %-m (Unix) or %#m (Windows) removes the leading zero
    return datetime.now().strftime("%-m/%d/%y")


def get_date_numeric():
    # Returns: 03-27-2026
    return datetime.now().strftime("%m-%d-%Y")


def get_rounded_time():
    now = datetime.now()
    # Logic: round to the nearest 30 minutes
    minute = (now.minute + 15) // 30 * 30
    if minute == 60:
        rounded_time = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
    else:
        rounded_time = now.replace(minute=minute, second=0, microsecond=0)
    # Returns format like: 3:30pm
    return rounded_time.strftime("%-I:%M%p").lower()


def calculate_hours(clock_in, clock_out):
    """
    Expects datetime objects as input.
    Example: calculate_hours(datetime(2026, 3, 27, 9, 0), datetime(2026, 3, 27, 17, 30))
    """
    delta = clock_out - clock_in
    # Convert total seconds to hours (3600 seconds in an hour)
    hours_worked = delta.total_seconds() / 3600
    return round(hours_worked, 2)


