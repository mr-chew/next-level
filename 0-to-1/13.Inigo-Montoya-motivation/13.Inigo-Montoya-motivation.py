import random
from pathlib import Path

data_folder = Path("data/")
file_to_open = data_folder / "motivation.txt"
quotes = file_to_open.read_text().splitlines()
print(random.choice(quotes)