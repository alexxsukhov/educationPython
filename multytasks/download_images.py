import asyncio
import os
import sys
import time
import requests
import threading
import multiprocessing


# Функция для скачивания изображения с указанного URL и сохранения его на диск
def download_image(url, folder):
    try:
        response = requests.get(url)
        response.raise_for_status()
        filename = os.path.join(folder, os.path.basename(url))
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Скачано: {url}")
    except Exception as e:
        print(f"Ошибка при скачивании {url}: {e}")


# Функция для обработки URL-адресов с использованием многопоточности
def download_images_multithread(urls, folder):
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_image, args=(url, folder))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Многопоточное скачивание завершено за {total_time:.2f} секунд")


# Функция для обработки URL-адресов с использованием многопроцессорности
def download_images_multiprocess(urls, folder):
    start_time = time.time()
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=download_image, args=(url, folder))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Многопроцессорное скачивание завершено за {total_time:.2f} секунд")


# Функция для асинхронного скачивания изображений
async def download_images_async(urls, folder):
    start_time = time.time()
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_image_async(url, folder))
        tasks.append(task)

    await asyncio.gather(*tasks)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Асинхронное скачивание завершено за {total_time:.2f} секунд")


# Функция для асинхронного скачивания изображения
async def download_image_async(url, folder):
    try:
        response = await asyncio.to_thread(requests.get, url)
        response.raise_for_status()
        filename = os.path.join(folder, os.path.basename(url))
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Скачано: {url}")
    except Exception as e:
        print(f"Ошибка при скачивании {url}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python download_images.py <папка_для_сохранения> <URL1> <URL2> ...")
        sys.exit(1)

    folder = sys.argv[1]
    urls = sys.argv[2:]

    if not os.path.exists(folder):
        os.makedirs(folder)

    print("Многопоточное скачивание:")
    download_images_multithread(urls, folder)

    print("\nМногопроцессорное скачивание:")
    download_images_multiprocess(urls, folder)

    print("\nАсинхронное скачивание:")
    asyncio.run(download_images_async(urls, folder))