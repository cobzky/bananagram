import pandas as  pd
import sys
import itertools
from tqdm import tqdm

wordlist = pd.read_csv("ordlista.txt").iloc[:,0].values

def get_combinations(letters,number):
	res = list(itertools.combinations(letters,number))
	return res


def get_anagrams(letters):
	result = []
	res = list(itertools.permutations(letters))
	words = ["".join(list(k)) for k in res]
	for word in words:
		if word in wordlist:
			result.append(word)

	return result

def get_sub_anagrams(letters,number):
	combinations = get_combinations(letters,number)
	result = []
	print("Working through all combintations:")
	for combination in tqdm(combinations):
		result = result + get_anagrams(combination)
	print("Done!")

	return list(set(result))



def main():
	arguments = sys.argv
	letters = arguments[1]
	number = int(arguments[2])

	result = get_sub_anagrams(letters,number)
	print("Results:")
	for r in result:
		print(r)
	
if __name__ == "__main__":
	main()
