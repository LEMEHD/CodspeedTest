from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_recursive(n):
    """
    Calcule la suite de Fibonacci de manière récursive.
    MAINTENANT OPTIMISÉE AVEC UN CACHE !
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    """
    Calcule la suite de Fibonacci avec une boucle.
    C'est la méthode optimisée. Elle est beaucoup plus rapide.
    Complexité : Linéaire O(n)
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b