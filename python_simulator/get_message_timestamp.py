def _get_hours(utc_string):
    return int(float(utc_string) // (10 ** 4)) * 3600 * 1000

def _get_minutes(utc_string):
    return int((float(utc_string) // (10 ** 2) % (10 ** 2))) * 60 * 1000

def _get_seconds(utc_string):
    return int(float(utc_string) % (10 ** 2)) * 1000

def _get_milliseconds(utc_string):
    return int(utc_string.split(".")[1])

def _get_timestamp(utc_string):
    return (
        _get_hours(utc_string) + 
        _get_minutes(utc_string) + 
        _get_seconds(utc_string) + 
        _get_milliseconds(utc_string)
    )

def get_gga_message_timestamp(words):
    return _get_timestamp(words[1])

def get_gll_message_timestamp(words):
    return _get_timestamp(words[5])

def get_rmc_message_timestamp(words):
    return _get_timestamp(words[1])

def get_vtg_message_timestamp(words):
    return None

def get_gsa_message_timestamp(words):
    return None

def get_gsv_message_timestamp(words):
    return None

def get_adv_message_timestamp(words):
    return None
