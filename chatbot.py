from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello", ["Hello!", "Hi there!"]],
    ["how are you", ["I'm fine, thanks!"]],
    ["bye", ["Goodbye!"]]
]

chat = Chat(pairs, reflections)
chat.converse()