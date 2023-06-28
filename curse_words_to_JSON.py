import json

ar = []

try:
    with open('C:\\for_bots\\curse_words.txt', encoding='utf-8') as r:
        for i in r:
            n = i.lower().split('\n')[0]
            if n != '':
                ar.append(n)
    with open('C:\\for_bots\\WisheryBotTelegram\\curse_words.json', 'w', encoding='utf-8') as e:
        json.dump(ar, e)
except FileNotFoundError:
    print('Not found')
except Exception as e:
    print(f"Error: {e.__class__.__name__}")

