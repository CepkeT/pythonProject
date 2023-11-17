def draw_tree():
    print("   ^   ")
    print("  /|\  ")
    print(" / | \ ")
    print("/__|__\\")
    print("   |   ")


def draw_forest(num_trees):
    for _ in range(num_trees):
        draw_tree()
        print()


def draw_hand_forest(num_forests):
    for _ in range(num_forests):
        draw_forest(5)  # Adjust the number of trees in each forest here
        print()


num_forests = 3  # Adjust the number of forests here
draw_hand_forest(num_forests)
