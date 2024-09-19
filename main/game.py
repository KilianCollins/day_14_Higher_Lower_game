import random

score  = 0

ppl_list = [
    ["Shakira", 23_456],
    ["NASA", 4_000_000],
    ["John Lennon", 34_000_000],
    ["Tom von jones", 900_000],
]

def choose_ppl(list):
    randchoice = random.randint(0,3)
    for i in ppl_list:
        key = i[0]
        value = i[1]
        list = [key,value]
    return list
#     need to find a way to return only the keys.

A = choose_ppl(ppl_list)
B = choose_ppl(ppl_list)

# first compututer has to choose two canadates,
print(A, B)

# then user has to choose between the two

# comp checks if user is right

    # then 1 point is added to the score

    # else game over

# after first choice comp only chooses one new peerson




