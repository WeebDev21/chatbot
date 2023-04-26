#pip install nltk

import re
from responses import unknown

def probability(user_message, recognised_words, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def answer(bot_response, list_of_words, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = probability(message, list_of_words, required_words)

    answer('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'])
    answer('See you!', ['bye', 'goodbye'])
    answer('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    answer('You\'re welcome!', ['thank', 'thanks'])
    answer('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    answer('My name is Waltbot, but you can call me Walt.',['what', 'is', 'your', 'name'], required_words=['name'])

    answer("It depends upon how you use it. AI has been a boon to mankind as it has\n "
             "helped humans in a lot of fields like healthcare, technology, education and many other fields.", ['is', 'ai', 'boon', 'or', 'curse'], required_words=['boon', 'curse'])
    answer("Ai has helped humans a lot in several fields, but it has also been a problem to them.\n "
             "AI has caused unemployment in some fields. People are losing their jobs and being replaced by \n"
             "AI enabled machines.", ['has', 'ai', 'harmed', 'humans'], required_words=['harmed'])
    answer('AI stands for Artificial Intelligence. It is a subfield of computer Science concerned with \n'
             'the cause to design intelligent machines, that possess the ability to think logically and \n'
             'respond to certain things like human beings.', ['what', 'is', 'ai', 'you', 'know', 'about'], required_words=['ai'])
    answer("Sure! I like making friends. You are my buddy now.", ['will', 'you', 'be', 'my', 'friend'], required_words=['friend'])
    answer("AI can be helpful in various fields. some of these fields are:\n Education\n Healthcare\n Technology", ['how', 'is', 'ai', 'helpful'], required_words=['ai', 'helpful'])
    answer("There are three domains of AI:\n (1) Data Science\n (2) Computer Vision\n (3) Natural Language Processing", ['what', 'are', 'domains', 'of', 'ai'], required_words=['domains'])
    answer('The subfields of AI are:\n (1) Machine Learning\n (2) Deep Learning', ['what', 'are', 'subfields', 'of', 'ai'], required_words=['subfields'])
    answer('I will tell you about AI, its applications, its drawbacks and advantages, and the need to\n'
             'adopt AI for increasing the productivity of work.', ['how', 'will', 'you', 'help', 'us'], required_words=['help'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return unknown() if highest_prob_list[best_match] < 1 else best_match


def get_answer(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


while True:
    print('Walt: ' + get_answer(input('You: ')))
