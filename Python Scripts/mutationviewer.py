import csv 
import operator 

outfile=open('relevantmutations.csv', 'w')
with open('mutations.csv', 'r') as infile: 
	reader=csv.reader(infile, delimiter= ';')
	header= next(reader)
	for row in reader:
		Position=row[0]
		AA_mutation=row[2]
		Count=row[4]
		Type=row[5]
		line='{},{},{},{}\n'.format(Position, AA_mutation, Count, Type)
		if Type=='Substitution - Missense':
			outfile.write(line)
outfile.close()

with open('relevantmutations.csv', 'r') as input_file:
	reader=csv.reader(input_file)
	sorted_data=sorted(reader, key=lambda row: int(row[2]), reverse=True)

with open('orderedrelevantmutations.csv', 'w', newline= '') as output_file:
	writer=csv.writer(output_file)
	for row in sorted_data: 
		writer.writerow(row)

with open('orderedrelevantmutations.csv', 'r') as inputfile:
	reader=csv.reader(inputfile)

	with open('NHE_family_COSMIC_data.txt', 'a') as outputfile: 
		for row in reader: 
			outputfile.write(', '.join(row)+ '\n')

























