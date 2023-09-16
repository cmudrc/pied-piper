from piperabm.time import Date


def date_serialize(date: Date) -> dict:
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


if __name__ == "__main__":
    date = Date(2000, 1, 1)
    dictionary = date_serialize(date)
    print(dictionary)
