articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    result = []
    if letter_case == False:
        key = str(key).lower()
        for my_dict in articles_dict:

            for k, v in my_dict.items():
                if str(v).lower().find(key) != -1:
                    result += my_dict.values()
        return print(result)

    else:
        for my_dict in articles_dict:
            for k, v in my_dict.items():
                if str(my_dict.values()).find(key) != -1:
                    result += my_dict.values()
            return print(result)


if __name__ == "__main__":
    find_articles("ocean")
