#номер 2
import random
import time
from multiprocessing import Pool


def func():
    array = []
    for i in range(10 ** 6):
        array.append(random.randint(-100, 100))
    print(sum(array) % 2)


if __name__ == '__main__':
    print('В одном потоке:')

    t1 = time.time()
    for _ in range(4):
        func()
    print(time.time() - t1, 'секунд')

    print('В 4 потоках:')
    t1 = time.time()
    with Pool(4) as p:
        r = []
        for _ in range(4):
            r.append(p.apply_async(func))
        for a in r:
            a.wait()
    print(time.time() - t1, 'секунд')

from os import makedirs
from os.path import join
import requests
from concurrent.futures import ThreadPoolExecutor

r = requests.get('https://api.ipify.org/?format=json')
ip = r.json()['ip']
ip_info = requests.get(f'https://ipinfo.io/{ip}/geo')
dir = f'user_data/{ip}/'
makedirs(dir, exist_ok=True)
with open(join(dir, 'user_info.txt'), 'w', encoding='utf-8') as file:
    file.write(ip_info.text)
def download_doge():
    s = requests.Session()
    r = s.get('https://dog.ceo/api/breeds/image/random')
    img_url = r.json()['message']
    r = s.get(img_url)
    with open(join(dir, r.url.split('/')[-1]), 'wb') as f:
        f.write(r.content)
with ThreadPoolExecutor(4) as pool:
    for _ in range(12):
        pool.submit(download_doge)

