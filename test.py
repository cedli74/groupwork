import pytest
from nombre_premier import est_premier, liste_nombres_premiers

# Assurez-vous que les fonctions est_premier et liste_nombres_premiers sont déjà définies

def test_est_premier():
    # Tests des nombres premiers
    assert est_premier(2) == True
    assert est_premier(3) == True
    assert est_premier(5) == True
    assert est_premier(11) == True
    
    # Tests des nombres non premiers
    assert est_premier(1) == False
    assert est_premier(4) == False
    assert est_premier(9) == False
    assert est_premier(15) == False
    assert est_premier(25) == False

def test_liste_nombres_premiers():
    # Tests des listes de nombres premiers
    assert liste_nombres_premiers(1) == []
    assert liste_nombres_premiers(2) == [2]
    assert liste_nombres_premiers(10) == [2, 3, 5, 7]
    assert liste_nombres_premiers(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert liste_nombres_premiers(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

if __name__ == "__main__":
    pytest.main()
