def date_info(start_date, end_date):
    #format_YMD = date.strftime('%Y-%m-%d')
    txt = ''
    txt += '['
    txt += str(start_date)
    txt += ' - '
    txt += str(end_date)
    txt += ']'
    return txt


if __name__ == "__main__":
    from piperabm.unit import Date

    kwargs = {
        "start_date": Date(2020, 1, 1),
        "end_date": Date(2020, 1, 2),
    }
    txt = date_info(**kwargs)
    print(txt)