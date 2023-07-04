import json
from pathlib import Path

from modules.utils.decryptor import decrypt_private_key


def load_json(filepath: Path | str):
    with open(filepath, "r") as file:
        return json.load(file)
    
def read_txt(filepath: Path | str):
    with open(filepath, "r") as file:
        return [row.strip() for row in file]
    
def call_json(result: list | dict, filepath: Path | str):
    with open(f"{filepath}.json", "w") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

def read_wallets(encryption, private_keys, password):
    keys = read_txt(private_keys)
    if encryption:
        return [decrypt_private_key(data, password).decode() for data in keys]
    return keys