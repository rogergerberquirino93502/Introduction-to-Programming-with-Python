def great(input):
    if "hello" in input:
        return "Hello! How can I help you today?"
    else:
        return "Hi there! What can I do for you?"


greeting = great("hello")
print(greeting + " Welcome to the guessing game!")