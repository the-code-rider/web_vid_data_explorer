import dateutil.parser as dp

def convert_to_seconds(iso_time):
    parsed_time = dp.parse(iso_time)
    return parsed_time.timestamp()
