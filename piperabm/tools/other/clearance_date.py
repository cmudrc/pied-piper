from datetime import date as Date


def duration(_from, _to):

    def refine_input(txt:str):
        date_list = txt.split('/')
        month = int(date_list[0])
        day = int(date_list[1])
        year = int(date_list[2])
        return year, month, day

    _from_year, _from_month, _from_day = refine_input(_from)
    _from = Date(_from_year, _from_month, _from_day)
    _to_year, _to_month, _to_day = refine_input(_to)
    _to = Date(_to_year, _to_month, _to_day)

    return _to - _from

txt = "05/19/2022 - 06/21/2022"
txt = txt.split(" - ")
_from = txt[0]
_to = txt[1]
print(duration(_from, _to))