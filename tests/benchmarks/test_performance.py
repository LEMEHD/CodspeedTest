

from src.algorithms import fibonacci_recursive, fibonacci_iterative

def test_fibonacci_recursive(benchmark):
    """
    Test de performance pour la version récursive.
    On utilise n=20 car c'est déjà assez lourd pour du récursif pur.
    """
    # La syntaxe est: benchmark(fonction_a_tester, arguments...)
    result = benchmark(fibonacci_recursive, 20)
    
    # On peut quand même vérifier que le résultat est juste !
    assert result == 6765

def test_fibonacci_iterative(benchmark):
    """
    Test de performance pour la version itérative.
    Celle-ci devrait être infiniment plus rapide.
    """
    result = benchmark(fibonacci_iterative, 20)
    
    assert result == 6765