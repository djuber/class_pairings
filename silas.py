from random import randrange, randint

Class = ['Boring Guy']*47
Kids =  ['Silas', 'Suyeon', 'Calvin']
Class += Kids

def random_elt(group):
    limit = len(group)
    return group[randrange(limit)]

def pairings(group):
    output = []
    r = randint(1,len(group)-1)
    output.append((group[0], group[r]))
    if len(group) > 2:
        output += pairings(group[1:r] + group[r+1:])
    return output

def on_the_bus(paired):
    output = []
    for pair in paired:
        output.append(random_elt(pair))
    return output

def students_all_on_the_bus():
    field_trip = on_the_bus(pairings(Class))
    for kid in Kids:
        if kid not in field_trip:
            return False
    return True
    
def all_separate(n):
    def separate_once():
        pairing = pairings(Class)
    
        for pair in pairing:
            if pair != ('Boring Guy', 'Boring Guy'):
                if 'Boring Guy' not in pair:
                    return False
        return True
    count = 0
    for i in range(n):
        count += separate_once()
    return 1.0 * count / n
    
def sample(n):
    count = 0
    for i in range(n):
        count += students_all_on_the_bus()
    return 1.0 * count / n


def product(myrange, function):
    return reduce ( lambda x,y : x * y, map(function, myrange))

def summation(myrange, function):
    return reduce ( lambda x,y : x + y, map(function, myrange))