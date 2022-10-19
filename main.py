from game import InLine

def print_tablero(game):
        print('  0    1    2    3    4    5    6')
        for r in game.board:
            print (r)

def choose_col(game):
    try:
        col_input = int(input(f'Jugador {game.player} ingrese un número del 0 al 6: '))
        try:
            game.throw_coin(col_input)
            print_tablero(game)
        except TypeError:
            print('No hay mas espacio, elija otra casilla')
    except ValueError:
        print('No se ha ingresado un numero, intente nuevamente')
    except IndexError:
        print('La columna ingresada no existe, intente nuevamente')    


if __name__ == '__main__':
    game = InLine()
    print_tablero(game)
    while True:
        choose_col(game)
        if game.check_winner() == True:
            print(f'El juego ha terminado. Felicitaciones {game.winner}, has ganado')
            break
        

