import sys

inpath = "./data/kosarak/kosarak_sub.dat"
outpath = "./data/kosarak/kosarak_sub.arff"

if len(sys.argv) == 3:
    inpath = sys.argv[1]
    outpath = sys.argv[2]

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    
    print("Reading file...")
    lines = infile.read().splitlines();

    print("Parsing...")
    max_num = 0
    out_string = []
    for line in lines:
        out_string_sub = "{"
        for element in sorted(set(map(int, line.split(' ')))):
            max_num = max(max_num, element)
            out_string_sub += str(element - 1) + " 1, " 
        out_string_sub = out_string_sub[:-2] + "}\n"
        out_string.append(out_string_sub)

    print("Coverting to arff...")

    # write arff header
    print("Writing header...")
    outfile.write("@RELATION kosarak\n")
    for x in range(1, max_num + 1):
        outfile.write("@ATTRIBUTE id" + str(x) + " {0, 1}\n")

    # write data
    print("Writing data..")
    outfile.write("@DATA\n")
    for out_line in out_string:
        outfile.write(out_line)

    print("Done parsing, closing files...")
