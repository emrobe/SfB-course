import os, sys, subprocess
from Bio import SeqIO
from Bio.Seq import Seq
import shlex
#import HTSeq

# Path to 'hmmsearch' binary
HMMSEARCH = 'hmmsearch'

path = '/'.join(sys.argv[0].split('/')[:-1])
BACTERIA_FWD_16S = os.path.join(path, 'hmm/16s_bact_for3.hmm')
BACTERIA_REV_16S = os.path.join(path, 'hmm/16s_bact_rev3.hmm')
ARCHAEA_FWD_16S = os.path.join(path, 'hmm/16s_arch_for3.hmm')
ARCHAEA_REV_16S = os.path.join(path, 'hmm/16s_arch_rev3.hmm')
BACTERIA_FWD_23S = os.path.join(path, 'hmm/23s_bact_for3.hmm')
BACTERIA_REV_23S = os.path.join(path, 'hmm/23s_bact_rev3.hmm')
ARCHAEA_FWD_23S = os.path.join(path, 'hmm/23s_arch_for3.hmm')
ARCHAEA_REV_23S = os.path.join(path, 'hmm/23s_arch_rev3.hmm')
BACTERIA_FWD_5S = os.path.join(path, 'hmm/5s_bact_for3.hmm')
BACTERIA_REV_5S = os.path.join(path, 'hmm/5s_bact_rev3.hmm')
ARCHAEA_FWD_5S = os.path.join(path, 'hmm/5s_arch_for3.hmm')
ARCHAEA_REV_5S = os.path.join(path, 'hmm/5s_arch_rev3.hmm')


def do_search(awk, inp, profile, matches, do_trim=True, reverse=False, cpu=1):
	### Do HMM search
	#If input is fastq, use awk to translate and pipe to hmmer. Sets inp to '-'
	if args.f:
		command1 = awk+inp
		fastq = subprocess.Popen(command1, shell=True, universal_newlines=True,  stdout = subprocess.PIPE)
		inp = '-'
	cmd = '{3} --cpu {2} --notextw -E 10E-5 --noali {1} {0}'
	cmd = cmd.format(inp, profile, cpu, HMMSEARCH)
	command2 = shlex.split(cmd)
	sys.stdout.flush()

	#If fastq, pipe from file->awk->hmmer. Else, pipe from file->hmmer.
	if args.f:
		pipe = subprocess.Popen(command2, universal_newlines=True, stdin=fastq.stdout, stdout=subprocess.PIPE)
	else:
		pipe = subprocess.Popen(command2, universal_newlines=True, stdout = subprocess.PIPE)

	out = pipe.communicate()
	lines = out[0].splitlines()
	for i in range(len(lines)):
		line = lines[i]
		if line[0:3] == '>> ':
			skip_symbols = ('', '..', '[.', '.]', '[]')
			val = lines[i+3].strip().split(' ')
			val = [v for v in val if (v not in skip_symbols)]
			if int(val[7])-int(val[6]) < 100:
				continue
			pos1 = int(val[8])
			pos2 = int(val[9])
			matches[line.strip()[3:].replace('  ', ' ')] = (pos1, pos2, reverse)

def extract_sequences(matches, inp, do_trim=True, fastq=True):		
	# Extract matching sequences from input fasta file
	if not fastq:
		filetype='fasta'
	else:
		filetype='fastq'
	file = open(inp, 'r')
	matching_headers = matches.keys()
	for rec in SeqIO.parse(file, filetype):
		if rec.description in matching_headers:
			matching_headers.remove(rec.description)
			reverse = matches[rec.description][2]
			print '>'+rec.description
			if not do_trim:
				if reverse:
					print rec.seq.reverse_complement().tostring()
				else:
					print rec.seq.tostring()
			elif do_trim:
				pos1 = matches[rec.description][0]
				pos2 = matches[rec.description][1]
				if reverse:
					print rec.seq.reverse_complement().tostring()[pos1-1:pos2]
				else:
					print rec.seq.tostring()[pos1-1:pos2]

