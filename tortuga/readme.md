# Tortuga

To solve this challenge, all that was needed was plotting the figures asked for. This script did the trick

```python
import matplotlib.pyplot as plt

def dessiner_formes(liste_segments):
    # Initialiser le point de départ à (0, 0)
    x, y = 0, 0
    # Initialiser les listes pour stocker les coordonnées des points
    x_points = [x, x]
    y_points = [y, y]

    # Parcourir la liste de segments
    for dx, dy in liste_segments:
        # Si (dx, dy) est différent de (0, 0), dessiner un segment
        if dx != 0 or dy != 0:
            # Calculer les coordonnées du nouveau point
            x += dx
            y -= dy
            # Ajouter les coordonnées du nouveau point aux listes
            x_points.append(x)
            y_points.append(y)
        else:
            plt.plot(x_points[1:], y_points[1:])
            x_points = [x_points[-1]]
            y_points = [y_points[-1]]

    # Dessiner les formes
    plt.plot(x_points[1:], y_points[1:])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Dessin des formes')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Exemple d'utilisation avec la liste fournie
liste_segments_exemple = [
    (2, 0), (-1, 2), (-1, -2),
    (0, 0), (3, 0),
    (-1, 2), (2, 0), (-1, -2),
    (0, 0), (1, 0),
] * 6
liste_segments_exemple = [(0,2),(0,-2),(1,0),(-1,0),(0,1),(1,0),(0,0),(1,1),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,0),(2,-2),(-1,0),(0,1),(1,0),(0,1),(-1,0),(0,0),(2,0),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,0),(3,-2),(-1,0),(0,1),(-1,0),(1,0),(0,1),(1,0),(0,0),(4,-2),(-2,0),(0,0),(0,2),(2,0),(0,-2),(0,1),(-2,0),(0,0),(3,-1),(0,2),(0,0),(3,-2),(-1,0),(-1,1),(0,1),(2,0),(0,-1),(-2,0),(0,0),(3,0),(1,0),(0,-1),(-1,0),(0,2),(1,0),(0,-1),(0,0),(1,1),(1,0),(0,-2),(-1,0),(0,0),(0,1),(1,0),(0,0),(2,1),(0,-2),(-1,1),(2,0),(0,0),(1,-1),(1,0),(-1,2),(0,0),(0,-1),(1,0),(0,0),(1,-1),(1,0),(0,1),(-1,0),(0,1),(1,0),(0,0),(1,0),(1,0),(0,-1),(-1,0),(0,-1),(1,0),(0,0),(1,2),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,-1),(-1,0),(0,0),(2,1),(1,0),(-1,0),(0,-2),(1,0),(-1,2),(1,0),(0,-2),(0,0),(1,0),(0,1),(1,0),(0,-1),(0,2),(0,0),(2,-2),(1,0),(0,1),(1,0),(-1,0),(0,1),(-1,0)]

dessiner_formes(liste_segments_exemple)

```
