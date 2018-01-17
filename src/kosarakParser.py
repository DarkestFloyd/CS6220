import sys

inpath = "./data/kosarak/kosarak_sub.dat"
outpath = "./data/kosarak/kosarak_sub.arff"

if len(sys.argv) == 3:
    inpath = sys.argv[1]
    outpath = sys.argv[2]

MAX_VALUE = 10 # 41270

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    
    print("Reading file...")
    lines = infile.read().splitlines();

    print("Coverting to arff...")

    # write arff header
    outfile.write("@RELATION kosarak\n\n")
    for x in range(1, MAX_VALUE + 1):
        outfile.write("@ATTRIBUTE id" + str(x) + " NUMERIC\n")

    # write data
    outfile.write("\n@DATA\n")
    for index in range(len(lines)):
        ints = list(map(int, lines[index].split()))
        outfile.write("{")
        for val in ints[:-1]:
            outfile.write(str(val - 1) + " " + "1,")
        outfile.write(str(ints[-1] - 1) + " " + "1")
        outfile.write("}\n")

    print("Done parsing, closing files...")
