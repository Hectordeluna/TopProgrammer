def main():

	num = int(raw_input())

	notmirror = ["Q","E","R","P","S","D","F","G","J","K","L","Z","C","B","N"]

	for i in range(0,num):

		error = 0
		word = raw_input()


		rvs = word[::-1]

		for l in notmirror:

			if l in word:
				error = 1
				



		if rvs == word and error == 0:
			print ("YES")
		else:
			print ("NO")

if __name__ == "__main__":
	main()