g = open('SVDpp1.txt', 'w')
with open('data/qual.dta.predict', 'r') as f:
	f.readline()
	f.readline()
	f.readline()
	while(True):
		try:
			line = f.next()
			line = line.split()
			if len(line) == 3:
				g.write(line[2] + "\n")
		except StopIteration:
			break
g.close()

