text = """Python is simple and Python is powerful.
Simple code is easy to read."""
 
words = text.lower().replace(".", "").replace(",", "").split()
 
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
 
print("Частоти слів (за алфавітом):")
for word in sorted(freq):
    print(word, "-", freq[word])
 
print("\nЧастоти слів (за спаданням кількості):")
for word in sorted(freq, key=freq.get, reverse=True):
    print(word, "-", freq[word])
 
#Лише слова з частотою >= 2
frequent = {w: c for w, c in freq.items() if c >= 2}
print("\nСлова, що трапляються 2+ рази:", frequent)
