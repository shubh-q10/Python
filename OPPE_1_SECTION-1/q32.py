def next_roll_no(roll_no: str) -> str:
    yyr = roll_no[:3]
    num = int(roll_no[3:]) + 1
    return f'{yyr}{num}'

#next_roll_no("24f3099999") -> '24f3100000'
print(next_roll_no("24f3999999"))


