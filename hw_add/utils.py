import pymorphy2
import numpy as np
import pickle
import os

morph = pymorphy2.MorphAnalyzer()

print('Start loading...')
with open('./1grams-3.txt', 'r', encoding='utf-8') as f:
    words = f.readlines()

print('Start calc word in base...')
pos_map = {}
for num_word in words:
    _, word = num_word.split()

    word = word.lower()
    parse_word = morph.parse(word)[0]
    pos = parse_word.tag.POS
    if pos not in pos_map:
        pos_map[pos] = [parse_word]
    else:
        pos_map[pos].append(parse_word)

print('Finish calc word in base...')

def get_tags(word):
    parse_word = morph.parse(word)[0]
    pos = parse_word.tag.POS
    animacy = parse_word.tag.animacy
    aspect = parse_word.tag.aspect
    case = parse_word.tag.case
    gender = parse_word.tag.gender
    involvement = parse_word.tag.involvement
    mood = parse_word.tag.mood
    number = parse_word.tag.number
    person = parse_word.tag.person
    tense = parse_word.tag.tense
    transitivity = parse_word.tag.transitivity
    voice = parse_word.tag.voice


    tags = set()
    for tag in [pos, animacy, aspect, case,
               gender, involvement, mood, number,
               person, tense, transitivity, voice]:
        if tag is not None:
            tags.add(str(tag))
    return tags


def get_random_word(pos):
    if pos in pos_map:
        ind = np.random.randint(len(pos_map[pos]))
        return pos_map[pos][ind]

    raise ValueError


def get_equal_sentence(sentence):
    new_sentence = []
    for word in sentence.split():
        parse_word = morph.parse(word)[0]

        pos = parse_word.tag.POS
        tags = get_tags(word)

        new_word = None
        while new_word is None:
            rnd_word = get_random_word(pos)
            new_word = rnd_word.inflect(tags)

        new_sentence.append(new_word.word)

    return ' '.join(new_sentence)
