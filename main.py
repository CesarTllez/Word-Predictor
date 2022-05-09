acceptanceSpeech = {
    'speech': open("discurso.txt", "r", encoding="utf-8"),
    'speechWSC': '',
    'regex': ',.?¿<>«»()!¡:'
}

def wordSeparator(speech):
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
    acceptanceSpeech['speech'].close()
    return acceptanceSpeech['speechWSC'].split()

print(wordSeparator(acceptanceSpeech['speech']))