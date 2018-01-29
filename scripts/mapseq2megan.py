#/usr/bin/python
import argparse, collections

parser = argparse.ArgumentParser(description='This script converts Mapseq formated results to MEGAN input')
parser.add_argument('input', help="Input file (Mapseq output file)", type=str)
parser.add_argument('-c', type=float, default=0.5, help="Confidence score threshold. (default 0.5)")
parser.add_argument('-u', type=int, default=0, help="Root count. Mapseq does not provide information of unclassified reads, however if you have counted this manually, you can provide it for more sensible visualization in MEGAN")
parser.add_argument('-f', action='store_true', help="Filter unassigned OTUs")
args = parser.parse_args()

data = collections.defaultdict(str)

# Iterator to return all lists in the data dictionary
def yield_all_lists(data):
	for k,v in data.items():
		yield tuple(v)

# Parse
with open(args.input) as handle:
	for line in handle:
		if line.startswith("#"):
			continue
		line = line.strip().split("\t")
		data[line[0]]= line[13:]

# Apply threshold cut off
for k,v in data.items():
	# Mapseq bug: The taxa B16S, and maybe others include an extra \t, which screws up strict x3 column output pr taxa while parsing. Perform quick fix.
	if len(v)%3 != 0:
		if args.f:
			index = v.index('')
			v = v[:index]
		else:
			v.remove('')
	for x, _ in enumerate(v):
		if x%3 == 0:
			if float(min(v[x+1], v[x+2])) >= args.c:
				if x == 0:
					data[k] = [v[x]]
				else:
					data[k].append(v[x])
# Print Krona format
krona = collections.Counter(yield_all_lists(data))
alltaxa = []
for k,v in krona.items():
	for taxa in k:
		alltaxa.append(taxa)
alltaxa = collections.Counter(alltaxa)
for k,v in alltaxa.items():
	print "{}\t{}".format(k,v)


if args.u is not 0:
	print "{}\t{}".format('root', args.u)
