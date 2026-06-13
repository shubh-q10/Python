def seconds_to_minute_seconds(seconds: int) -> tuple:
    minutes = ((seconds)//60)
    seconds = ((seconds) - (60 * minutes))
    return (minutes, seconds)

print(seconds_to_minute_seconds(123))