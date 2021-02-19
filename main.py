from inspect import signature
import random

ctr = open("Lists of categories/countries", "r")
anim = open("Lists of categories/animals", "r")
city = open("Lists of categories/cities", "r")
plants = open("Lists of categories/plants", "r")
noun = open("Lists of categories/nouns", "r")
verbs = open("Lists of categories/verbs", "r")
names = open("Lists of categories/names", "r")
letters = input('Enter the letters to match ')
letters = letters.upper()


def countries(letters, ctr):
    for line in ctr:
        for word in line.split():
            if word.isalpha():
                if word.startswith(letters):
                    return "country: " + word


def ctr_cit(letters, topic):
    for line in topic:
        if line[0].startswith(letters):
            return topic.name + ": " + line


print(
    f'{countries(letters, ctr)} {ctr_cit(letters, city)} '
    f'{ctr_cit(letters, anim)} {ctr_cit(letters, plants)}'
    f' {ctr_cit(letters, noun)} {ctr_cit(letters, names)}')
