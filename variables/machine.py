emoticon = "🤖"


def main():
    global emoticon
    say("Hello! I am a friendly robot.")
    emoticon = "😎"
    say("I am here to assist you with your tasks.")

def say(phrase):
    print(phrase + " " + emoticon)

main()