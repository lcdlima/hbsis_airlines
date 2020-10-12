from random import randint
import sys

plane = []
terminal = ['piloto', 'chefe_servico', 'policial', 'oficial_1', 'oficial_2', 'comissario_1', 'comissario_2', 'presidiario']

def choose_driver ():
    drivers = [element for element in terminal if element in ['piloto', 'chefe_servico', 'policial']]
    n = randint(0, len(drivers) - 1)
    return drivers[n]

def choose_pilot_passenger ():
    options = [element for element in terminal if element in ['oficial_1', 'oficial_2']]
    if plane.count('oficial_1') == 0 or plane.count('oficial_2') == 0:
        return options.pop()
    elif plane.count('chefe_servico') == 0:
        return 'chefe_servico'
    else:
        return False

def choose_attendant_passenger ():
    options = [element for element in terminal if element in ['comissario_1', 'comissario_2']]
    if plane.count('comissario_1') == 0 or plane.count('comissario_2') == 0:
        return options.pop()
    elif plane.count('piloto') == 0:
        return 'piloto'
    else:
        return False

def choose_police_passenger ():
    options = [element for element in terminal if element in ['piloto', 'chefe_servico']]
    if len(terminal) == 2 and terminal.count('policial') != 0 and terminal.count('presidiario') != 0:
        return 'presidiario'
    elif len(terminal) == 3:
        return options.pop()
    else:
        return False

def move_fortwo_to_plane (person):
    if person is not None:
        terminal.append(person)
        print(' ')
        print('Fortwo chegou ao Terminal')
        print(f'{person} embarcou no Terminal')

    passenger = False

    while passenger is False:
        driver = choose_driver()
        if driver == 'piloto':
            passenger = choose_pilot_passenger()
        elif driver == 'chefe_servico':
            passenger = choose_attendant_passenger()
        elif driver == 'policial':
            passenger = choose_police_passenger()
    
    terminal.remove(driver)
    terminal.remove(passenger)
    print(f'{passenger} e {driver} saindo do Terminal no Fortwo')
    print(f'Ficou no Terminal: {", ".join(terminal)}')
    move_fortwo_to_terminal (driver, passenger)

def move_fortwo_to_terminal (driver, passenger):
    print(' ')
    print('Fortwo chegou ao Avião')
    print(f'{passenger} e {driver} embarcaram no Avião')

    plane.append(passenger)
    plane.append(driver)

    if len(plane) == 8:
        sys.exit('Todos embarcaram no Avião!')

    if (terminal.count('oficial_1') != 0 or terminal.count('oficial_2') != 0) and plane.count('piloto') != 0:
        person_to_return = 'piloto'
    elif (terminal.count('comissario_1') != 0 or terminal.count('comissario_2') != 0) and plane.count('chefe_servico') != 0:
        person_to_return = 'chefe_servico'
    elif terminal == ['presidiario'] and plane.count('policial') != 0:
        person_to_return = 'policial'
    else:
        options = [element for element in plane if element in ['piloto', 'chefe_servico']]
        person_to_return = options.pop()
    
    plane.remove(person_to_return)
    print(f'{person_to_return} saindo do Avião no Fortwo')
    print(f'Ficou no Avião: {", ".join(plane)}')
    move_fortwo_to_plane (person_to_return)

move_fortwo_to_plane (None)
