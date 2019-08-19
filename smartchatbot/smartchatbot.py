import requests

responses = {
    "what": "A robot is a machine—especially one programmable by a computer— capable of carrying out a complex series of actions automatically.",
    "use": "Robots have replaced humans in performing repetitive and dangerous tasks which humans prefer not to do, or are unable to do because of size limitations, or which take place in extreme environments such as outer space or the bottom of the sea.",
    "long": "The idea of automata originates in the mythologies of many cultures around the world. Engineers and inventors from ancient civilizations, including Ancient China, Ancient Greece, and Ptolemaic Egypt, attempted to build self-operating machines, some resembling animals and humans.",
    "where": "The term comes from a Czech word, robota, meaning 'forced labor'",
    "word": "The word robot can refer to both physical robots and virtual software agents, but the latter are usually referred to as bots."
}


def processIntent(intent):
    key = intent["class_name"].lower()
    confidence = intent["confidence"]

    if confidence < 40:
        return "I don't know that"

    if key in responses:
        return "I am " + str(confidence) + "% sure you want to know: " + responses[key]
    else:
        return "I don't know that"


# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "c1572fe0-c2b0-11e9-a971-e3949585133e62cddc89-ab1f-43fd-aba8-0a54a9801947"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

# response = classify("Length of time between now and when robots were made")
# print(response)

def main():
    print("Welcome to Robot Facts! I can talk to you about robots\n")
    print("Ask me a question or type quit\n")

    userInput = ""

    while userInput != "quit":
        userInput = input("Whats your question? ").lower()
        #print(userInput)
        if userInput != "quit":
            intent = classify(userInput)
            response = processIntent(intent)
            print(response)

    print("It was good talking to you, bye!")


main()
