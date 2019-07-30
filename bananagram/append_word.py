import sys
from tqdm import tqdm

def main():
	arguments = sys.argv
	words = arguments[1:]
	f=open("ordlista.txt", "a+")
	for word in tqdm(words):
		f.write("\n"+word)

	f.close()
	print("Done")




if __name__ == "__main__":
	main()