* Dans ce TP, nous allons utiliser le solveur de contraintes de Google. La
  documentation est https://developers.google.com/optimization/cp/cp_solver.

* Installer la librairie `ortools` à partir de pip
```
python3 -m pip install ortools
# ou
pip3 install ortools
```
* Exécuter le fichier intro.py
  * Que fait ce programme ?
  ```
  Le programme définit trois variables x, y, z.
  La variable x a une valeur comprise dans l'intervale [0, 1]. 
  La variable y a une valeur comprise dans l'intervale [0, 2]. 
  La variable z a une valeur comprise dans l'intervale [0, 3]. 
  Le programme calcule les valeurs de ces trois variables afin que x soit
  différent de y. 
  ```
  * La fonction solver.solve() retourne un statut pouvant avoir 5 valeurs.
    Quelles sont les statuts possibles pour un problème possèdant des solutions ?
    ```
    2 statuts sont possibles pour un problème possèdant des solutions :
     - optimal: la solution retournée est la solution optimale
     - feasible: une solution a été trouvée mais on ne sait pas si c'est la
       solution optimale
    ```
* Modifier le programme afin d'afficher les valeurs de x, y et z de la solution
  trouvée par le solveur. Quelles sont les valeurs de x, y et z ?
  ```
  voir le fichier intro_correction.py
  x = 1 ; y = 0 ; z = 0
  ```
* Modifier le programme pour ajouter la contrainte : "x doit être strictement
  plus petit que z". Quelles sont les valeurs de x, y et z ?
  ```
  voir le fichier intro_correction.py
  x = 0 ; y = 1 ; z = 3
  ```
* À l'aide de la documentation et de la classe VarArraySolutionPrinter du module
  s_printer.py, afficher toutes les solutions du problème décrits. Lister les
  solutions obtenues.
  * Pour importer la classe VarArraySolutionPrinter, utiliser la ligne suivante:
    `from s_printer import VarArraySolutionPrinter`
  ```
  voir le fichier intro_printer_correction.py
    x=0 y=2 z=2
    x=0 y=2 z=1
    x=0 y=1 z=1
    x=0 y=1 z=2
    x=0 y=1 z=3
    x=0 y=2 z=3
    x=1 y=2 z=3
    x=1 y=2 z=2
    x=1 y=0 z=2
    x=1 y=0 z=3
  ```
