
from generator import ADJECTIVES, NOUNS

def list_adjectives(prefix: str = "\t") -> str:
    return f"\n".join([prefix + str(i) for i in ADJECTIVES]) + "\n"

def list_nouns(prefix: str = "\t") -> str:
    return f"\n".join([prefix + str(i) for i in NOUNS]) + "\n"

def header(word_type) -> str:
    return f"<details>\n\t<summary><h2 style=\"display:inline-block\">{word_type} used in generation</h2></summary>\n\n"
    
def footer() -> str:
    return "</details>\n\n"

def generate_adjective_list() -> str:
    return header("Adjectives") + list_adjectives() + footer()

def generate_noun_list() -> str:
    return header("Nouns") + list_nouns() + footer()
        
if __name__=="__main__":    
    SAFE_LINES = 36
    
    with open("README.md", "r") as f:
        intro = f.readlines()
        
    intro = intro[:SAFE_LINES]
           
    with open("README.md", "w") as f:
        f.writelines(intro)
        
        f.write(generate_adjective_list())
        f.write(generate_noun_list())
        
        