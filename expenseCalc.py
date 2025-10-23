exp = -1
total_exp = 0
max_exp = 0
min_exp = 0

while exp != 0:
    exp = int(input("what is expense? (type 0 to stop)"))
    total_exp = total_exp + exp
    if exp > max_exp:
        max_exp = exp
    elif exp != 0 & exp < min_exp:
        min_exp = exp

print("total exp: ", total_exp)
print('Min exp: ', min_exp);
print('Max exp: ', max_exp);
