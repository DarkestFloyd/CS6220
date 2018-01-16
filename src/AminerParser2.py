import sys

filename = "AP_sub"

if len(sys.argv) == 2:
    filename = sys.argv[1]

inpath = "./data/Aminer/" + filename + ".txt"
outpath = "./data/Aminer/" + filename + ".tsv"

TAB = "\t\t"
print("Opening files...")
with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
    print("Files opened...")

    print("Reading input file..")
    lines = infile.readlines()
    print("Read.. Parsing..")

    outfile.write("index\ttitle\tauthors\tyear\tvenue\trefs\tabs\n")

    index, title, authors, year = "NA", "NA", "NA", "NA"
    venue, refs, abstract = "NA", "NA", "NA"

    for line in lines:
        if len(line) < 2:
            for element in [index, title, authors, year, venue]:
                if not element:
                    element = "NA"
                outfile.write(element + TAB)
            if len(refs) > 2: 
                refs = refs[2:-1]
            outfile.write(refs + TAB + abstract + "\n")
            index, title, authors, year, venue = "NA", "NA", "NA", "NA", "NA"
            refs, abstract = "NA", "NA"
            continue
        if line[1] == "i":
            index = str(line[7:].strip())
        if line[1] == "*":
            title = line[3:].strip()
        if line[1] == "@":
            authors = line[3:].strip()
        if line[1] == "t":
            year = line[3:7].strip()
        if line[1] == "c":
            venue = line[3:].strip()
        if line[1] == "%":
            refs = refs + line[3:].strip() + ","
        if line[1] == "!":
            abstract = line[3:].strip()

    print("Parsing complete. Output filename: " + filename + ".tsv")
    print("Closing files...")
