import requests


list_heroes = ["Hulk", "Captain America", "Thanos"]
token = "2619421814940190"
intel = 'intelligence'


# Функция вывода отсортированного по интеллекту списка героев
def rate_hero(hero_list, tkn, stat):
    heroes_to_compare = {}
    for hero in hero_list:
        search_url = f'https://superheroapi.com/api/{tkn}/search/{hero}'
        hero_id = requests.get(search_url)
        id_num = hero_id.json()['results'][0]['id']
        intel_url = f'https://superheroapi.com/api/{token}/{id_num}/powerstats'
        get_intel_stat = requests.get(intel_url)
        stats = get_intel_stat.json()[stat]
        elem = {hero: stats}
        heroes_to_compare.update(elem)
    all_heroes_sorted = sorted(heroes_to_compare.items())
    for number, hero in enumerate(reversed(all_heroes_sorted)):
        print(f'{number + 1} место занял {hero[0]}! Уровень интеллекта - {hero[1]}')


rate_hero(list_heroes, token, intel)