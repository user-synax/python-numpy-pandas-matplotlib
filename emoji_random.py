import numpy as np

rng = np.random.default_rng()
emojis = np.array(['😀', '😂', '😍', '😎', '🤔', '🙈', '👻','🎉', '🚀'])
random_emojis = rng.choice(emojis, size=(5, 5))
print(random_emojis)