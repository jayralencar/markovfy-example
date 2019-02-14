import markovify

with open("sherlock.txt") as f:
    text = f.read()

    text_model = markovify.Text(text, state_size=3)

    for i in range(5):
        print(text_model.make_sentence())
print("\nPortuguese:\n")
# Portuguese
with open("cdg.txt") as f2:
    text2 = f2.read()

    text_model2 = markovify.Text(text2)

    for i in range(5):
        print(text_model2.make_short_sentence(140))