import random

d = {}


def main(line):
    for n in range(0, len(line)-1):
        words = line[n].split()
        for i in range(0, len(words)-2):
            d[(words[i], words[i+1])] = [words[i+2]]
    output(d)


def output(d):
    new_text = ''
    for i in range(30):
        sentence = list(random.choice(list((d.keys()))))
        sentence[0] = sentence[0].capitalize()
        for j in range(random.randint(4, 10)):
            words = list(random.choice(list((d.keys()))))
            sentence.extend(words)
        sentence[-1] += ". "
        sentence = ' '.join(sentence)
        new_text += sentence
    print(new_text)


if __name__ == '__main__':
    infile = open('sherlock_small.txt', 'r')
    line = infile.readlines()
    infile.close()
    main(line)
