# Here's my solution. I was given string "s".
# s="abcabcabcabc"

# From s I build an array of possible substrings
# possible_substrings = ["a","ab","abc","abca","abcab","abcabc"]

# For each possible substring, I checked if it was valid.
# valid_substrings = ["abc","abcabc"]

# Then I found the number of times each valid substring appeard in s
# valid_substring_freq = [4, 2]

# The solution is the greatest number of times a valid substring appears!
# solution = 4

def answer(s): 
    # 1. Create list of all present sub strings.
    
    # From s="abcabcabcabc" we would get:  
    # "a", "ab", "abc", "abca", "abcab", "abcabc"...
    # The longest substring (fewest slices, excluding 0)
    # Would be half the length of the array, (2 slices).
    possible_substrings = []
    number_possible_substrings = int( len(s)/2 ) + 1
    # So for 1/2 length of s, create an array of substrings 
    for i in range(1, number_possible_substrings):
        substring = s[0:i]
        possible_substrings.append(substring)
        
    # Now that we know all present substrings
    # we need to figure out which ones are valid solutions.
    
    # For a substring to be a valid solution
    # the substring must repeat for the entire 
    # length of s. Ex. "abc" -> "abcabcabcabc"
    
    # Working our way through s (0, end) let compare
    # each possible substring to the next substring of 
    # equal length. Valid substrings will repeat for 
    # the entire length of s.
    valid_substrings = []
    for substring in possible_substrings:
        substring_length = len(substring)
        for i in range(substring_length, int(len(s)), substring_length):
            cake_slice = s[i-substring_length:i]
            # Compare each slice to current substring
            if cake_slice == substring: # A match!
                if i+substring_length == len(s): # If the patter repeats for whole length of s, it is valid!
                    valid_substrings.append(substring)
                continue
            elif cake_slice != substring: # No match!
                break

    # Phew! Now, we have a list of valid substrings.
    # So from s="abcabcabcabc" we found "abc" and "abcabc"
    # Now figure out how often each substring occurs
    valid_substring_freq = []
    for valid_substring in valid_substrings:
        freq = s.count(valid_substring)
        valid_substring_freq.append(freq)
    
    # We found "abc" appears 4 times, "abcabc" appears 2 times.
    # valid_substring_freq = [4, 2]
    # The solution is the greatest number of times a valid substring appears!
    if len(valid_substring_freq) == 0:
        solution = 1
    else:
        solution = max(valid_substring_freq)
    
    return solution

cases = ["abcabcabcabc", "abccbaabccba", "abcabcabcab"]

for s in cases:
    a = answer(s)
    print(s)
    print(a)
