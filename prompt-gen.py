import random
from colorama import init, Fore

girlsNumber = ["1girl", "2girls", "3girls"]

censorship = ["censored", "nude"]

typeP = ["full_growth", "bust", "portrait"]

pose = ["victory", "bunny", "69", "missionary", "doggystyle"]

skinColor = ["light", "black"]

outfitColor = ["white", "black", "red", "gray", "green", "yellow", "purple"]
outfit = ["dress", "swimsuit", "school_uniform", "bunnysuit", "lingerie", "cleavage", "suit", "t-shirt", "skirt"]

accessories = ["hat", "umbrella", "no_accessories", "smartphone", "watch", "choker", "bows"]

jewelry = ["no_jewelry", "necklace", "medallion", "gems", "bracelet"]

hairLong = ["cut", "long", "very long"]
hairColor = ["blonde", "black", "green", "red", "blue", "brown", "strawberry blonde", "golden blonde"]

eyesColor = ["blue", "green", "brown", "yellow", "dark", "red", "amber", "gray"]

breasts = ["small", "medium", "big", "huge", "very huge"]

ass = ["small", "big", "huge"]

background = ["white background", "swimming pool", "forest", "bedroom", 
              "mountain background", "green valley background", "beach", 
              "classroom", "sky", "street"]

style = ["art by rutkowski", "realistic", "anime", "oil painting"]

tags = [girlsNumber, censorship, typeP, pose, skinColor, 
       outfitColor, outfit, accessories, jewelry, hairLong, 
       hairColor, eyesColor, breasts, ass, background, style]

negative = "worst quality, bad anatomy, deformed hands, deformed face, deformed breasts, text, watermark, JPEG artefacts"

prompt = ""
for i in range(len(tags)):
    if tags[i] == pose:
        prompt += f"{random.choice(tags[i])} pose, "

    elif tags[i] == skinColor:
        prompt += f"{random.choice(tags[i])} skin, "

    elif tags[i] == outfitColor:
        prompt += f"{random.choice(tags[i])} "

    elif tags[i] == hairLong or tags[i] == hairColor:
        prompt += f"{random.choice(tags[i])} hair, "

    elif tags[i] == eyesColor:
        prompt += f"{random.choice(tags[i])} eyes, "

    elif tags[i] == breasts:
        prompt += f"{random.choice(tags[i])} breasts, "

    elif tags[i] == ass:
        prompt += f"{random.choice(tags[i])} ass, "

    else:
        prompt += f"{random.choice(tags[i])}, "

print(f"Prompt:\n{Fore.GREEN}{prompt}pussy\n{Fore.WHITE}Negative prompt:\n{Fore.GREEN}{negative}")
print(f"""{Fore.WHITE}For this generation, I recommend using \"Euler a\", \"DDIM\" or \"DPM++\" sampler methods:
    \"Euler a\" - 25-35 steps.
    \"DDIM\" - 30-40 steps.
    \"DMP++\" methods - 20-30 steps.
Resolution for generations - 512x768.
CFG Scale - 7-10.""")











