def add_to_inventory(inventory, added_items):
    print('Inventory:')
    for v in added_items:
        if v in inventory:
            inventory[v] += 1
        else:
            inventory[v] = 1
    return inventory


def print_inventory(inventory):
    sum_inventory = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        sum_inventory = sum_inventory + int(v)
    print(f'Total numbers of items: {sum_inventory}')


game_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(game_inventory, dragon_loot)
print_inventory(inv)

