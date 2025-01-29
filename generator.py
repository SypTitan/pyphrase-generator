import random
import argparse

ADJECTIVES: tuple[str] = (
    "red", "blue", "green", "yellow", "purple", "orange", "black", "white", "gray", "brown",
    "tall", "short", "big", "small", "tiny", "huge", "wide", "narrow", "thick", "thin",
    "fast", "slow", "hot", "cold", "warm", "cool", "bright", "dark", "loud", "quiet",
    "soft", "hard", "rough", "smooth", "sharp", "dull", "clean", "dirty", "dry", "wet",
    "new", "old", "young", "fresh", "stale", "rich", "poor", "full", "empty", "light",
    "heavy", "strong", "weak", "bold", "shy", "brave", "calm", "wild", "tame", "sweet",
    "sour", "bitter", "mild", "spicy", "flat", "round", "square", "deep", "shallow", "high",
    "low", "long", "quick", "slow", "busy", "lazy", "proud", "wise", "funny", "stern",
    "kind", "mean", "nice", "neat", "messy", "plain", "fancy", "rare", "pure", "raw",
    "ripe", "safe", "sick", "sore", "tidy", "vast", "warm", "wise", "real", "main"
)

NOUNS: tuple[str] = (
    "time", "door", "tree", "bird", "fish", "book", "hand", "star", "ring", "king",
    "queen", "heart", "fire", "rain", "snow", "wind", "moon", "ship", "road", "path",
    "house", "chair", "table", "wall", "floor", "roof", "food", "bread", "milk", "meat",
    "fruit", "apple", "stone", "sand", "lake", "river", "hill", "cloud", "storm", "light",
    "sound", "voice", "child", "horse", "sheep", "plant", "grass", "leaf", "wood", "metal",
    "glass", "gold", "paper", "clock", "wheel", "train", "plane", "sword", "shield", "crown",
    "bridge", "tower", "gate", "cave", "farm", "field", "coast", "beach", "world", "earth",
    "water", "ocean", "game", "song", "film", "story", "money", "work", "room", "card",
    "tooth", "hair", "face", "head", "foot", "nose", "mind", "gift", "shop", "town",
    "city", "park", "dream", "life", "hope", "friend", "baby", "bird", "dog", "cat"
)

def generate_adjective() -> str:
    return random.choice(ADJECTIVES)

def generate_noun() -> str:
    return random.choice(NOUNS)

def generate_random_word() -> str:
    return random.choice([generate_adjective, generate_noun])()

def generate_phrase(length: int = 4) -> str:
    if (length < 1):
        return ""
    elif (length == 1):
        return generate_random_word()
    else:
        out: str = ""
        out += generate_adjective()
        for i in range(1, length - 1):
            out += " " + generate_random_word()
        out += " " + generate_noun()
        return out
    
def generate_pascal_phrase(length: int = 4) -> str:
    return generate_phrase(length).title()

def positive(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError(f"Length must be a positive integer, not {value}")
    return number

def main_cli():
    parser = argparse.ArgumentParser(description="Generate a random phrase")
    parser.add_argument("-l", "--lowercase", action="store_true", help="Generate a fully lowercase passphrase")
    parser.add_argument("length", type=positive, nargs="?", help="The number of words in the phrase", default=4)
    
    args = parser.parse_args()
    
    if args.lowercase:
        print(generate_phrase(args.length))
    else:
        print(generate_pascal_phrase(args.length))

if __name__=="__main__":
    l: int = 4
    i: str = ""
    while i != "exit":
        i = input("Enter a number of words to generate (or 'exit' to quit): ")
        try:
            l = int(i)
            print("\t" + generate_pascal_phrase(l))
        except:
            if i != "exit":
                print("Invalid input. Please enter a number.")