import os

__all__ = ["number_count", "file_rename"]


def number_count(self, step=1, start=1, end=5):
    current_number = start

    while current_number <= end:
        if step == 1:
            return str(current_number)
        elif step == 2:
            return str(current_number).zfill(2)


def file_rename(step=2,
                enj='txt',
                enj_end='txt',
                num_start=3,
                num_end=6,
                folder_path="."):
    file_list = os.listdir(folder_path)
    for file in file_list:
        lst = file.split('.')
        if len(lst) > 1:
            if len(lst[0]) >= num_end and lst[1] == enj:
                num = number_count(step, num_start, len(file_list))
                old_name = f"{lst[0]}.{lst[1]}"
                new_name = f"{lst[0][num_start:num_end]}-{num}.{enj_end}"
                try:
                    os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, new_name))
                except Exception as ex:
                    print(f'{ex}')
                finally:
                    num_start += 1
            elif len(lst[0]) <= num_end and lst[1] == enj:
                num = number_count(step, num_start, len(file_list))
                old_name = f"{lst[0]}.{lst[1]}"
                new_name = f"{lst[0]}{num}.{enj_end}"
                os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, new_name))
