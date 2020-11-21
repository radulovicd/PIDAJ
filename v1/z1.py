import math

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

def main():
	list = generate(30)
	print(list)
	list = primes(list)
	print(list)
	list = hex_list(list)
	print(list)
	

if __name__ == "__main__":
	main()
