import random

girlsNumber = ["1girl", "2girls", "3girls"]

censorship = ["censored", "nude"]

typeP = ["full_growth", "bust", "portrait"]

pose = ["victory_pose", "bunny_pose", "69 pose"]

skinColor = ["light", "black"]

outfit = ["dress", "swimsuit", "school_uniform", "lingerie", "suit", "t-shirt", "skirt"]
outfitColor = ["white", "black", "red", "gray", "green", "yellow", "purple"]

accessories = ["hat", "umbrella", "no_accessories", "smartphone", "watch", "choker", "bows"]

jewelry = ["no_jewelry", "necklace", "medallion", "gems", "bracelet"]

hairLong = ["cut", "long", "very_long"]
hairColor = ["blonde", "black", "green", "red", "blue", "brown", "strawberry_blonde", "golden_blonde"]

eyesColor = ["blue", "green", "brown", "yellow", "dark", "red", "amber", "gray"]

breasts = ["small", "medium", "big", "huge", "very_huge"]

background = ["white_background", "swimming_pool", "forest", "bedroom", "beach", "classroom", "sky", "street"]

prompt = f"{random.choice(girlsNumber)},{random.choice(censorship)}, {random.choice(typeP)}, {random.choice(pose)}, {random.choice(skinColor)}_skin, pussy, {random.choice(outfitColor)}_{random.choice(outfit)}, {random.choice(accessories)}, {random.choice(jewelry)},{random.choice(hairColor)}_{random.choice(hairLong)}_hair, {random.choice(eyesColor)}_eyes, {random.choice(breasts)}_breasts, nipples, {random.choice(background)}"
print(prompt)