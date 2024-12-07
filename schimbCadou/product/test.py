# def transform_data(data):
# 	return {k: v*2 for k,v in data.items() if v % 2 == 0}
#
# def compute_result(data):
# 	transformed = transform_data(data)
# 	return sum(map(lambda x: x**2, transformed.values()))
#
# def main():
# 	data = {'a':1, 'b':2,'c':3,'d':4}
# 	return compute_result(data)
#
# result = main()
# print(result)

# def process_list(lst):
# 	return [x**2 for x in lst if x%2==0]
#
# def main():
# 	numbers = [1,2,3,4,5]
# 	processed = process_list(numbers)
# 	processed.sort(reverse=True)
# 	return sum(processed)
#
# result = main()
# print(result)

# def filter_and_sum(lst):
# 	filtered = [x for x in lst if x % 3 == 0]
# 	doubled = list(map(lambda x: x * 2, filtered))
# 	return sum(doubled)
#
#
# def main():
# 	data = [10, 15, 20, 25, 30]
# 	return filter_and_sum(data)
#
#
# result = main()
# print(result)

# def emphasize(func):
# 	def wrapper(*args, **kwargs):
# 		result = func(*args,**kwargs)
# 		return f"**{result}**"
# 	return wrapper
#
# @emphasize
# def greet(name):
# 	return f"Hello, {name}!"
#
# def main():
# 	message  = greet("Horia")
# 	print(message)
#
# if __name__ == "__main__":
# 	main()

def compute_difference(lst):
	even_sum = sum (x for x in lst if x % 2 == 0 )
	odd_product = 1
	for x in lst:
		if x % 2 != 0:
			odd_product *= x
	return even_sum - odd_product

def main():
	data = [2,3,4,5,6]
	return compute_difference(data)

result = main()
print(result)