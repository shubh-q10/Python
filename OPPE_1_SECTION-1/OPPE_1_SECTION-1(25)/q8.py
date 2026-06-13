def mm_dd_yy_to_yy_dd_mm(date: str) -> str:
    return (date[-2:] + date[2:6] + date[0:2])