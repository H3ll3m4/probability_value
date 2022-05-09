from collections import namedtuple
import random 


value_probability = namedtuple('value_probability',['value', 'probability'])

def return_value_with_probability(*args):
	'''
	Function that returns a random value picked out of a pre-defined set, with an associated probability
	Conform to interface defined : 	func( (1, 0.6), (3, 0.4) ) return the value 1 with 60% probability, or the value
	3 with 40% probability
	'''
	sequence = list()
	weights_list = list()
	for arg in args:
		sequence.append(arg[0])
		weights_list.append(arg[1])
	result_number = 1
	# We could create a set with 6x1 and 4x 3 and randomly choose one of them
	# Get some inspiration of random : https://github.com/python/cpython/blob/main/Lib/random.py
	result = random.choices(sequence,weights = weights_list,k = result_number)
	return result[0]

def return_value(proportions):
	'''
	Function that returns a random value picked out of a pre-defined set, with an associated probability. 
	'''
	sequence = list()
	weights_list = list()
	for proportion in proportions:
		sequence.append(proportion[0])
		weights_list.append(proportion[1])
	result_number = 1
	result = random.choices(sequence,weights = weights_list,k = result_number)
	return result[0]


def main():
	#An example to return one value depending on probabilities defined
	result = return_value_with_probability((8, 0.2), (43, 0.2), (56, 0.6))
	print(result)

	#An example to run a series of experiments
	results = list()
	vp1 = value_probability(1, 0.6)
	vp2 = value_probability(3, 0.4)
	experiments_number = 10000
	for i in range(experiments_number):
		result = return_value_with_probability(vp1,vp2)
		results.append(result)
	count1 = 0
	count2 = 0
	for element in results:
		if element == vp1.value:
			count1 += 1
		if element == vp2.value:
			count2 += 1
	print(count1)
	print(count2)



if __name__ == "__main__":
	main()
