emoticon = "ʕ•ᴥ•ʔ"

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("I am a machine.")
    
    
def say(phrase):
    print(phrase + " " + emoticon)
          
main()