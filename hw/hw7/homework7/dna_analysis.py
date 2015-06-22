# Name: Hannah Krager
# Foundations II: Python
# Homework 7: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G, C, A and T nucleotides seen so far.
g_count = 0
c_count = 0
a_count = 0
t_count = 0


# for each relevant nucleotide in the string,
for n in seq:
    # increment the total number of n(nucleotides) we've seen
    total_count = total_count + 1
    #count individual A, G, T and C
    if n == 'C':
        c_count += 1
    elif n == 'G':
        g_count += 1
    elif n == 'A':
        a_count += 1
    elif n == 'T':
        t_count += 1


#Calculations performed here:

#add the values of each a, t, c and g count
sums = a_count + t_count + g_count + c_count
# divide the sum of g and c counts by the sums of the individual counts
gc_content = float((c_count + g_count) / sums)
# divide the sum of a and c counts by the sums of the individual counts
at_content = float((a_count + t_count) / sums)
#calculate the at/gc ratio
at_gc = float((a_count + t_count)/(g_count + c_count))


#classify low/moderate/high for gc content based on given parameters
if gc_content < .4:
    classification = 'low GC content'
elif gc_content > .6:
    classification = 'high GC content'
else:
    classification = 'moderate GC content'

# Print the answers
print('GC-content:', gc_content)
print('AT-content:', at_content)
print('G count:', g_count)
print('C count:', c_count)
print('A count:', a_count)
print('T count:', t_count)
print('Sum count:', sums)
print('Total count:', total_count)
print('seq length:', len(seq))
print('AT/GC Ratio:', at_gc)
print('GC Classification:', classification)
