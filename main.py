import os
import shutil
import logging
import logging.handlers
import requests
from lxml import etree
import numpy as np
import cv2
import random

root_url = 'https://wallhaven.cc/'
headers = {
    'Referer': 'https://wallhaven.cc/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/94.0.4606.61 Safari/537.36',
}

logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(rf_handler)

def download_img(url):
    img_name = url.split('/')[-1]
    img_path = "C:\\Users\\kruse\\Pictures\\downloads\\" + img_name
    resp = requests.get(url, headers=headers, stream=True, timeout=5)

    img = np.asarray(bytearray(resp.raw.read()), dtype='uint8')
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    h, w, _ = img.shape
    # if h / 9 == w / 16:
    res = float(w) / h
    if 1.5 < res < 2.5:
        cv2.imwrite(img_path, img, [cv2.IMWRITE_JPEG_QUALITY, 100])
        logger.info("get raw img success: " + url)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # resp = requests.get(url, headers=headers)
    # with open(img_name, 'wb') as f:
    #     f.write(resp.content)


def get_page(url):
    try:
        page_id = random.randint(1, 90)
        url = url + '?page=' + str(page_id)
        logger.debug("page number: " + str(page_id))

        page = requests.get(url, headers=headers)
        page.raise_for_status()
        html_page = etree.HTML(page.text)
        pre_urls = html_page.xpath('//li/figure/a/@href')

        for i in range(1, 5):
            index = random.randint(0, len(pre_urls) - 1)
            img_url = pre_urls[index]

            logger.debug("attempt loading img preview: " + img_url)

            img_page = requests.get(img_url, headers=headers)
            img_html = etree.HTML(img_page.text)
            raw_url = img_html.xpath('//main//img/@src')
            download_img(raw_url[0])

    except requests.HTTPError as e:
        print(e)
    except Exception as e:
        print(e)



def del_and_copy(src_dir, dst_dir, img_list):
    logger.debug("clean old imgs...")
    shutil.rmtree(dst_dir)
    os.mkdir(dst_dir)
    for img_name in img_list:
        src_path = os.path.join(src_dir, img_name)
        dst_path = os.path.join(dst_dir, img_name)
        shutil.move(src_path, dst_path)
    logger.debug("clean over!")


if __name__ == '__main__':
    # LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    # DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    # logging.basicConfig(filename="crawl.log", level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)
    urls = [root_url + 'toplist']
    src_dir = "C:\\Users\\kruse\\Pictures\\downloads"
    dst_dir = "C:\\Users\\kruse\\Pictures\\bak"
    img_list = os.listdir(src_dir)
    for i in range(1, 5):
        index = random.randint(0, len(urls) - 1)
        url = urls[index]
        logger.debug("Wallpaper class: " + url)
        get_page(url)
    # get_page(root_url + 'search?q=like%3Ak7lxxq')
    del_and_copy(src_dir, dst_dir, img_list)
    logger.info("end")
