import tracemalloc
import math
import time

def calcualte_distance(matrix_point, special_point):
    return math.sqrt((matrix_point[0] - special_point[0])**2 + (matrix_point[1] - special_point[1])**2)

def get_distances(matrix_point, special_points):
    return [calcualte_distance(matrix_point, point) for point in special_points]

def find_nearest(matrix_point, special_points):
    return min(enumerate(get_distances(matrix_point, special_points)), key=lambda point: point[1])[0]

def generate_points(rows, cols):
    return [(i, j) for i in range(rows) for j in range(cols)]

def compute(rows, cols, special_points):
    return [find_nearest(point, special_points) for point in generate_points(rows, cols)]

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
