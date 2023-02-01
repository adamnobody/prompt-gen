import random

girlsNumber = ["1girl", "2girls", "3girls"]

censorship = ["censored", "nude"]

typeP = ["full_growth", "bust", "portrait"]

pose = ["victory", "bunny", "69", "random", "missionary", "doggy_style"]

skinColor = ["light", "black"]

outfit = ["dress", "swimsuit", "school_uniform", "bunnysuit", "lingerie", "cleavage", "suit", "t-shirt", "skirt"]
outfitColor = ["white", "black", "red", "gray", "green", "yellow", "purple"]

accessories = ["hat", "umbrella", "no_accessories", "smartphone", "watch", "choker", "bows"]

jewelry = ["no_jewelry", "necklace", "medallion", "gems", "bracelet"]

hairLong = ["cut", "long", "very_long"]
hairColor = ["blonde", "black", "green", "red", "blue", "brown", "strawberry_blonde", "golden_blonde"]

eyesColor = ["blue", "green", "brown", "yellow", "dark", "red", "amber", "gray"]

breasts = ["small", "medium", "big", "huge", "very_huge"]

ass = ["small", "big", "huge"]

background = ["white_background", "swimming_pool", "forest", "bedroom", "mountain_background", "green_valley_background", "beach", "classroom", "sky", "street"]

style = ["art by rutkowski", "realistic", "anime", "oil painting"]

negative = "Negative prompt:\nworst quality, bad anatomy, deformed hands, deformed face, deformed breasts, text, watermark, JPEG artefacts"

prompt = f"Prompt:\n{random.choice(girlsNumber)},{random.choice(censorship)}, {random.choice(typeP)}, {random.choice(pose)}_pose, {random.choice(skinColor)}_skin, pussy, {random.choice(outfitColor)}_{random.choice(outfit)}, {random.choice(accessories)}, {random.choice(jewelry)},{random.choice(hairColor)}_{random.choice(hairLong)}_hair, {random.choice(eyesColor)}_eyes, {random.choice(breasts)}_breasts, nipples, {random.choice(ass)}_ass, {random.choice(background)}, {random.choice(style)}"
print(prompt)
print(negative)