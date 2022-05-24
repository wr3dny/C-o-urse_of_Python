# short deffintion to check if name is male or female
def name_checker(name):
    if name == 'Kuba':
        print(f'{name} is male')
    elif name[-1] == 'a':
        print(f'{name} is female')
    else:
        print(f'{name} is male')