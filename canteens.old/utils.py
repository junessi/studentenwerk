import datetime
import math
import re

def parse_date(date_query):
    weekday = datetime.datetime.today().weekday()
    monday = datetime.datetime.today() - datetime.timedelta(days = weekday)
    sunday = monday + datetime.timedelta(days = 6)
    monday_int = int("{0}{1:02d}{2:02d}".format(monday.year, monday.month, monday.day))
    sunday_int = int("{0}{1:02d}{2:02d}".format(sunday.year, sunday.month, sunday.day))

    # default: this week
    date_range = [monday_int, sunday_int]
    
    date_range_str = str(date_query)
    if len(date_range_str) > 0:
        today = datetime.datetime.today()

        # interpret some words
        if date_range_str == "nextweek":
            date_range_str = "next1weeks"
        elif date_range_str == "lastweek":
            date_range_str = "last1weeks"

        # today
        if re.match("yesterday", date_range_str):
            yesterday = today - datetime.timedelta(days = 1)
            yesterday_int = int("{0}{1:02d}{2:02d}".format(yesterday.year, yesterday.month, yesterday.day))
            date_range = [yesterday_int, yesterday_int]
        elif re.match("today", date_range_str):
            today_int = int("{0}{1:02d}{2:02d}".format(today.year, today.month, today.day))
            date_range = [today_int, today_int]
        elif re.match("tomorrow", date_range_str):
            tomorrow = today + datetime.timedelta(days = 1)
            tomorrow_int = int("{0}{1:02d}{2:02d}".format(tomorrow.year, tomorrow.month, tomorrow.day))
            date_range = [tomorrow_int, tomorrow_int]
        elif re.match(r"(next|last)(\d+)weeks", date_range_str):
            m = re.match(r"(next|last)(\d+)weeks", date_range_str)
            n = int(m.group(2))
            if m.group(1) == "next":
                monday = monday + datetime.timedelta(days = 7*n)
                sunday = sunday + datetime.timedelta(days = 7*n)
            elif m.group(1) == "last":
                monday = monday - datetime.timedelta(days = 7*n)
                sunday = sunday - datetime.timedelta(days = 7*n)
            date_range = [int("{0}{1:02d}{2:02d}".format(monday.year, monday.month, monday.day)),
                          int("{0}{1:02d}{2:02d}".format(sunday.year, sunday.month, sunday.day))]
        elif re.match(r"(next|last)(\d+)days", date_range_str):
            m = re.match(r"(next|last)(\d+)days", date_range_str)
            if m.group(1) == "next":
                day_start = today + datetime.timedelta(days = 1)
                day_end   = today + datetime.timedelta(days = int(m.group(2)))
                date_range = [int("{0}{1:02d}{2:02d}".format(day_start.year, day_start.month, day_start.day)),
                              int("{0}{1:02d}{2:02d}".format(day_end.year, day_end.month, day_end.day))]
            elif m.group(1) == "last":
                day_start = today - datetime.timedelta(days = 1)
                day_end   = today - datetime.timedelta(days = int(m.group(2)))
                date_range = [int("{0}{1:02d}{2:02d}".format(day_end.year, day_end.month, day_end.day)),
                              int("{0}{1:02d}{2:02d}".format(day_start.year, day_start.month, day_start.day))]
        elif re.match(r"from(\d{8})to(\d{8})", date_range_str):
            m = re.match("from(\d{8})to(\d{8})", date_range_str)
            date_range = [int((m.group(1)), int(m.group(2)))]
        elif re.match(r"\[([+,-]?\d+),([+,-]?\d+)\]", date_range_str):
            m = re.match(r"\[([+,-]?\d+),([+,-]?\d+)\]", date_range_str)
            start = int(m.group(1))
            end = int(m.group(2))
            if start <= end:
                day_start = today
                day_end = today
                if start < 0:
                    day_start = today - datetime.timedelta(days = math.fabs(start))
                else:
                    day_start = today + datetime.timedelta(days = math.fabs(start))
                if end < 0:
                    day_end = today - datetime.timedelta(days = math.fabs(end))
                else:
                    day_end = today + datetime.timedelta(days = math.fabs(end))

                date_range = [int("{0}{1:02d}{2:02d}".format(day_start.year, day_start.month, day_start.day)),
                              int("{0}{1:02d}{2:02d}".format(day_end.year, day_end.month, day_end.day))]

    print(date_range)
    return date_range

