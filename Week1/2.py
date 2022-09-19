# Create a function that translates emoticons to specific words. Given a sentence as a
# string, replace the emoticons ‘:D’, ‘:)’, ‘:(‘ and ‘:P’ into the words ‘smile’, ‘grin’, ‘sad’ and ‘mad’
# Example: “I feel :( today” à “I feel sad today”


def translate(quote):
    if ":D" in quote:
        print(quote.replace(":D", "smile"))
    elif ":)" in quote:
        print(quote.replace(":)", "grin"))
    elif ":(" in quote:
        print(quote.replace(":(", "sad"))
    elif ":P" in quote:
        print(quote.replace(":P", "mad"))


q = input("Quote: ")
translate(q)
