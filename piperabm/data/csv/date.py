from datetime import date


def load_date(data: str, split: str, arrangement: str):
    data_splitted = data.split(split)
    if arrangement == 'mmddyy':
        day = data_splitted[1]
        month = data_splitted[0]
        year = '20' + data_splitted[2]
    elif arrangement == 'yyyymmdd':
        day = data_splitted[2]
        month = data_splitted[1]
        year = data_splitted[0]
    else:
        raise ValueError("arrangement not recognized")
    return date(
        year=int(year),
        month=int(month),
        day=int(day)
    )


if __name__ == "__main__":
    # 1
    d = load_date(
        data='4/30/16',
        split='/',
        arrangement='mmddyy'
    )
    print(d)

    # 2
    d = load_date(
        data='2017-06-24',
        split='-',
        arrangement='yyyymmdd'
    )
    print(d)

