import sys

filename = "AP_sub"

if len(sys.argv) == 2:
    filename = sys.argv[1]

inpath = "./data/Aminer/" + filename + ".txt"
outpath = "./data/Aminer/" + filename + ".tsv"

TAB = "\t"
print("Opening files...")
with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    print("Files opened...")

    print("Reading input file..")
    lines = infile.readlines()
    print("Read.. Parsing..")

    for line in lines:
        if len(line) < 2:
            outfile.write("\n")
            continue
        if line[1] == "i":
            outfile.write(line[7:].strip() + TAB)
        if line[1] == "*":
            outfile.write(line[3:].strip() + TAB)
        if line[1] == "@":
            outfile.write(line[3:].strip() + TAB)
        if line[1] == "t":
            outfile.write(line[3:].strip() + TAB)
        if line[1] == "c":
            outfile.write(line[3:].strip() + TAB)
        if line[1] == "%":
            outfile.write(line[3:].strip() + ",")
        if line[1] == "!":
            outfile.write(TAB + line[3:].strip())

    print("Parsing complete. Output filename: " + filename + ".tsv")
