from piperabm.time import Date


def date_deserialize(dictionary: dict) -> Date:
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
    dictionary = {'year': 2000, 'month': 1, 'day': 1, 'hour': 0, 'minute': 0, 'second': 0}
    date = date_deserialize(dictionary)
    print(date)
