def check_existance(initiation_date, start_date, end_date):
    """
    Check element existance based on its initiation_date
    """
    exists = False
    if start_date is None or end_date is None:
        exists = True
    else:
        if initiation_date < end_date:
            exists = True
        else:
            exists = False
    return exists