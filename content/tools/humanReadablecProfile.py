"""
    Python Script Profile Output Sorter

    Takes the output of cProfile (generated by running the profile.sh script)
    and generates a human readable .txt file from it. 

    Used on a per script basis, the output of cProfile is piped into this, which 
    generates the final output file for the profiled Python files. 


    USAGE

    Should never need to be called independtly of the main profiling script, however;
    The output file from cProfile should be piped to this, and it will generate a 
    human readable table sorted by the cumulative time used for each method called,
    highest to lowest time used. 
    This overwrites / replaces the non-human readable file it was passed, as it uses 
    the input file name as the output file name. This is to reduce the amount of clutter
    generated, and ultimately because this will be incorporated into a Feedback.py style 
    script which is run for the CMEE Miniprojects.

    Example:
    E.G. GOES HERE

    ARGUMENTS 

    --inputFile : name of the input file. Likely to be a .txt file, of the same name as the script
                    that you wished to profile. 
"""

import sys, subprocess, os, csv, argparse, re, time, pstats

parser = argparse.ArgumentParser("Generates human readable output from cProfile, used on each of the CMEE Miniproject .py files, for projcts which ran over 10 minutes")
parser.add_argument("-f", "--inputFile", required=True, help="input text (.txt) file generated by cProfile -o argument")
args = parser.parse_args()

# send the stats to an output file next
#   file of same name as input, do some magic with a tmp file, deleted the original
#       then write out the human readable using its name

def GenerateOutput(cProfileLog):
    """
    Takes a .txt file generated by cProfile and creates a human readable version of it
    sorted by cumulative use. 

    ARGUMENTS 
    cProfileLog : input filename from sys.argv, should be a .txt file, with the same name as the profiled script
    """
    p = pstats.Stats(cProfileLog)
    p.sort_stats('cumulative')

    return p
    #then send that to a text file?

def main(argv):
    """
    Runs the GenerateOutput method on the given input. 

    ARGUMENTS 
    argv : input filename from sys.argv
    """
    #basename = os.path.basename(argv)
    output = GenerateOutput(argv)
    f = open(argv, "w")
    f.write(output)
    f.close




## probably want to write this as a module, with the 'if main' stuff
# that way it can be more easily used as just a little function on cmd line
if __name__ == "__main__":
    # if  len(sys.argv) < 1:
    #     print("No arguments given. Please give at least one cProfile log (.txt) file")
    # else:
    #     # check that a .txt file was given? 
    #     # ooh or could generate a dic of possible input file .txt names, and compare
    #     sys.argv.endswith()
    main(sys.argv)