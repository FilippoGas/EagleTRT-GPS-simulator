from get_message_timestamp import *
from time import sleep

# Returns all the text contained in the file "gps.ubx"
def read_log_file():
    gps_file = open("./gps.ubx", "r")
    text = gps_file.read()
    gps_file.close()
    return text

# Split the text in an array of lines and returns them
def get_lines(text):
    return text.splitlines()

# Parses a message, returning a dictionary with the raw line and its parsed timestamp
def parse_message(line):
    # Gets the array of words
    words = line.split(',')
    # To simulate switch in python
    switcher = {
        # TODO: Add all gps messages, it crashes if there is an unknown message type
        "$GNGGA": get_gga_message_timestamp,
        "$GNGLL": get_gll_message_timestamp,
        "$GNRMC": get_rmc_message_timestamp,
        "$GNVTG": get_vtg_message_timestamp,
        "$GNGSA": get_gsa_message_timestamp,
        "$GBGSV": get_gsv_message_timestamp,
        "$GPGSV": get_gsv_message_timestamp,
        "$GNADV": get_adv_message_timestamp,
    }
    # Raw contains the line, timestamp the milliseconds of the message or None
    return {
        "raw": line,
        "timestamp": switcher.get(words[0])(words)
    }

# Returns all the messages from the lines
def get_messages(lines):
    # TODO: filter empty lines, otherwise it crushes
    return list(map(parse_message, lines))

# Returns the messages with the timestamp modfied: it will contain the number of milliseconds passed from the last message
def parse_timestamps(messages):
    last_timestamp = None
    for m in messages:
        if last_timestamp is None:
            if m.get("timestamp") is None:
                m.update(timestamp = 0)
            else:
                last_timestamp = m.get("timestamp")
                m.update(timestamp = 0)
        else:
            if m.get("timestamp") is None:
                m.update(timestamp = 0)
            else:
                temp = m.get("timestamp")
                m.update(timestamp = temp - last_timestamp)
                last_timestamp = temp

# It emulates the serial port from the gps messages
def emulate(messages):
    for m in messages:
        # Sleep for milliseconds
        sleep(m.get("timestamp") / 1000)
        # TODO: Print on serial port
        print(m.get("raw"))

# The main procedure
def main():
    log_text = read_log_file()
    lines = get_lines(log_text)
    messages = get_messages(lines)
    parse_timestamps(messages)
    while True:
        emulate(messages)
    
# Executes the main procedure
main()

