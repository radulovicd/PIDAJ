import math
import tracemalloc

def generate(n):
	list = []
	for i in range(1, n + 1):
		list.append(i)
	return list

def is_prime(x):
	for i in range(0, int(math.sqrt(x)) + 1):
		if i < 2:
			continue
				
		if x % i == 0:
			return False
	return True

def primes(list):
	primes = []
	for x in list:
	
		if x < 2:
			continue
			
		if is_prime(x):
			primes.append(x)
			
	return primes

def hex_list(list):
	hexlist = []
	
	for x in list:
		hexlist.append(hex(x))
		
	return hexlist

def hex_dictionary(list):
	dictionary = {}
	for x in list:
		for s in x[2:]:
			if s in dictionary:
				dictionary[s] += 1
			else:
				dictionary[s] = 1
	
	return dictionary	

def main():
	list = generate(1000000)
	list = primes(list)
	tracemalloc.start()
	list = hex_list(list)
	current, peak = tracemalloc.get_traced_memory()
	print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
	tracemalloc.stop()
#	dict = hex_dictionary(list)

if __name__ == "__main__":
	main()
