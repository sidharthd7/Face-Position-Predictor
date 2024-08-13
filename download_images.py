from icrawler.builtin import GoogleImageCrawler
import time 
import os

def crawl_images(keyword, max_num, storage_dir):
    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)
    
    crawler = GoogleImageCrawler(storage={'root_dir': storage_dir})
    crawler.crawl(keyword=keyword, max_num=max_num)
    
base_dir = 'dataset'

crawl_images('face looking left side portrait side profile', max_num=20, storage_dir=os.path.join(base_dir, 'left'))

time.sleep(2)

crawl_images('face looking right side portrait', max_num=20, storage_dir=os.path.join(base_dir, 'right'))

time.sleep(2)

crawl_images('front face portrait profile pic', max_num=10, storage_dir=os.path.join(base_dir, 'front'))


    