import gzip
import sys

def cut_gzipfile(infile,outfile,line_num):
    """
    Extract 'line_num' lines of contents from 'infile'
    and write that to 'outfile'.

    Parameters
    -----------
    infile : file name to be input
    outfile : file name to be newly created
    line_num : number of line to be extracted from 'infile'
    """
    with gzip.open(infile,'rt','utf-8') as ingzip:
        with gzip.open(outfile,'wt') as outgzip :

            for _ in range(0,line_num):
                line_str = ingzip.readline()
                outgzip.write(line_str)

            print("Check 'outfile' you specified. : ", outfile)

if __name__ == '__main__':
    # you can specify 'infile','outfile','line_num' as command-line argument.
    print(sys.argv)
    if len(sys.argv) != 4:
        print("You should specify 'infile', 'outfile', 'line_num ' as "\
                "command line argument!")
        quit()
    infile = sys.argv[1]
    outfile = sys.argv[2]
    line_num = int(sys.argv[3])
    print(infile,outfile,line_num)
    cut_gzipfile(infile=infile,outfile=outfile,line_num=line_num)
    # Check 'outfile' your specified
