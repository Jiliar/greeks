def conjugate_verb(verb, form):
    result = verb['greek']+"{}"
    if form == 'SINGULAR_FIRST_PERSON':
        if verb['greek'][-1] != "ω":
            return "[yo]: "+result.format("ω")
        else:
            return "[yo]: "+verb['greek']
    elif form == 'SINGULAR_SECOND_PERSON':
        return "[tú]: "+result.format("εις")
    elif form == 'SINGULAR_THIRD_PERSON':
        return "[él]: "+result.format("ει")
    elif form == 'PLURAL_FIRST_PERSON':
        return "[nosotros]: "+result.format("ομεν")
    elif form == 'PLURAL_SECOND_PERSON':
        return "[vosotros]: "+result.format("ετε")
    elif form == 'PLURAL_THIRD_PERSON':
        return "[ellos]:    "+result.format("ουσι")


verb = {'greek': "ακούω", 'spanish': 'escuchar'}
verb = {'greek': "πιστεύ", 'spanish': 'creer'}
verb = {'greek': "λεγω", 'spanish': 'hablar'}

print("----------------------------------")
print("Spanish: {}".format(verb['spanish']))
print("Greek:   {}".format(verb['greek']))
print("----------------------------------")
print("----------------------------------")
print('***          SINGULAR          ***')
print("----------------------------------")
print(conjugate_verb(verb, 'SINGULAR_FIRST_PERSON'))
print(conjugate_verb(verb, 'SINGULAR_SECOND_PERSON'))
print(conjugate_verb(verb, 'SINGULAR_THIRD_PERSON'))
print("----------------------------------")
print('***           PLURAL           ***')
print("----------------------------------")
print(conjugate_verb(verb, 'PLURAL_FIRST_PERSON'))
print(conjugate_verb(verb, 'PLURAL_SECOND_PERSON'))
print(conjugate_verb(verb, 'PLURAL_THIRD_PERSON'))
print("----------------------------------")