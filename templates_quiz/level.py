def choose_level(n_pregunta, p_level):
    
    levels_per_question = {
        1: 'Básica',
        2: 'Básica',
        3: 'Intermedia',
        4: 'Intermedia',
        5: 'Avanzada',
        6: 'Avanzada'
    }
   
    
    level = levels_per_question.get(n_pregunta, 'No definido')
    
    return level


if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias