

def display_inventory(inventory: dict) -> None:
    total = 0
    for key, value in inventory.items():
        print(f"{key}: {value}")
        total += value
    print("Total number of items: ", total)


def add_to_inventory(inventory: dict, loot: list) -> None:
    for item in loot:
        if item in INVENTORY:
            INVENTORY[item] += 1
        else:
            INVENTORY[item] = 1


if __name__ == "__main__":

    INVENTORY = {
        "arrow": 5,
        "bow": 1,
        "apple": 7,
        "sword": 2
    }

    LOOT = ["sword", "grape"]

    add_to_inventory(INVENTORY, LOOT)
    display_inventory(INVENTORY)