### Add method to substract matches in fastq file
def substract (matches, inp, fastq=False):
	if not fastq:
                filetype='fasta'
        else:
                filetype='fastq'
	file = open(inp, 'r')
	for rec in SeqIO.parse(file, filetype):
		if rec.description in matches:
			continue
		print(rec.format(filetype))

if __name__ == '__main__':
	import argparse
	
	parser = argparse.ArgumentParser()
	parser.add_argument('input', help="Input FASTA/FASTQ file", type=str)
	parser.add_argument('-f', help="Fastq as input (Default=fasta)", action="store_true")
	parser.add_argument('-s', help="Output fastq/fasta with rRNA sequences substracted (Default=Extract 16S sequences as fasta)", action="store_true")
	parser.add_argument('-a', help="Only screen for archaeal 16S rRNA (Default=5S, 16S, 23S)", action="store_true")
	parser.add_argument('-b', help="Only screen for bacterial 16S rRNA (Default=5S, 16S, 23S)", action="store_true")
        parser.add_argument('-c', help="Only screen for 16S rRNA (Default=5S, 16S, 23S)", action="store_true")
	parser.add_argument('-t', help="Trim sequences to regions matching rRNA sequences", action="store_true")
	parser.add_argument('-n', help="Number of CPUs to use", type=int, default=1)
	parser.add_argument('-o', help="Output file name (Extracted 16S sequences (default) will be fasta, substracted (-s) will be same as input filetype (-f))", nargs=1, type=str)
	args = parser.parse_args()
	
	if args.o:
		f = open(args.o[0], 'w')
		sys.stdout = f
		
	matches = {}
	awk = """awk '{if(NR%4==1) {printf(">%s\\n",substr($0,2));} else if(NR%4==2) print;}' """
	
	if args.a and not args.b:
		do_search(awk, args.input, ARCHAEA_FWD_16S, matches, cpu=args.n)
		do_search(awk, args.input, ARCHAEA_REV_16S, matches, reverse=True, cpu=args.n)
	elif args.b and not args.a:
		do_search(awk, args.input, BACTERIA_FWD_16S, matches, cpu=args.n)
		do_search(awk, args.input, BACTERIA_REV_16S, matches, reverse=True, cpu=args.n)
	elif not args.a and not args.b and args.c:
		do_search(awk, args.input, ARCHAEA_FWD_16S, matches, cpu=args.n)
		do_search(awk, args.input, ARCHAEA_REV_16S, matches, reverse=True, cpu=args.n)
		do_search(awk, args.input, BACTERIA_FWD_16S, matches, cpu=args.n)
		do_search(awk, args.input, BACTERIA_REV_16S, matches, reverse=True, cpu=args.n)
	else:
		do_search(awk, args.input, ARCHAEA_FWD_16S, matches, cpu=args.n)
                do_search(awk, args.input, ARCHAEA_REV_16S, matches, reverse=True, cpu=args.n)
                do_search(awk, args.input, BACTERIA_FWD_16S, matches, cpu=args.n)
                do_search(awk, args.input, BACTERIA_REV_16S, matches, reverse=True, cpu=args.n)	
                do_search(awk, args.input, ARCHAEA_FWD_23S, matches, cpu=args.n)
                do_search(awk, args.input, ARCHAEA_REV_23S, matches, reverse=True, cpu=args.n)
                do_search(awk, args.input, BACTERIA_FWD_23S, matches, cpu=args.n)
                do_search(awk, args.input, BACTERIA_REV_23S, matches, reverse=True, cpu=args.n)
                do_search(awk, args.input, ARCHAEA_FWD_5S, matches, cpu=args.n)
                do_search(awk, args.input, ARCHAEA_REV_5S, matches, reverse=True, cpu=args.n)
                do_search(awk, args.input, BACTERIA_FWD_5S, matches, cpu=args.n)
                do_search(awk, args.input, BACTERIA_REV_5S, matches, reverse=True, cpu=args.n)

	if args.s:
		substract(matches, args.input, args.f)
	else:
		extract_sequences(matches, args.input, args.t, args.f)
	if args.o:
		sys.stdout.flush()
		f.close()






