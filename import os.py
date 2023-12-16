import os

folder_path = r'H:\Switch Mod Master\Repositories\XGC_Pokedexs\Dexs\Sprite Image Dexs\Shiny Sprite Dex'

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.startswith("b_") and filename.endswith(".png"):
            base_number, *rest = filename[2:].split("-", 1)
            new_name = f"{base_number}S_{rest[0].replace('s', '')}" if rest else f"{base_number}.png"
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} to {new_name}")

if __name__ == "__main__":
    rename_files(folder_path)
