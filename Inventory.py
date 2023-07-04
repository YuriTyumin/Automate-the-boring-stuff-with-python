def print_inventory(inventory):
    print('Inventory:')
    sum_invenory = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        sum_invenory = sum_invenory + int(v)
    print(f'Total numbers of items: {sum_invenory}')


game_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
print_inventory(game_inventory)
