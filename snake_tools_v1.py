"""
              A set of functions for the snake game (v.1)
"""
import random

from snake_params import LEFT, RIGHT, UP, DOWN, WIDTH, HEIGHT, BLOCK_SIZE


def new_apple(x_snake, y_snake):
    """
    Return a random position for the apple (not onto the snake).
    """
    ### ON PEUT UTILISER QUELQUE CHOSE COMME
    x = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    y = (random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    ### MAIS IL FAUT QUE LA POMME NE SOIT PAS SUR UN BLOCK DU SERPENT !
    
            
    return x, y


def new_head(x_snake, y_snake, direction):
    """
    Return the new position of the snake's head after one step moving.
    
    The function does not verify whether the direction is correct or not.
    
    >>> new_head([200, 190, 180], [ 200, 200, 200], RIGHT)
    (210, 200)
    
    >>> new_head([200, 190, 180], [ 200, 200, 200], UP)
    (200, 190)
    
    """
    
    ### COMPLÈTER POUR RÉCUPÉRER LA POSITION ACTUELLE DE LA TÊTE
    x = ...
    y = ...
    ### PUIS POUR DÉTERMINER LES NOUVELLES VALEURS DE x ET y...
    ### PS : . LES x AUGMENTENT VERS LA DROITE, LES y AUGMENTENT VERS LE BAS
    ###      . AUGMENTER OU DIMINUER x ET/OU y DE `BLOCK_SIZE`
    if direction == RIGHT:
        ###...
        pass
    return x, y


def next_snake(x_snake, y_snake, x_head, y_head):
    """
    Return the modified snake, possibly beyond the edges or biting itself.
    
    `x_head`, `y_head` give the next position of the snake's head.
    The function does not verify whether the direction is correct or not.

    >>> next_snake([200, 190, 180], [ 200, 200, 200], 200, 190)
    ([200, 200, 190], [190, 200, 200])
   
    """
    assert len(x_snake) == len(y_snake)
    ### DÉCALER LES VALEURS DES BLOCS DU SERPENT
    ###  (PLUS FACILE EN PARTANT DE LA FIN !)
    # ...
    
    return x_snake, y_snake


def lost(x_snake, y_snake) -> bool:
    """
    Return True if the snake bites itself or is beyond the edges, else False.

    >>> lost([200, 190, 180], [ 200, 200, 200])
    False

    beyond the edges
    >>> lost([0, 0, 0], [ -BLOCK_SIZE, 0,  BLOCK_SIZE])
    True

    bites itself
    >>> lost([0, 0, 10, 10, 0], [0, 10, 10, 0, 0])
    True

    """
    ### COMPLÈTER POUR RÉCUPÉRER A POSITION DE LA TÊTE DU SERPENT
    x = 0 # ...
    y = 0 # ...
    ### COMPLÈTER POUR DÉTECTER LES SORTIES DE LA ZONE DE JEU
    if x > WIDTH - BLOCK_SIZE : ### ...
        return True
        
    ### COMPLÈTER POUR DÉTECTER LES CAS OÙ LE SERPENT SE MORD LUI-MÊME        
    assert len(x_snake) == len(y_snake)        
    #for ...
        #if ...
            # return True

    # On a passé avec succès tous les tests précédents
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()