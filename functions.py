from random import randint

plane = []
terminal = ['piloto', 'chefe_servico', 'policial', 'oficial_1', 'oficial_2', 'comissario_1', 'comissario_2', 'presidiario']
drivers = ['piloto', 'chefe_servico', 'policial']

def choose_driver ():
    n = randint(0, len(drivers) - 1)
    return drivers[n]

def choose_pilot_passenger ():
    options = [element for element in terminal if element in ['oficial_1', 'oficial_2']]
    if (plane.count('presidiario') != 0  and plane.count('policial') != 0):
        return 'policial'
    elif plane.count('oficial_1') != 0 or plane.count('oficial_2') != 0:
        return options.pop()
    elif plane.count('chefe_servico') == 0:
        return 'chefe_servico'
    else:
        return False

def choose_attendant_passenger ():
    options = [element for element in terminal if element in ['comissario_1', 'comissario_2']]
    if (plane.count('presidiario') != 0  and plane.count('policial') != 0):
        return 'policial'
    elif plane.count('comissario_1') != 0 or plane.count('comissario_2') != 0:
        return options.pop()
    elif plane.count('piloto') == 0:
        return 'piloto'
    else:
        return False

def choose_police_passenger ():
    options = drivers
    options.remove('policial')
    if plane.count('presidiario') != 0:
        n = randint(0, len(options) - 1)
        return options[n]
    else:
        return 'presidiario'

def move_fortwo_to_plane ():
    passenger = False

    while passenger is False:
        driver = choose_driver()
        if driver == 'piloto':
            passenger = choose_pilot_passenger()
        if driver == 'chefe_servico':
            passenger = choose_attendant_passenger()
        if driver == 'policial':
            passenger = choose_police_passenger()
    
    terminal.remove(driver)
    terminal.remove(passenger)
    print(f'{passenger} e {driver} subindo no Fortwo')
    print(f'Ficaram no terminal: {", ".join(terminal)}')
