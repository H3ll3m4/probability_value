import random_val_probability as rvp
import pytest


testcases = [
				((1, 0.6), (3, 0.4)),
				((8, 0.2), (43, 0.2), (56, 0.6),),
			]

@pytest.mark.parametrize("proportions",testcases)
def test_return_probability(proportions):
	results = list()
	# What level of type 1 α error we want
	type1error = 0.01 
	# Sample size calculation if we want power = 1−β = 99%
	# https://www.stat.ubc.ca/~rollin/stats/ssize/b2.html 
	# for 2 independant samples with one degree of freedom. 
	# nb_tests = 114853 # Not sufficient for 2 degrees of freedom
	# https://academic.oup.com/ndt/article/25/5/1388/1842407
	# Calculations are different for non binomial case, ie with more than two outcomes. 
	nb_tests = 1000000

	for i in range(nb_tests):
		result = rvp.return_value(proportions)
		results.append(result)
	count = dict()
	for tuple in proportions:
		count[tuple] = 0

	for element in results:
		for tuple in proportions:
			if element == tuple[0]:
				count[tuple] += 1

	for tuple in proportions:
		accepted_min = tuple[1]*nb_tests*(1-type1error)
		accepted_max = tuple[1]*nb_tests*(1+type1error)
		assert count[tuple] <= accepted_max and count[tuple] >= accepted_min





