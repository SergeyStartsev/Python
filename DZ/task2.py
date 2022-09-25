for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is",
                  not (x or y or z) == (not x and not y and not z))