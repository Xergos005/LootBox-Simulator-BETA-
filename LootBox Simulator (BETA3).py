import random
input("Welcome to LootBox Simulator! Press ENTER to continue...")
rarity = ["common", "rare", "legendary", "mythic"]
common = ["Scrapped Assault Rifle", "Makeshift Shotgun", "Rusted Revolver" , "Vintage Pistol" , "Homemade Crossbow" , "Broken Hunting Rifle" , "Old Double Barrel Shotgun"]
rare = ["AK-47 Assault Rifle", "MP5 Submachine Gun", "M4 Assault Rifle" , "SCAR-L Assault Rifle" , "Kriss Vector SMG" , "Desert Eagle Pistol" , "SPAS-12 Shotgun" , "FAMAS Assault Rifle" , "AA-12 Shotgun" , "Uzi	Submachine Gun" , "MAC-10 Submachine Gun" , "Remington 870 Shotgun" , "Mossberg 500 Shotgun" , "AUG A3 Assault Rifle" , "P90 Submachine Gun" , "Benelli M4 Shotgun" , "HK416 Assault Rifle" , "G36C Assault Rifle" , "MP7	Submachine Gun" , "Saiga-12	Shotgun" , "USAS-12	Shotgun" , "Origin-12 Shotgun"]
legendary = ["RPG-7 Rocket Launcher", "AWP Sniper Rifle", "Barrett M82 Sniper Rifle", "Remington 700 Sniper Rifle", "SVD Dragunov Sniper Rifle", "L96A1 Sniper Rifle", "M40A5 Sniper Rifle", "CheyTac M200 Sniper Rifle", "Mosin-Nagant Sniper Rifle" , "SR-25 Marksman Rifle", "MK14 EBR Marksman Rifle", "M110 Marksman Rifle", "SKS Marksman Rifle", "G28 Marksman Rifle", "SCAR-H DMR Marksman Rifle", "M14 Marksman Rifle" , "M72 LAW Rocket Launcher", "AT4 Rocket Launcher", "Javelin Rocket Launcher", "Carl Gustaf Recoilless Rifle", "Panzerfaust 3 Rocket Launcher", "SMAW Rocket Launcher", "M202 FLASH Rocket Launcher"]
mythic = ["Juggernaut Suit + M61 Minigun" , "EOD Suit + M4A1 Assault Rifle" , "Ghillie Suit +  SILENCED Remington 700 Sniper Rifle"]
coins = 100
inventory = []
print(f"You start with {coins} coins!")
while True:
    answer = input("Press ENTER to open a chest or type EXIT: ")
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
                        coins += value
                        print(f"You sold {weapon} for {value} coins!")
                    else:
                        print("Invalid weapon number!")
                else:
                    print("Please enter a number!")
            print(f"Your balance: {coins} coins")
            continue
    if answer.upper() == "EXIT":
        break
    if coins < 20:
        print("Not enough coins! You can still manage your inventory.")
        continue
    coins -= 20
    print(f"You spent 20 coins! You now have {coins} coins.")

    print("You opened a chest!")
    chosen_rarity = random.choices(
        rarity,
        weights=[60, 25, 12, 3],
        k=1
    )[0]
    if chosen_rarity == "common":
        weapon = random.choice(common)
        color = "\033[37m"
        value = 10
    elif chosen_rarity == "rare":
        weapon = random.choice(rare)
        color = "\033[34m"
        value = 25
    elif chosen_rarity == "legendary":
        weapon = random.choice(legendary)
        color = "\033[33m"
        value = 75
    else:
        weapon = random.choice(mythic)
        color = "\033[31m"
        value = 250
    print(f"{color}You got a {chosen_rarity.upper()} weapon: {weapon}!\033[0m")
    print(f"{weapon} is now in your inventory!")
    choice = input("Do you want to SELL or KEEP this weapon? ").lower()
    if choice == "keep":
        inventory.append((weapon, value))
        print(f"{weapon} added to your inventory!")
    elif choice == "sell":
        coins += value
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
