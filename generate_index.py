import os
import json

def is_image_file(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))

def generate_index(library_folder, output_file):
    index = {}

    for dirpath, _, filenames in os.walk(library_folder):
        image_files = [f for f in filenames if is_image_file(f)]
        if not image_files:
            continue

        # Strip base folder and normalize slashes
        rel_path = os.path.relpath(dirpath, library_folder).replace("\\", "/")
        parts = rel_path.split("/")

        if len(parts) == 1:
            top = parts[0]
            sub = "_root"
        else:
            top = parts[0]
            sub = parts[1]

        if top not in index:
            index[top] = {}
        if sub not in index[top]:
            index[top][sub] = []

        for f in image_files:
            index[top][sub].append(f"{rel_path}/{f}" if rel_path != "." else f)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)
    print(f"✅ {output_file} generated.")

if __name__ == "__main__":
    generate_index("games", "games_index.json")