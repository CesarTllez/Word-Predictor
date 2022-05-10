acceptanceSpeech = {
    'speech': open("discurso.txt", "r", encoding="utf-8"),
    'speechWSC': '',
    'regex': ',.?¿<>«»()!¡:',
    'wordPair': []
}

def wordSeparator(speech):
    """Method that allows changing or eliminating
    the special characters of the speech and separating
    the words of it."""
    for paragraph in speech:
        for letter in paragraph:
            if letter == 'á':
                acceptanceSpeech['speechWSC'] += 'a'
            elif letter == 'é':
                acceptanceSpeech['speechWSC'] += 'e'
            elif letter == 'í':
                acceptanceSpeech['speechWSC'] += 'i'
            elif letter == 'ó' or letter == 'ö':
                acceptanceSpeech['speechWSC'] += 'o'
            elif letter == 'ú':
                acceptanceSpeech['speechWSC'] += 'u'
            elif letter == 'ñ':
                acceptanceSpeech['speechWSC'] += 'n'
            elif letter in acceptanceSpeech['regex']:
                pass
            else:
                acceptanceSpeech['speechWSC'] += letter.lower()
    
    return acceptanceSpeech['speechWSC'].split()

from statistics import mode

def getSuggestion(phraseInput):
    """Method that allows get the next words corresponding 
    to the input word"""
    wordInputArray = phraseInput.split()
    if len(wordInputArray) < 3:
        wordSeparatorAux = wordSeparator(acceptanceSpeech['speech'])
        index = 0; acceptanceSpeech['wordPair'].clear()
        for word in wordSeparatorAux:
            if word == wordInputArray[len(wordInputArray)-1]:
                if (index+1) != len(wordSeparatorAux):
                    acceptanceSpeech['wordPair'].append(wordSeparatorAux[index+1])
            index += 1

        if len(acceptanceSpeech['wordPair']) != 0:
            return mode(acceptanceSpeech['wordPair'])