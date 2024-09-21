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
    result_pairs = []

    for i in range(8):
        pairs.append(f'{i:04b}')

    for struct in pairs:
        result = []
        result_2 = []
        for i in range(len(struct)):
            if struct[i] == "0":
                result.append(components1[i])
                result_2.append(components2[i])
            else:
                result.append(components2[i])
                result_2.append(components1[i])

        vowel1 = combine_vowel(result[1], result[3])
        vowel2 = combine_vowel(result_2[1], result_2[3])
        word1_combined = f"{result[0]}{vowel1}{result[2]}"
        word2_combined = f"{result_2[0]}{vowel2}{result_2[2]}"
        result_pairs.append((word1_combined, word2_combined))
    
    return result_pairs

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
