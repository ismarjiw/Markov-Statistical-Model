import random

def build_frequency_table(text, k):
    frequency_table_map = {}

    for i in range(len(text) - k):
        kgram = tuple(text[i:i + k])
        next_char = text[i + k]

        if kgram not in frequency_table_map:
            frequency_table_map[kgram] = {'frequencies': {}, 'total': 0}

        frequency_table_map[kgram]['frequencies'][next_char] = \
            frequency_table_map[kgram]['frequencies'].get(next_char, 0) + 1

        frequency_table_map[kgram]['total'] += 1

    return frequency_table_map

def rand(frequency_table_map, kgram):
    if kgram in frequency_table_map:
        choices = list(frequency_table_map[kgram]['frequencies'].keys())
        probabilities = [
            frequency_table_map[kgram]['frequencies'][char] / frequency_table_map[kgram]['total']
            for char in choices
        ]

        return random.choices(choices, probabilities)[0]

    raise RuntimeError("Error generating random character. Kgram not found in frequency table.")

def generate(frequency_table_map, kgram, T):
    result = list(kgram)

    for _ in range(T - len(kgram)):
        next_char = rand(frequency_table_map, kgram)
        result.append(next_char)
        kgram = tuple(result[-len(kgram):])

    return ''.join(result)

if __name__ == "__main__":
    input_path = 'green_eggs.txt'
    with open(input_path, 'r') as file:
        input_text = file.read()

    k = 4
    kgram = tuple(input_text[:k])
    T = 50

    frequency_table_map = build_frequency_table(input_text, k)
    generated_text = generate(frequency_table_map, kgram, T)
    print(generated_text)