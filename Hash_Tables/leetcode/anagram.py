# WRITE GROUP_ANAGRAMS FUNCTION HERE #
#                                    #
#                                    #
#                                    #
#                                    #
######################################

def group_anagrams(strings):
    anagrams_group = {}
    for word in strings:
        key = "".join(sorted(word))
        
        if key in anagrams_group:
            anagrams_group[key].append(word)
            
        else:
            anagrams_group[key] = [word]
    return list(anagrams_group.values())
        
    


print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""