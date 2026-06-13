L = [('Sachin', 'AUS', 240), ('Laxman', 'AUS', 289),
     ('Sachin', 'WI', 78), ('Dravid', 'WI', 210),
     ('Dravid', 'AUS', 200), ('Dravid', 'WI', 210),
     ('Sachin', 'AUS', 50), ('Dravid', 'WI', 50),
     ('Laxman', 'AUS', 30), ('Laxman', 'WI', 10)]

D = { }
for item in L:
    player, opp, runs = item
    key = (player, opp)
    if key not in D:
        D[key] = 0
    D[key] += runs

player = input()
opp = input()
if D[(player, opp)] >= 300:
    print('Star Batsman')