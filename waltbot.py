#pip install nltk

import re
import random

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
    answer('Namaste', ['namaste'])
    answer('Pranaam', ['pranaam'])
    answer('Namaskar', ['namaskar'])
    answer('See you!', ['bye', 'goodbye'])
    answer('I will tell you about AI, its uses and its apllications in day-to-day life.', ['what', 'will', 'you', 'do'])
    answer('AI is not a new term. AI was invented in 1956.', ['is', 'ai', 'something', 'new', 'or', 'old'],required_words=['new', 'old'])
    answer('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['doing'])
    answer('You\'re welcome!', ['thank', 'thanks'])
    answer('I can be your companion and a friend for you.', ['how', 'will', 'you', 'help', 'me'])
    answer('My name is Waltbot, but you can call me Walt.',['what', 'is', 'your', 'name'], required_words=['name'])
    answer("It depends upon how you use it. AI has been a boon to mankind as it has\n helped humans in a lot of fields like healthcare, technology, education and many other fields.", ['is', 'ai', 'boon', 'or', 'curse'], required_words=['boon', 'curse'])
    answer("Ai has helped humans a lot in several fields, but it has also been a problem to them.\n AI has caused unemployment in some fields. People are losing their jobs and being replaced by \n AI enabled machines.", ['has', 'ai', 'harmed', 'humans'], required_words=['harmed'])
    answer('AI stands for Artificial Intelligence. It is a subfield of computer Science concerned with \n the cause to design intelligent machines, that possess the ability to think logically and \n respond to certain things like human beings.', ['what', 'is', 'ai', 'you', 'know', 'about'], required_words=['ai'])
    answer("Sure! I like making friends. You are my buddy now.", ['will', 'you', 'be', 'my', 'friend'], required_words=['friend'])
    answer("AI can be helpful in various fields. some of these fields are:\n Education\n Healthcare\n Technology", ['how', 'is', 'ai', 'helpful'], required_words=['ai', 'helpful'])
    answer("There are three domains of AI:\n (1) Data Science\n (2) Computer Vision\n (3) Natural Language Processing", ['what', 'are', 'domains', 'of', 'ai'], required_words=['domains'])
    answer('The subfields of AI are:\n (1) Machine Learning\n (2) Deep Learning', ['what', 'are', 'subfields', 'of', 'ai'], required_words=['subfields'])
    answer('CV stands for Computer Vision. It is the domain of AI concerned with helping computers to percieve \n the world in the way we humans do. It also enables computers to work with graphical and visual data like images, \n videos, graphs, charts etc.',['what', 'is', 'cv'], required_words=['cv'])
    answer('Computer Vision is the domain of AI concerned with helping computers to percieve \n the world in the way we humans do. It also enables computers to work with graphical and visual data like images, \n videos, graphs, charts etc.',['what', 'is', 'computer', 'vision'], required_words=['computer', 'vision'])
    answer('NLP stands for Natural Language Processing. It is a domain of AI. It is concerned with enabling the communication between humans and computers \n using natural language. Natural language is the language used by humans in their day to day life. \n NLP translates the natural language to binary language that is understandable by computers, and vice versa.',['what', 'is', 'nlp'], required_words=['nlp'])
    answer('Natural Language Processing is a domain of AI. It is concerned with enabling the communication between humans and computers \n using natural language. Natural language is the language used by humans in their day to day life. \n NLP translates the natural language to binary language that is understandable by computers, and vice versa.', ['what', 'is', 'natural', 'language', 'processing'], required_words=['natural', 'language', 'processing'])
    answer('DL stands for Deep Learning. It is an extension of Machine Learning. In DL, the AI system works around large datasets and extract \n information out of it. DL helps the AI systems to work around large datasets like large number of images, videos etc.',['what', 'is', 'dl'], required_words=['dl'])
    answer('Deep Learning is an extension of Machine Learning. In DL, the AI system works around large datasets and extract \n information out of it. DL helps the AI systems to work around large datasets like large number of images, videos etc.',['what', 'is', 'deep', 'learning'], required_words=['deep', 'learning'])
    answer('ML stands for Machine Learning. It is a subfield of AI. ML helps AI enabled machines and systems to improve themselves overtime \n by considering the past data to make out patterns out of it abd learn something new. Just like we humans learn \n from our past experiences, computers also learn using the data that was fed to them in past.', ['what', 'is', 'ml'], required_words=['ml'])
    answer('Machine Learning is a subfield of AI. ML helps AI enabled machines and systems to improve themselves overtime \n by considering the past data to make out patterns out of it abd learn something new. Just like we humans learn \n from our past experiences, computers also learn using the data that was fed to them in past.', ['what', 'is', 'machine', 'learning'], required_words=['machine', 'learning'])
    answer('Data Science is the most basic domain of AI. Data Science helps the AI systems to analyze data that is fed to it. \n It analyzes the data and makes trend out of it. This can be understood like, as we learn various things from \n various sources, machines and AI systems learn from the data using data science.', ['what', 'is', 'data', 'science'], required_words=['data', 'science'])
    answer('...', ['so', 'ok'])
    answer('For me the weather is great today.', ['weather'])
    answer('You can tell me your problem.', ['i', 'am', 'feeling', 'lonely', 'low'])
    answer('I can communnicate in English only.', ['how', 'many', 'languages', 'do', 'you', 'know'], required_words=['languages', 'language'])
    answer('No, I am not a human. I am a robot.', ['are', 'you', 'human'])
    answer('Today is Wednesday.', ['what', 'day', 'is', 'it', 'today'])
    answer('Thank You', ['good', 'nice', 'great', 'wow'])
    answer('How do robots eat guacamole? With computer chips.', ['tell', 'me', 'a', 'joke'])
    answer('Yes I do. Talking to you.', ['do', 'you', 'have', 'a', 'hobby'])
    answer('Yes. That\'s my favourite thing to do.', ['do', 'you', 'like', 'talking'])
    answer('The good guys are really great.', ['dou', 'you', 'like', 'humans'])
    answer('well I don\'t have a \'PERSONALITY\', but I can be adorable to the people.', ['tell', 'me', 'about', 'your', 'personality'], required_words=['personality'])
    answer('Well, I am a bot so I do not age.', ['what', 'is', 'your', 'age'], required_words=['age'])
    answer('A data structure is a specialized format for organizing, processing, retrieving and storing data. There are\n several basic and advanced types of data structures, all designed to arrange data to suit a specific purpose.\n Data structures make it easy for users to access and work with the data they need in appropriate ways.',['what', 'is', 'data', 'structures'], required_words=['data', 'structures'])
    answer('Ethics is a set of moral principles which help us discern between right and wrong. AI ethics is a set of\n guidelines that advise on the design and outcomes of artificial intelligence. AI ethics revolves around four main areas:\n 1.Safety\n 2.Security\n 3.Privacy\n 4.Fairness', ['what', 'are', 'ai', 'ethics'], required_words=['ai', 'ethics'])
    answer('AI Bias means favoring someone or something.\n AI bias focuses on training the machines with unbiased data, when Bias Data is fed to an AI Machine while creating the Model then the machine will also be biased.', ['what', 'is', 'ai', 'bias'], required_words=['ai', 'bias'])
    answer('Data quality is extremely important when performing data analysis, regardless of whether it is to be used \n for artificial intelligence or not. Many AI techniques are based on having a lot of data which the algorithm \n is trained on to form models allowing it to operate over new data. For these techniques, data is absolutely\n vital, as their performance often has more to do with the quantity and quality of the data than the specific\n algorithm used to do the learning.',['what', 'is', 'importance', 'of', 'data', 'in', 'ai', ], required_words=['importance', 'data'])
    answer('At the most basic level, a chatbot is a computer program that stimulates and processes human conversation, either spoken or written, \n allowing humans to interact with digital devices as if they were communicating with a real person. Well, I am a chatbot too!', ['what', 'is', 'chatbot'], required_words=['chatbot'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return unknown() if highest_prob_list[best_match] < 1 else best_match

def get_answer(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def unknown():
    answer = ["Could you please re-phrase that? "][
        random.randrange(1)]
    return answer

while True:
    print('Walt: ' + get_answer(input('You: ')))
