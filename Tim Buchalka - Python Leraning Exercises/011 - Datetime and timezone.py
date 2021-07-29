import pytz
import datetime

country = 'Europe/Moscow'

timezone = pytz.timezone(country)
local_time = datetime.datetime.now(tz=timezone)

print(f'The time in {country} is {local_time}')
print(f'UTC is {datetime.datetime.utcnow()}')

# for options in pytz.all_timezones:
#     print(options)                      List of all countries timezones

