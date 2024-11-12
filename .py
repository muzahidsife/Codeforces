def count_middle_letters(text):
    if len(text) > 10:
        middle_text = text[1:-1]
        middle_count = len(middle_text)
        return f"{text[0]}{middle_count}{text[-1]}"
    else:
        return text

num_words = int(input())

for _ in range(num_words):
    word = input()
    result = count_middle_letters(word)
    print(result)
