#!/usr/bin/env python3

import sys

def kmer(genome, k):
  """
  This function identify all k-mer of size k from the genome 
  and return all unique possible subsequent k-mer of each k-mer.
  
  Arguments:
    genome (string): sequenced genome
    k (int): size of substrings
  
  Return:
    dict: All substrings of size k and all unique possible subsequent substrings of each substring.
  """
  nuc = []
  out = {}
  # get all the substring of size k and save it to a list
  for i in range(len(genome)-(k-1)):
    sub = genome[i:i+k]
    nuc.append(sub)
  
  # remove duplicate in a list
  uniq_nuc = list(set(nuc))
  
  # create a dict with each unique substring as the key and the values are the possible subsequent substrings
  for n in nuc:
    # create new key from the given unique substring with empty list as the value
    if not (n in out.keys()):
      out[n]=[]
      # look for possible subsequent substrings and append it to the value list
      for u in uniq_nuc:
        if n[-k+1:] == u[0:k-1]:
          out[n].append(u)
  return out

def all_kmer(filename, k):
  """
  This function identify all k-mer of size k from the genome fragments read from a file.
  and return all unique possible subsequent k-mer of each k-mer.
  
   Arguments:
    filename (string): File of genome fragments
    k (int): size of substrings
  
  Return:
    dict: All substrings of size k and all unique possible subsequent substrings of each substring.
  """
  res = {}
  
  # read genomes from a file
  with open(filename, "r") as f:
    # read the genome fragments line by line 
    genome = f.readlines()
    for g in genome:
      # remove \n of each line
      g = g.replace('\n','')
      # get all k-mer of size k from the genome and return all unique possible subsequent k-mer of each k-mer
      out = kmer(g, k)
      
      # save the result in one big dict
      for o in out:
        # if the key already exist, combine their values
        if o in res.keys():
          temp = res[o] + out[o]
          # remove duplicates in the value
          res[o] = list(set(temp))
        else:
          res[o] = out[o]
    f.close()
    return res

def one_k(filename):
  """
  This function returns the smallest value of k where every substring has only one possible substring that follows it.
  
  Arguments:
    genome (string): sequenced genome
    
  Return:
    int: smallest k where every substring has only one possible substring that follows it
  """
  genome = ""
  with open(filename, "r") as f:
    # read the genome fragments line by line 
    lines = f.readlines()
    for l in lines:
      # remove \n of each line
      l = l.replace('\n','')
      genome = genome + l
      
  # look for all kmer from length 2 to len(genome)-1
  for i in range(2, len(genome)):
    # get all k-mer of size k from the genome and return all unique possible subsequent k-mer of each k-mer
    out = kmer(genome, i)
    
    # variable to indicate, if every substring has only one possible substring that follows it
    ind = True
    
    # check for every subsequent values if they only has one possible substring
    for k in out:
      if not (len(out[k]) == 1):
        ind = False
        break
    if ind:
      return i
  return 0

if __name__ == "__main__":
  file = sys.argv[1]
  k = one_k(file)
  print(k)
  
