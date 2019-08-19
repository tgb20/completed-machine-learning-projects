# Sourced from https://en.wikipedia.org/wiki/Robot

prompts = {
    "what": "What is a robot?",
    "use": "What are robots used for?",
    "long": "How long have there been robots?",
    "where": "Where does the word robot come from?",
    "word": "What does the word robot refer too?"
}

responses = {
    "what": "A robot is a machine—especially one programmable by a computer— capable of carrying out a complex series of actions automatically.",
    "use": "Robots have replaced humans in performing repetitive and dangerous tasks which humans prefer not to do, or are unable to do because of size limitations, or which take place in extreme environments such as outer space or the bottom of the sea.",
    "long": "The idea of automata originates in the mythologies of many cultures around the world. Engineers and inventors from ancient civilizations, including Ancient China, Ancient Greece, and Ptolemaic Egypt, attempted to build self-operating machines, some resembling animals and humans.",
    "where": "The term comes from a Czech word, robota, meaning 'forced labor'",
    "word": "The word robot can refer to both physical robots and virtual software agents, but the latter are usually referred to as bots."
}



def processInput(userInput):
    pass

def main():
    print("Welcome to Robot Facts! I can talk to you about robots\n")
    print("Ask me a question or type quit\n")

    userInput = ""

    while userInput != "quit":
        userInput = input("Whats your question? ").lower()
        #print(userInput)
        if userInput != "quit":
            response = processInput(userInput)
            print(response)

    print("It was good talking to you, bye!")


main()