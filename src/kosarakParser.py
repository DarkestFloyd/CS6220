import sys

inpath = "./data/kosarak/kosarak_sub.dat"
outpath = "./data/kosarak/kosarak_sub.arff"

if len(sys.argv) == 3:
    inpath = sys.argv[1]
    outpath = sys.argv[2]

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    
    print("Reading file...")
    lines = infile.read().splitlines();

    max_num = 0
    out_string = ""
    for line in lines:
        out_string += "{"
        for element in set(map(int, line.split(' '))):
            max_num = max(max_num, element)
            out_string += str(element - 1) + " 1, " 
        out_string = out_string[:-2] + "}\n"

    print("Coverting to arff...")

    # write arff header
    print("Writing header...")
    outfile.write("@RELATION kosarak\n")
    for x in range(1, max_num + 1):
        outfile.write("@ATTRIBUTE id" + str(x) + " {0, 1}\n")

    # write data
    print("Writing data..")
    outfile.write("@DATA\n")
    outfile.write(out_string)

    print("Done parsing, closing files...")
