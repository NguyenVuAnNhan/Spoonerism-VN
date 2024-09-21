import re

# Define tone marks and their corresponding names
tone_marks = {
    'á': 'sắc', 'à': 'huyền', 'ả': 'hỏi', 'ã': 'ngã', 'ạ': 'nặng',
    'ắ': 'sắc', 'ằ': 'huyền', 'ẳ': 'hỏi', 'ẵ': 'ngã', 'ặ': 'nặng',
    'ấ': 'sắc', 'ầ': 'huyền', 'ẩ': 'hỏi', 'ẫ': 'ngã', 'ậ': 'nặng',
    'é': 'sắc', 'è': 'huyền', 'ẻ': 'hỏi', 'ẽ': 'ngã', 'ẹ': 'nặng',
    'ế': 'sắc', 'ề': 'huyền', 'ể': 'hỏi', 'ễ': 'ngã', 'ệ': 'nặng',
    'í': 'sắc', 'ì': 'huyền', 'ỉ': 'hỏi', 'ĩ': 'ngã', 'ị': 'nặng',
    'ó': 'sắc', 'ò': 'huyền', 'ỏ': 'hỏi', 'õ': 'ngã', 'ọ': 'nặng',
    'ố': 'sắc', 'ồ': 'huyền', 'ổ': 'hỏi', 'ỗ': 'ngã', 'ộ': 'nặng',
    'ớ': 'sắc', 'ờ': 'huyền', 'ở': 'hỏi', 'ỡ': 'ngã', 'ợ': 'nặng',
    'ú': 'sắc', 'ù': 'huyền', 'ủ': 'hỏi', 'ũ': 'ngã', 'ụ': 'nặng',
    'ứ': 'sắc', 'ừ': 'huyền', 'ử': 'hỏi', 'ữ': 'ngã', 'ự': 'nặng',
    'ý': 'sắc', 'ỳ': 'huyền', 'ỷ': 'hỏi', 'ỹ': 'ngã', 'ỵ': 'nặng'
}

# Base vowels to replace diacritic-marked vowels
base_vowels = {
    'á': 'a', 'à': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
    'ắ': 'ă', 'ằ': 'ă', 'ẳ': 'ă', 'ẵ': 'ă', 'ặ': 'ă',
    'ấ': 'â', 'ầ': 'â', 'ẩ': 'â', 'ẫ': 'â', 'ậ': 'â',
    'é': 'e', 'è': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
    'ế': 'ê', 'ề': 'ê', 'ể': 'ê', 'ễ': 'ê', 'ệ': 'ê',
    'í': 'i', 'ì': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
    'ó': 'o', 'ò': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
    'ố': 'ô', 'ồ': 'ô', 'ổ': 'ô', 'ỗ': 'ô', 'ộ': 'ô',
    'ớ': 'ơ', 'ờ': 'ơ', 'ở': 'ơ', 'ỡ': 'ơ', 'ợ': 'ơ',
    'ú': 'u', 'ù': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
    'ứ': 'ư', 'ừ': 'ư', 'ử': 'ư', 'ữ': 'ư', 'ự': 'ư',
    'ý': 'y', 'ỳ': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y'
}

# Regex pattern to handle Vietnamese syllable structure
def split_vietnamese_word(word):
    # Corrected regex pattern to capture all Vietnamese vowel clusters including tone-marked vowels
    pattern = r"^(b|c|ch|d|đ|g|gh|h|k|kh|l|m|n|ng|ngh|nh|p|ph|q|r|s|t|th|tr|v|x|gi)?([aăâeêiîoôơuưyáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộơớờởỡợúùủũụứừửữựýỳỷỹỵ]+)(c|ch|m|n|ng|nh|p|t)?$"

    match = re.match(pattern, word)
    
    if match:
        initial_consonant = match.group(1) if match.group(1) else ""
        nucleus = match.group(2)
        final_consonant = match.group(3) if match.group(3) else ""

        # Detect diacritic in the vowel cluster
        diacritic = ""
        for char in nucleus:
            if char in tone_marks:
                diacritic = tone_marks[char]
                # Replace the vowel with its base form
                nucleus = nucleus.replace(char, base_vowels[char])
                break

        return {
            "initial_consonant": initial_consonant,
            "nucleus": nucleus,
            "final_consonant": final_consonant,
            "diacritic": diacritic
        }
    else:
        return {"error": "Invalid Vietnamese word"}

# Example usage
word = "trắng"
components = split_vietnamese_word(word)
print(components)
