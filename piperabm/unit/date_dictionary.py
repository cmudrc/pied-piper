from piperabm.unit import Date


def date_to_dict(date: Date) -> dict:
    result = None
    if date is not None:
        result = {
            'year': date.year,
            'month': date.month,
            'day': date.day,
            'hour': date.hour,
            'minute': date.minute,
            'second': date.second
        }
    return result


def date_from_dict(dictionary: dict) -> Date:
    result = None
    if dictionary is not None:
        result = Date(
            year=dictionary['year'],
            month=dictionary['month'],
            day=dictionary['day'],
            hour=dictionary['hour'],
            minute=dictionary['minute'],
            second=dictionary['second']
        )
    return result


if __name__ == "__main__":
    date = Date(2000, 1, 1)
    dictionary = date_to_dict(date)
    date = date_from_dict(dictionary)
    print(date)
