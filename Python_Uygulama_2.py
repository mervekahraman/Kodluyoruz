# points = [‘(x, y)’] listi oluştur
# euclideanDistance’ adında bir fonksiyon tanımlayın. Bu fonksiyon, iki demet
# (her biri bir noktayı temsil eder) almalı
# ve bu iki nokta arasındaki Öklid mesafesini döndürmelidir.
# Bir döngü kullanarak, ‘points’ listesindeki her nokta çifti arasındaki Öklid mesafesini
# hesaplayın. Bu mesafeleri ‘distances’ adında başka bir listede saklayın.
# ‘distances’ listesinden minimum mesafeyi bulun ve yazdırın.
import math


def euclideanDistance(points):
    distances = []
    for p in points:
        distance = math.sqrt((p[0]) ** 2 + (p[1]) ** 2)
        distances.append(distance)
    return distances


points = [(1, 2), (3, 4)]

distances = euclideanDistance(points)
print(distances)
