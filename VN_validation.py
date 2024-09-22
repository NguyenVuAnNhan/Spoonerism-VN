import mwparserfromhell
import bz2
import re

# Function to extract words from Wiktionary dump
def extract_words_from_dump(dump_file):
    words = set()

    # Open the Wiktionary dump file (compressed in bz2 format)
    with bz2.open(dump_file, 'rt', encoding='utf-8') as f:
        current_page = []
        inside_page = False

        for line in f:
            if '<page>' in line:
                inside_page = True
                current_page = []
            elif '</page>' in line:
                inside_page = False
                page_text = ''.join(current_page)
                words.update(extract_words_from_page(page_text))
            if inside_page:
                current_page.append(line)

    return words

# Function to parse words from each page
def extract_words_from_page(page_text):
    words_in_page = set()
    if '<title>' in page_text and '<ns>0</ns>' in page_text:  # Only process actual dictionary entries (namespace 0)
        title_match = re.search(r'<title>(.*?)</title>', page_text)
        if title_match:
            title = title_match.group(1)
            # Ignore non-article pages like "Category:", "Template:", etc.
            if ':' not in title and '{{lang|vi' in page_text:  # Check that the page contains Vietnamese content
                words_in_page.add(title)
    return words_in_page

# Save extracted words to a file
def save_words_to_file(words, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in sorted(words):
            f.write(word + '\n')

# Main function
def main():
    dump_file = 'viwiktionary.bz2'  # Path to your downloaded Wiktionary dump
    output_file = 'vietnamese_words.txt'

    words = extract_words_from_dump(dump_file)
    save_words_to_file(words, output_file)
    print(f"Extracted {len(words)} words and saved to {output_file}")

if __name__ == "__main__":
    main()
