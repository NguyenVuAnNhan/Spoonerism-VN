import itertools

# Function to combine nucleus and diacritic into a single vowel with the correct tone mark
def combine_vowel(nucleus, diacritic):
    tone_marks = {
        'sắc': {'a': 'á', 'ă': 'ắ', 'â': 'ấ', 'e': 'é', 'ê': 'ế', 'i': 'í', 'o': 'ó', 'ô': 'ố', 'ơ': 'ớ', 'u': 'ú', 'ư': 'ứ', 'y': 'ý'},
        'huyền': {'a': 'à', 'ă': 'ằ', 'â': 'ầ', 'e': 'è', 'ê': 'ề', 'i': 'ì', 'o': 'ò', 'ô': 'ồ', 'ơ': 'ờ', 'u': 'ù', 'ư': 'ừ', 'y': 'ỳ'},
        'hỏi': {'a': 'ả', 'ă': 'ẳ', 'â': 'ẩ', 'e': 'ẻ', 'ê': 'ể', 'i': 'ỉ', 'o': 'ỏ', 'ô': 'ổ', 'ơ': 'ở', 'u': 'ủ', 'ư': 'ử', 'y': 'ỷ'},
        'ngã': {'a': 'ã', 'ă': 'ẵ', 'â': 'ẫ', 'e': 'ẽ', 'ê': 'ễ', 'i': 'ĩ', 'o': 'õ', 'ô': 'ỗ', 'ơ': 'ỡ', 'u': 'ũ', 'ư': 'ữ', 'y': 'ỹ'},
        'nặng': {'a': 'ạ', 'ă': 'ặ', 'â': 'ậ', 'e': 'ẹ', 'ê': 'ệ', 'i': 'ị', 'o': 'ọ', 'ô': 'ộ', 'ơ': 'ợ', 'u': 'ụ', 'ư': 'ự', 'y': 'ỵ'}
    }

    if diacritic:
        return tone_marks[diacritic].get(nucleus, nucleus)  # Combine nucleus with its diacritic
    return nucleus  # If no diacritic, return the nucleus as it is

# Function to permutate components of two words and return pairs
def permutate(word1, word2):
    # Extract components from both words
    components1 = [word1['initial_consonant'], word1['nucleus'], word1['final_consonant'], word1['diacritic']]
    components2 = [word2['initial_consonant'], word2['nucleus'], word2['final_consonant'], word2['diacritic']]
    
    # List to store pairs
    pairs = []

    # Generate all possible permutations of components using itertools.product()
    for (initial_consonant1, nucleus1, final_consonant1, diacritic1), (initial_consonant2, nucleus2, final_consonant2, diacritic2) in itertools.product(
            itertools.product([word1['initial_consonant'], word2['initial_consonant']], 
                              [word1['nucleus'], word2['nucleus']], 
                              [word1['final_consonant'], word2['final_consonant']], 
                              [word1['diacritic'], word2['diacritic']]),
            repeat=2):
        
        # Combine nucleus with diacritic for both words
        vowel1 = combine_vowel(nucleus1, diacritic1)
        vowel2 = combine_vowel(nucleus2, diacritic2)
        
        # Form the two words
        word1_combined = f"{initial_consonant1}{vowel1}{final_consonant1}"
        word2_combined = f"{initial_consonant2}{vowel2}{final_consonant2}"
        
        # Append the pair to the list
        pairs.append((word1_combined, word2_combined))
    
    return pairs

# Example usage
word1 = {
    'initial_consonant': 'm',
    'nucleus': 'e',
    'final_consonant': 'o',
    'diacritic': 'nặng'
}

word2 = {
    'initial_consonant': 'b',
    'nucleus': 'e',
    'final_consonant': '',
    'diacritic': 'sắc'
}

# Generate all permutations in pairs of word1 and word2
all_pairs = permutate(word1, word2)
print(all_pairs)
