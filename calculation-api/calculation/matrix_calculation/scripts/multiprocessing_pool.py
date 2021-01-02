import tracemalloc
import math
from multiprocessing import Pool
from functools import partial
import time

def calcualte_distance(matrix_point, special_point):
    return math.sqrt((matrix_point[0] - special_point[0])**2 + (matrix_point[1] - special_point[1])**2)

def get_distances(matrix_point, special_points):
    return (calcualte_distance(matrix_point, point) for point in special_points)

def find_nearest(matrix_point, special_points):
    return min(enumerate(get_distances(matrix_point, special_points)), key=lambda point: point[1])[0]

def generate_points(n, m):
    return ((i, j) for i in range(n) for j in range(m))

def chunk(n, m):
    if n > 2:
        return 2 * m
    else:
        return n

def compute(n, m, special_points):
    with Pool() as pool:
        yield from pool.imap(partial(find_nearest, special_points=special_points), generate_points(n, m), chunksize=chunk(n, m))

def to_int(point_coordinates):
    point = point_coordinates.split(",")
    return (int(point[0]), int(point[1]))

def cast_points(special_points):
    return [to_int(point) for point in special_points]


def api(n, m, special_points):
    tracemalloc.start()
    start = time.time()
    results = compute(n, m, cast_points(special_points))
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return results, current, peak, time.time() - start


def main():
    n = 700
    m = 700
    special_points = ["5,679", "355,115", "290,190", "78,90", "100,544", "14,34", "650,680"]
    results, current, peak, elapsed = api(n, m, special_points)
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    print(f"Time elapsed: {elapsed}s")
 

if __name__ == "__main__":
    main()
