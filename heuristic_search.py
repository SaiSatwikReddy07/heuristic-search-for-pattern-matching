def heuristic_search(pattern, sequence):
    """
    Perform heuristic search to find the given pattern in the given sequence.
    """
    # Initialize variables to track the current position in the sequence and the
    # number of mismatches between the pattern and the current substring of the
    # sequence.
    pos = 0
    mismatches = 0   
    # Iterate over the sequence, one character at a time.
    while pos < len(sequence):
        # If the current character in the pattern and the current character in
        # the sequence match, move on to the next character in both the pattern
        # and the sequence.
        if pattern[mismatches] == sequence[pos]:
            mismatches += 1
            pos += 1
        else:
            # If there is a mismatch, move to the next character in the sequence
            # but reset the number of mismatches to zero.
            mismatches = 0
            pos += 1       
        # If we have reached the end of the pattern, we have found a match.
        if mismatches == len(pattern):
            return pos - mismatches    
    # If we reach the end of the sequence without finding a match, return -1.
    return -1
# Search for the pattern "ATG" in the sequence "ATGCATGCATG".
result = heuristic_search("ATG", "ATGCATGCATG")
print(result)  # Output: 0
# Search for the pattern "TGC" in the sequence "ATGCATGCATG".
result = heuristic_search("TGC", "ATGCATGCATG")
print(result)  # Output: 1
# Search for the pattern "AGC" in the sequence "ATGCATGCATG".
result = heuristic_search("AGC", "ATGCATGCATG")
print(result)  # Output: -1