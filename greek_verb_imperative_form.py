def conjugate_verb(verb, form):
    result = ""
    if verb['greek'][-1] == "ω":
        result = verb['greek'][:-1]+"{}"
    else:
        result = verb['greek']+"{}"
    
    if form == 'SINGULAR_SECOND_PERSON':
        return "[tú]: "+result.format("ε")
    elif form == 'SINGULAR_THIRD_PERSON':
        return "[él]: "+result.format("ετω")
    elif form == 'PLURAL_SECOND_PERSON':
        return "[vosotros]: "+result.format("ετε")
    elif form == 'PLURAL_THIRD_PERSON':
        return "[ellos]:    "+result.format("ετωσαν")


verb = {'greek': "λεγω", 'spanish': 'hablar'}

print("----------------------------------")
print("Spanish: {}".format(verb['spanish']))
print("Greek:   {}".format(verb['greek']))
print("----------------------------------")
print("----------------------------------")
print('***          SINGULAR          ***')
print("----------------------------------")
print(conjugate_verb(verb, 'SINGULAR_SECOND_PERSON'))
print(conjugate_verb(verb, 'SINGULAR_THIRD_PERSON'))
print("----------------------------------")
print('***           PLURAL           ***')
print("----------------------------------")
print(conjugate_verb(verb, 'PLURAL_SECOND_PERSON'))
print(conjugate_verb(verb, 'PLURAL_THIRD_PERSON'))
print("----------------------------------")