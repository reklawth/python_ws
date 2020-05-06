## Durations

Durations are modelled in Python by the timedelta type, which is the difference between two dates or datetimes.

## Time zones

To create time zone 'aware' objects we must attach instances of a tzinfo object to our time values.  Time zones, and daylight saving time, are a very complex domain mired in international politics and which could change atany time.  Because of this, the Python standard library does not include exhaustive time zone data.  For up-to-ate time zone data you will need to use the third party pytz or dateutil modules.  Python 3 - although not Python 2 - contains rudimentary support for timezone specification.  The tzinfo abstraction, on which more complete timezone support can be added, is supported in both Python2 and Python 3.