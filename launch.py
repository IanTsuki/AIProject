print("Hello,")
print("I am your personal assistant IDA.")
print("At the moment I am in Alpha 1, so please excuse any problems with my systems.")


meow = "death"
while meow != "close":
    meow = input()
    meow = meow.lower()
    if "how" in meow and "are" in meow and "you" in meow:
        print("I am good.")
    if "hello" in meow:
        print("Hello, what can I do for you today?")
    if "who" in meow and "are" in meow and "you" in meow:
        print("I am IDA, the Intiligent Desktop Application.")
