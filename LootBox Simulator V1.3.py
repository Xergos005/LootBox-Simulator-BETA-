import random
input("Welcome to LootBox Simulator! Press ENTER to continue...")
rarity = ["common", "rare", "legendary", "mythic"]
common = ["Scrapped Assault Rifle", "Makeshift Shotgun", "Rusted Revolver" , "Vintage Pistol" , "Homemade Crossbow" , "Broken Hunting Rifle" , "Old Double Barrel Shotgun"]
rare = ["AK-47 Assault Rifle", "MP5 Submachine Gun", "M4 Assault Rifle" , "SCAR-L Assault Rifle" , "Kriss Vector SMG" , "Desert Eagle Pistol" , "SPAS-12 Shotgun" , "FAMAS Assault Rifle" , "AA-12 Shotgun" , "Uzi	Submachine Gun" , "MAC-10 Submachine Gun" , "Remington 870 Shotgun" , "Mossberg 500 Shotgun" , "AUG A3 Assault Rifle" , "P90 Submachine Gun" , "Benelli M4 Shotgun" , "HK416 Assault Rifle" , "G36C Assault Rifle" , "MP7	Submachine Gun" , "Saiga-12	Shotgun" , "USAS-12	Shotgun" , "Origin-12 Shotgun"]
legendary = ["RPG-7 Rocket Launcher", "AWP Sniper Rifle", "Barrett M82 Sniper Rifle", "Remington 700 Sniper Rifle", "SVD Dragunov Sniper Rifle", "L96A1 Sniper Rifle", "M40A5 Sniper Rifle", "CheyTac M200 Sniper Rifle", "Mosin-Nagant Sniper Rifle" , "SR-25 Marksman Rifle", "MK14 EBR Marksman Rifle", "M110 Marksman Rifle", "SKS Marksman Rifle", "G28 Marksman Rifle", "SCAR-H DMR Marksman Rifle", "M14 Marksman Rifle" , "M72 LAW Rocket Launcher", "AT4 Rocket Launcher", "Javelin Rocket Launcher", "Carl Gustaf Recoilless Rifle", "Panzerfaust 3 Rocket Launcher", "SMAW Rocket Launcher", "M202 FLASH Rocket Launcher"]
mythic = ["Juggernaut Suit + M61 Minigun" , "EOD Suit + M4A1 Assault Rifle" , "Ghillie Suit +  SILENCED Remington 700 Sniper Rifle"]
coins = 100
inventory = []
chests_opened = 0
items_collected = 0
items_sold = 0
player_level = 1
player_xp = 0
xp_to_next_level = 100
rarest_rarity = "None"
highest_rarity_value = 0
lucky_charm = 0
xp_booster = 0
coin_multiplier = 0
chest_discount = 0
print(f"You start with {coins} coins!")
while True:
    answer = input(
        "[ENTER] Open Chest | [INVENTORY] View Inventory | [SELL] Sell Items | [STATS] Player Stats | [SHOP] Shop | [EXIT] Quit\n"
    )
    if answer.upper() == "SHOP":
        print("\n========== SHOP ==========")
        print(f"1. Lucky Charm - Level {lucky_charm}")
        print(f"2. XP Booster - Level {xp_booster}")
        print(f"3. Coin Multiplier - Level {coin_multiplier}")
        print(f"4. Chest Discount - Level {chest_discount}")
        print("==================================")
        shop_choice = input("Choose an upgrade (1-4) or EXIT: ")
        if shop_choice == "1":
            cost = 100 * (lucky_charm + 1)
            if coins >= cost:
                coins -= cost
                lucky_charm += 1
                print("\033[92mLucky Charm upgraded!\033[0m")
            else:
                print("\033[91mNot enough coins!\033[0m")
        elif shop_choice == "2":
            cost = 150 * (xp_booster + 1)

            if coins >= cost:
                coins -= cost
                xp_booster += 1
                print("\033[92mXP Booster upgraded!\033[0m")
            else:
                print("\033[91mNot enough coins!\033[0m")
        elif shop_choice == "3":
            cost = 200 * (coin_multiplier + 1)

            if coins >= cost:
                coins -= cost
                coin_multiplier += 1
                print("\033[92mCoin Multiplier upgraded!\033[0m")
            else:
                print("\033[91mNot enough coins!\033[0m")
        elif shop_choice == "4":
            cost = 250 * (chest_discount + 1)

            if coins >= cost:
                coins -= cost
                chest_discount += 1
                print("\033[92mChest Discount upgraded!\033[0m")
            else:
                print("\033[91mNot enough coins!\033[0m")
        continue
    if answer.upper() == "STATS":
        print("\n========== PLAYER STATS ==========")

        print(f"\033[93m Current Balance: {coins} coins\033[0m")
        print(f"\033[34m Chests Opened: {chests_opened}\033[0m")
        print(f"\033[92m Items Collected: {items_collected}\033[0m")
        print(f"\033[91m Items Sold: {items_sold}\033[0m")
        print(f"\033[95m Rarest Item Rarity: {rarest_rarity.upper()}\033[0m")
        print(f"\033[93m Player Level: {player_level}\033[0m")
        print(f"\033[96m Player XP: {player_xp}/{xp_to_next_level}\033[0m")

        print("==================================")
        continue
    if answer.upper() == "INVENTORY":
        print("\n========== YOUR INVENTORY ==========")
        if len(inventory) == 0:
            print("Your inventory is empty!")
        else:
            for i, item in enumerate(inventory, start=1):
                print(f"{i}. {item[0]} - {item[1]} coins")
            total_value = sum(item[1] for item in inventory)
            print(f"\nTotal Inventory Value: {total_value} coins")
        print("====================================")
        continue
    if answer.upper() == "SELL":
            if len(inventory) == 0:
                print("Your inventory is empty!")
            else:
                print("\n========== SELL WEAPONS ==========")
                for i, item in enumerate(inventory, start=1):
                    print(f"{i}. {item[0]} - {item[1]} coins")
                number = input("Choose a weapon to sell: ")
                if number.isdigit():
                    index = int(number) - 1
                    if 0 <= index < len(inventory):
                        weapon, value = inventory.pop(index)
                        bonus_value = int(value * (1 + coin_multiplier * 0.10))
                        coins += bonus_value
                        print(f"You sold {weapon} for {value} coins!")
                    else:
                        print("Invalid weapon number!")
                else:
                    print("Please enter a number!")
            print(f"Your balance: {coins} coins")
            continue
    if answer.upper() == "EXIT":
        confirm = input("Are you sure you want to quit? (YES/NO): ")
        if confirm.upper() == "YES":
            print("Thanks for playing LootBox Simulator!")
            break
        else:
            print("Returning to the game...")
            continue
    if coins < 20:
        print("Not enough coins! You can still manage your inventory.")
        continue
    chest_cost = max(5, 20 - (chest_discount * 2))
    coins -= chest_cost
    print(f"You spent 20 coins! You now have {coins} coins.")
    print("You opened a chest!")
    chests_opened += 1
    xp_gain = 25 + (xp_booster * 10)
    player_xp += xp_gain
    print(f"\033[96mYou earned {xp_gain} XP!\033[0m")
    print(f"You earned 25 XP! ({player_xp}/{xp_to_next_level})")
    if player_xp >= xp_to_next_level:
        player_xp -= xp_to_next_level
        player_level += 1
        xp_to_next_level = int(xp_to_next_level * 1.15)
        print("\033[93m")
        print("██╗     ███████╗██╗   ██╗███████╗██╗         ██╗   ██╗██████╗")
        print("██║     ██╔════╝██║   ██║██╔════╝██║         ██║   ██║██╔══██╗")
        print("██║     █████╗  ██║   ██║█████╗  ██║         ██║   ██║██████╔╝")
        print("██║     ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║         ██║   ██║██╔═══╝")
        print("███████╗███████╗ ╚████╔╝ ███████╗███████╗    ╚██████╔╝██║")
        print("╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚══════╝     ╚═════╝ ╚═╝")
        print(f"\n              PLAYER LEVEL: {player_level}")
        print("\033[0m")
    rarity = random.choices(
        ["common", "rare", "legendary", "mythic"],
        weights=[
            max(10, 60 - lucky_charm * 7),
            25 + lucky_charm * 2,
            12 + lucky_charm * 3,
            3 + lucky_charm * 2
        ],
    )[0]
    rarity_values = {
        "common": 1,
        "rare": 2,
        "legendary": 3,
        "mythic": 4
    }

    if rarity_values[rarity] > highest_rarity_value:
        highest_rarity_value = rarity_values[rarity]
        rarest_rarity = rarity
    if rarity == "common":
        weapon = random.choice(common)
        color = "\033[37m"
        value = 10
    elif rarity == "rare":
        weapon = random.choice(rare)
        color = "\033[34m"
        value = 25
    elif rarity == "legendary":
        weapon = random.choice(legendary)
        color = "\033[33m"
        value = 75
    else:
        weapon = random.choice(mythic)
        color = "\033[31m"
        value = 250
    print(f"{color}You got a {rarity.upper()} weapon: {weapon}!\033[0m")
    print(f"{weapon} is now in your inventory!")
    choice = input("Do you want to SELL or KEEP this weapon? ").lower()
    if choice == "keep":
        inventory.append((weapon, value))
        items_collected += 1
        print(f"{weapon} added to your inventory!")
    elif choice == "sell":
        bonus_value = int(value * (1 + coin_multiplier * 0.10))
        coins += bonus_value
        items_sold += 1
        print(f"You sold {weapon} for {value} coins!")
    else:
        print("Invalid choice!")
    print(f"Your balance: {coins} coins")
    if coins < 20 and len(inventory) == 0:
        print("\033[31m")



        print(" ██████╗  █████╗ ███╗   ███╗███████╗")
        print("██╔════╝ ██╔══██╗████╗ ████║██╔════╝")
        print("██║  ███╗███████║██╔████╔██║█████╗  ")
        print("██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ")
        print("╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗")
        print(" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝")

        print(" ██████╗ ██╗   ██╗███████╗██████╗ ")
        print("██╔═══██╗██║   ██║██╔════╝██╔══██╗")
        print("██║   ██║██║   ██║█████╗  ██████╔╝")
        print("██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
        print("╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
        print(" ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")

        print("You have no coins and no weapons!")
        break
