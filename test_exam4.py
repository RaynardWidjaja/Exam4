from exam4 import *

def test_kmer():
  genome = "ATGTCTGTCTGAA"
  k = 2
  out = kmer(genome, k)
  assert ("AT" in out.keys() and "AA" in out["GA"] and "AA" in out["AA"])
  
def test_all_kmer():
  filename = "reads_mini.fa"
  k = 5
  out = all_kmer(filename, k)
  assert (out['CCATA'] == ['CATAT'] and "TAAAC" in out['TTAAA'] and "TAAAA" in out['TTAAA'])

def test1_one_k():
  genome = "ATGTCTGTCTGAA"
  assert one_k(genome) == 0

def test2_one_k():
  genome = "GACATTTGCTACA"
  assert one_k(genome) == 4
