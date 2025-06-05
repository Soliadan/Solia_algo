from typing import List

def find_max_chain(readfile: str, writefile: str):
   
    word_list = read_file(readfile)
    word_list.sort(key=len)  

    word_table = {word: 1 for word in word_list}  
    word_set = set(word_list)  

    for word in word_list:
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            if new_word in word_set:
                word_table[word] = max(word_table[word], word_table[new_word] + 1)

    write_file(writefile, max(word_table.values()))


def read_file(filename: str) -> List[str]:
    with open(filename, 'r', encoding='utf-8') as file:
        first_line = file.readline().strip()
        if not first_line.isdigit():
            raise ValueError(f"Очікувалося число в першому рядку, але отримано: '{first_line}'")
        number_of_words = int(first_line)
        word_list = [file.readline().strip() for _ in range(number_of_words)]
    return word_list



def write_file(filename: str, result: int):
    """Writes result to the output file."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(result))


if __name__ == "__main__":
    import os

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    input_filename = os.path.join(base_dir, "input", "wchain.in")
    output_dir = os.path.join(base_dir, "output")
    output_filename = os.path.join(output_dir, "wchain.out")

    os.makedirs(output_dir, exist_ok=True)

    find_max_chain(input_filename, output_filename)

    with open(output_filename, 'r', encoding='utf-8') as f:
        result = f.read().strip()
        print(f"Максимальний ланцюжок: {result}")
