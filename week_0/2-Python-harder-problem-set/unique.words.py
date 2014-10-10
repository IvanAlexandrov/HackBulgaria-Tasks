def unique_words_count(arr):
    result = {}
    for word in arr:
        if word not in result:
            result[word] = word
    return len(result)

print(unique_words_count(["apple", "banana", "apple", "pie"]))
print(unique_words_count(["python", "python", "python", "ruby"]))
print(unique_words_count(["HELLO!"] * 10))
