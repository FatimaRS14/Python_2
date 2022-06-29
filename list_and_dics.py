ef run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "García"}

    super_list = [
        {"firstname": "Francisco", "lastname": "García"},
        {"firstname": "Emmanuel", "lastname": "Rodriguez"},
        {"firstname": "Luis", "lastname": "Trinidad"},
        {"firstname": "Fatima", "lastname": "Rojas"},
        {"firstname": "Josué", "lastname": "Montiel"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43],
    }

    for key, value in super_dict.items():
        print(key, ">", value)


if __name__ == '__main__':
    run()