from collections import deque

# đọc từ điển từ file
with open("data/wordsEn.txt") as f:
    words = set(word.strip().lower() for word in f if len(word.strip()) >= 3)

# loại bỏ các từ không thể sử dụng trong chuỗi
for word in words.copy():
    if word[0] == word[1]:
        words.remove(word)
    for i in range(2, len(word)):
        if word[i - 2:i] == word[i:i + 2]:
            words.remove(word)
            break


def longest_shiritori(start_word, word_list):
    graph = build_graph(word_list)
    longest_chain = []
    visited = set()
    stack = [(start_word, [start_word])]

    while stack:
        curr_word, chain = stack.pop()
        visited.add(curr_word)
        if len(chain) > len(longest_chain):
            longest_chain = chain
        last_char = curr_word[-1]
        neighbors = graph.get(last_char, [])
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append((neighbor, chain + [neighbor]))

    return longest_chain


def build_graph(word_list):
    graph = {}
    for word in word_list:
        first_char = word[0]
        last_char = word[-1]
        if first_char not in graph:
            graph[first_char] = []
        graph[first_char].append(word)
        if last_char not in graph:
            graph[last_char] = []
    return graph


arr = longest_shiritori("pen", words)
print(arr)