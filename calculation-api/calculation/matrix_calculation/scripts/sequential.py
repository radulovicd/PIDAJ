import tracemalloc
import math
import time

def calcualte_distance(matrix_point, special_point):
    return math.sqrt((matrix_point[0] - special_point[0])**2 + (matrix_point[1] - special_point[1])**2)

def get_distances(matrix_point, special_points):
    distance_list = []
    for point in special_points:
        distance_list.append(calcualte_distance(matrix_point, point))
    return distance_list

def find_nearest(matrix_point, special_points):
    distance_list = get_distances(matrix_point, special_points)
    minValue = distance_list[0]
    minIdx = 0
    index = -1

    for value in distance_list:
        index += 1
        if value < minValue:
            minIdx = index
            minValue = value

    return minIdx

def generate_points(rows, cols):
    point_list = []
    for i in range(rows):
        for j in range(cols):
            point_list.append((i, j))
    return point_list

def compute(rows, cols, special_points):
    nearest_distances = []
    for point in generate_points(rows, cols):
        nearest_distances.append(find_nearest(point, special_points))
    return nearest_distances

def cast_points(special_points):
    casted = []
    for point in special_points:
        point = point.split(",")
        casted.append((int(point[0]), int(point[1])))
    return casted

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
