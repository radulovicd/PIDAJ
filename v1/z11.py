import math
import tracemalloc

def generate(n):
	return (i for i in range(1, n + 1))

def is_prime(x):
	for i in range(0, int(math.sqrt(x)) + 1):
		if i < 2:
			continue
				
		if x % i == 0:
			return False
	return True

def primes(list):
	return (x for x in list if x > 2 and is_prime(x))

def hex_list(list):
	return (hex(x) for x in list)

def hex_dictionary(list):
	dictionary = {}
	for x in list:
		for s in x[2:]:
			dictionary[s] = dictionary[s] + 1 if s in dictionary else 1
	
	return dictionary	

def main():
	list = generate(1000000)
		
	list_primes = primes(list)
	tracemalloc.start()
	list_hex = hex_list(list_primes)
	current, peak = tracemalloc.get_traced_memory()
	print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
	tracemalloc.stop()
	dict = hex_dictionary(list_hex)

if __name__ == "__main__":
	main()
