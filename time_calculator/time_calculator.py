# very bad code example
from typing import Dict, Any


def add_time(start, duration, day=None):
    if day is not None:
      day = day.lower()
    global new_hours
    global day_number

    time_dict: dict[str | Any, str | Any] = {'13': '1', '14': '2', '15': '3', '16': '4', '17': '5', '18': '6',
                                             '19': '7', '20': '8', '21': '9',
                                             '22': '10', '23': '11', '24': '12'}
    week_days = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}
    day_now = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    count_days = 0

    first_hours = start.split(":")
    second_hours = duration.split(":")
    day_night = (first_hours[1]).split()
    am_pm_was = day_night[1]

    hours_was = int(first_hours[0])
    hours_added = int(second_hours[0])

    minutes_was = int(day_night[0])
    minutes_added = int(second_hours[1])

    sum_hours = (hours_was + hours_added)

    new_minutes = minutes_was + minutes_added
    if new_minutes > 60:
        sum_hours += new_minutes // 60
        sum_minutes = str(new_minutes % 60)
        new_minutes = str(sum_minutes)
    else:
        new_minutes = str(new_minutes)

    while sum_hours >= 12:
        if 12 <= sum_hours < 24 and am_pm_was == 'PM':
            am_pm_was = 'AM (next day)'
            count_days += 1
            break
        elif 12 <= sum_hours < 24 and am_pm_was == 'AM':
            am_pm_was = 'PM'
            break
        elif sum_hours > 24 and (sum_hours // 12) % 2 == 0 and am_pm_was == 'AM':
            am_pm_was = 'AM'
            break
        elif sum_hours > 24 and (sum_hours // 12) % 2 == 0 and am_pm_was == 'PM':
            am_pm_was = 'PM'
            break
        elif sum_hours > 24 and (sum_hours // 12) % 2 != 0 and (am_pm_was == 'PM' or am_pm_was == 'AM'):
            if am_pm_was == 'AM':
                am_pm_was = 'PM'
                break
            else:
                am_pm_was = 'AM'
                count_days += 1
                break

    while sum_hours > 12:
        if am_pm_was == 'PM':
            count_days += (sum_hours // 24)
            try:
                new_hours = time_dict[str(sum_hours % 24)]
            except:
                new_hours = str(sum_hours)
            if (sum_hours // 12) % 2 != 0 and count_days > 1:
                am_pm_was = 'PM'
                break
            else:
                try:
                    new_hours = time_dict[str(sum_hours % 24)]
                except:
                    new_hours = str(sum_hours)
                # print(new_hours)
                break
            # new_hours = time_dict[str(sum_hours)]
        else:
            count_days += sum_hours // 24
            try:
                new_hours = time_dict[str(sum_hours % 24)]
                # print(new_hours)
                break
            except:
                new_hours = str(sum_hours)
                break
            if (sum_hours // 12) % 2 != 0 and count_days > 1:
                am_pm_was = 'AM'
                break

    if sum_hours <= 12:
        new_hours = str(sum_hours)

    days_counter = count_days
    print(days_counter)
    #print(day_now[week_days[day] + count_days])
    try:
        if 1 <= days_counter < 8:
            day_number = day_now[week_days[day] + count_days]
        else:
            while days_counter > 7:
                days_counter -= 7
                if days_counter < 7:
                    days_counter = 7 - days_counter
                    day_number = day_now[days_counter]
                    print(day_number)
                    break
    except:
        day = None

    while sum_hours > 24:
        sum_hours = sum_hours - 24
        if 12 < sum_hours < 25:
            new_hours = time_dict[str(sum_hours % 24)]
            break
        elif sum_hours <= 12:
            new_hours = str(sum_hours)
            break

    if count_days == 1 and am_pm_was == 'AM':
        am_pm_was = 'AM (next day)'

    #if am_pm_was == 'AM (next day)':
        #am
    if day is not None:
        if len(new_minutes) != 2:
            if count_days > 1:
                return new_hours + ':' + '0' + str(
                    new_minutes) + ' ' + am_pm_was + f', {day_number}' + f' ({count_days} days later)'
            else:
                if am_pm_was == 'AM (next day)':
                    am_pm_was.split()
                    return new_hours + ':' + '0' + str(
                    new_minutes) + ' ' + am_pm_was[0] + f', {day_number}' + ' (next day)'
                else:
                    return new_hours + ':' + '0' + str(
                        new_minutes) + ' ' + am_pm_was + f', {day_number}'
        else:
            if count_days > 1:
                return new_hours + ':' + str(
                    new_minutes) + ' ' + am_pm_was + f', {day_number}' + f' ({count_days} days later)'
            else:           # else3eee ee
                if am_pm_was == 'AM (next day)':
                    am_pm_was = am_pm_was.split()
                    return new_hours + ':' + str(
                        new_minutes) + ' ' + am_pm_was[0] + f', {day_number}' + ' (next day)'
                else:
                    return new_hours + ':' + str(
                        new_minutes) + ' ' + am_pm_was + f', {day_number}'
    else:
        if len(new_minutes) != 2:
            if count_days > 1:
                return new_hours + ':' + '0' + str(new_minutes) + ' ' + am_pm_was + f' ({count_days} days later)'
            else:
                return new_hours + ':' + '0' + str(new_minutes) + ' ' + am_pm_was
        else:
            if count_days > 1:
                return new_hours + ':' + str(new_minutes) + ' ' + am_pm_was + f' ({count_days} days later)'
            else:
                return new_hours + ':' + str(new_minutes) + ' ' + am_pm_was
