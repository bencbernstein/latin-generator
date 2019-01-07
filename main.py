import random
from data import *
from sequence import *

def decline_noun(noun_object, case, number):
    gender = noun_object["latin"]["gender"]
    ending = latin_noun_endings[gender][case][number]
    return noun_object["latin"]["stem"] + ending

def make_verb(verb_object, verb_number, tense):
    return verb_object[verb_number][tense]

def make_latin_sentence(sentence_object):
    latin_subject = decline_noun(sentence_object["subject"], "subject", sentence_object["subject_number"])

    latin_object = decline_noun(sentence_object["object"], "object", sentence_object["object_number"])

    verb_number = sentence_object["subject_number"]
    latin_verb = make_verb(sentence_object["verb"]["latin"], verb_number, sentence_object["tense"])
    shuffled = [latin_subject, latin_verb, latin_object]
    random.shuffle(shuffled)
    return " ".join(shuffled)

def make_english_sentence(sentence_object):
    english_subject = sentence_object["subject"]["english"][sentence_object["subject_number"]]
    english_object = sentence_object["object"]["english"][sentence_object["object_number"]] 
    english_verb = sentence_object["verb"]["english"][sentence_object["subject_number"]][sentence_object["tense"]]
    return "the " + english_subject + " " + english_verb + " " + "the " + english_object

def make_red_herrings(sentence_object, params):
    red_herrings = []
    for tense in params["tense"]:
        for number in params["subject_number"]:
            red_herring = {
                "subject": sentence_object["subject"],
                "verb": sentence_object["verb"],
                "object": sentence_object["object"],
                "subject_number": number, 
                "object_number": number,
                "tense": tense
            }
            red_herring_swapped = {
                "subject": sentence_object["object"],
                "verb": red_herring["verb"],
                "object": sentence_object["subject"],
                "subject_number": red_herring["subject_number"], 
                "object_number": red_herring["object_number"],
                "tense": red_herring["tense"]
            }
            red_herrings.append(make_english_sentence(red_herring_swapped))
            red_herrings.append(make_english_sentence(red_herring))
    random.shuffle(red_herrings)
    return "\n".join(red_herrings)

def generate_questions(params):
    print("===new level / new parameters in effect===")
    for _ in range(params["number"]):

        random_nouns = random.sample(params["nouns"], 2)

        sentence_object = {
            "subject": nouns_dictionary[random_nouns[0]],
            "verb": verbs_dictionary[random.choice(params["verbs"])],
            "object": nouns_dictionary[random_nouns[1]],
            "subject_number": random.choice(params["subject_number"]), 
            "object_number": random.choice(params["object_number"]),
            "tense": random.choice(params["tense"])
        }

        latin_sentence = make_latin_sentence(sentence_object)
        print("=====")
        print(latin_sentence)
        print("\n")
        red_herrings = make_red_herrings(sentence_object, params)
        print(red_herrings)

        correct_answer_english = make_english_sentence(sentence_object)
        print("\n")
        print("answer:",correct_answer_english)
        print("\n")

# set levels set in sequence.py
[generate_questions(params) for params in levels]
