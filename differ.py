import sys
import markov


def differ(chain1, chain2):


    intersection = set(chain1.keys()).intersection(set(chain2.keys())) 

    difference = set(chain1.keys()).difference(set(chain2.keys())) 

    print "Chains in text 1: %d" % len(chain1) 
    print "Chains in text 2: %d" % len(chain2)
    print "Pairs in both sets: %d" % len(intersection)
    print "Difference %d" % len(difference) 

    l = [len(chain1), len(chain2)]
    match_percentage = (float(len(intersection)) / max(l)) * 100
    print "Approx match percentage: %d" % match_percentage

    if match_percentage < 2:
        print "Your sets are too different, they may not mix well"
    elif match_percentage < 10:
        print "Could be fun"
    else:
        print "Your sets are very much alike"


def main():
    args = sys.argv

    input_text1 = args[1]
    input_text2 = args[2]

    corpus1 = markov.read_file(input_text1)
    corpus2 = markov.read_file(input_text2)

    chain_dict1 = markov.make_chains(corpus1)
    chain_dict2 = markov.make_chains(corpus2)

    diff = differ(chain_dict1, chain_dict2)


if __name__ == "__main__":
    main()