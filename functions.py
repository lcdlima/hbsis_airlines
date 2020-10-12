from random import randint
import sys

plane = []
terminal = ['piloto', 'chefe_servico', 'policial', 'oficial_1', 'oficial_2', 'comissario_1', 'comissario_2', 'presidiario']
drivers = ['piloto', 'chefe_servico', 'policial']

def choose_driver ():
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
    options = drivers
    options.remove('policial')
    if terminal == ['policial', 'presidiario']:
        return 'presidiario'
    elif len(terminal) == 3:
        return options.pop()
    else:
        return False

def move_fortwo_to_plane (person):
    if person is not None:
        terminal.append(person)
        drivers.append(person)
        print(' ')
        print(f'{person} chegando ao Terminal no Fortwo')

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
    drivers.remove(driver)
    terminal.remove(passenger)
    print(f'{passenger} e {driver} saindo do Terminal no Fortwo')
    print(f'Ficaram no Terminal: {", ".join(terminal)}')
    move_fortwo_to_terminal (driver, passenger)

def move_fortwo_to_terminal (driver, passenger):
    print(' ')
    print(f'{passenger} e {driver} chegando ao Avião no Fortwo')

    plane.append(passenger)
    plane.append(driver)

    if len(terminal) == 8:
        sys.exit('Todos embarcaram no avião!')

    if (terminal.count('oficial_1') != 0 or terminal.count('oficial_2') != 0) and plane.count('piloto') != 0:
        person_to_return = 'piloto'
    elif (terminal.count('comissario_1') != 0 or terminal.count('comissario_2') != 0) and plane.count('chefe_servico') != 0:
        person_to_return = 'chefe_servico'
    elif terminal == ['presidiario']:
        person_to_return = 'policial'
    else:
        options = [element for element in terminal if element in ['piloto', 'chefe_servico']]
        person_to_return = options.pop()
    
    plane.remove(person_to_return)
    print(f'{person_to_return} saindo do Avião no Fortwo')
    print(f'Ficaram no Avião: {", ".join(plane)}')
    move_fortwo_to_plane (person_to_return)

move_fortwo_to_plane (None)
