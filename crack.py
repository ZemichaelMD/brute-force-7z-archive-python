import os,sys
from itertools import combinations

f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[1]),'r')
lines = f.read().splitlines()
print(lines)

list_combinations = []
list_combination_words = []
for L in range(len(lines) + 1):
	for i in range(L):	list_combinations.append(list(combinations(lines, i)))
for list_combination in list_combinations:
	for combination in list_combination:
		list_combination_words.append(''.join(combination))

for password in list_combination_words:
	x = os.system('7z e {0} -p{1}'.format(sys.argv[2],password))
	if x == 0:
		print('[~] Password is : {0}\n\n'.format(password))
		exit(1)

print( '[!] Password not found in the provided list!\n\n')