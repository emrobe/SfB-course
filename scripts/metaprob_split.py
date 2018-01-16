import argparse, HTSeq, collections, os

parser = argparse.ArgumentParser(description="Splits raw fastq files into clusters calculated by MetaProb. Provide -a and --aa for single end fastq, add --b --bb for paired end fastq. Output is written to output/")
parser.add_argument('--a', help="R1 fastq", type=str)
parser.add_argument('--b', help="R2 fastq",  type=str)
parser.add_argument('--aa', help="R1 clusters", type=str)
parser.add_argument('--bb', help="R2 clusters", type=str)
args = parser.parse_args()

if not args.a and args.aa:
	exit("Please specify at least one R1 fastq and clusters file!")

def parse(fastq, clustersfile):
	#Parse clusters
	data = collections.defaultdict(int)
	data = {}
	clusters = {}
	with open(clustersfile, "r") as f:
		for line in f:
			(key, val) = line.strip().split(",")
			clusters[str(key)] = int(val)
	#Parse fastq
	for read in HTSeq.FastqReader(fastq):
		accession = read.name.strip().split()
		accession = '@'+accession[0]
		if accession in clusters:
			if clusters[accession] not in data:
				data[clusters[accession]] = []
			else:
				data[clusters[accession]].append(read)

	# Create output folder, prefix filenames
	if not os.path.isdir(os.path.join(os.getcwd(), "output")):
		os.makedirs("output")
	prefix = fastq.split(".")
	prefix = prefix[0]

	# Iterate through clusters and print files
	for cluster, reads in data.iteritems():
		with open (os.path.join("output", prefix+'.'+str(cluster)+".fastq"),"w") as f:
			reads = sorted(reads)
			for read in reads:
				read.write_to_fastq_file(f)

parse(args.a, args.aa)

if args.b and args.bb:
	parse(args.b, args.bb)
