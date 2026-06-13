def mm_dd_yy_to_yy_dd_mm(date: str) -> str:
    mm = date[:2]
    dd = date[3:5]
    yy = date[6:]

    return (f"{yy}-{dd}-{mm}")



print(mm_dd_yy_to_yy_dd_mm("12-25-21"))
