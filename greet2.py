import collections

def words_order(text: str, words: list) -> bool:
    reci = text.split()
    dic_text = dict(enumerate(reci))
    dic_words = dict(enumerate(words))
    indexi = []

    for i in collections.Counter(words).values():
        if i > 1:
            return False
        
    check =  all(item in reci for item in words)
    if check == False:
        return False
    else:
        return True

    for i in dic_words.values():
        for ind, rec in dic_text.items():
            if i in rec:
                indexi.append(ind)

    indexi1 = sorted(indexi) 
    
    if indexi == indexi1:
        return True
    else:
        return False

if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['country', 'world']))