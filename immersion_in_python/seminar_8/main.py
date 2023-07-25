import csv
import json
import os
import pickle


def get_size_dir(directory):
    total_size = 0
    for path_to_dir, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(path_to_dir, filename)
            total_size += os.path.getsize(filepath)
    return total_size


def traverse_and_save(directory):
    results = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        item_type = "file" if os.path.isfile(item_path) else "directory"

        if item_type == "file":
            item_size = os.path.getsize(item_path)
        else:
            item_size = get_size_dir(item_path)

        item_info = {
            "name": item,
            "type": item_type,
            "size": item_size,
            "parent_directory": directory
        }
        results.append(item_info)

        if item_type == "directory":
            results.extend(traverse_and_save(item_path))

    return results


def save_to_files(data, file_path):
    with open(file_path + ".json", "w") as file:
        json.dump(data, file, indent=2)

    with open(file_path + ".csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    with open(file_path + ".pickle", "wb") as file:
        pickle.dump(data, file)


# Пример использования
current_dir = "./"
result_data = traverse_and_save(current_dir)

# Сохранение результатов в файлы
save_to_files(result_data, "result")
