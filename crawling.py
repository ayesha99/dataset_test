from icrawler.builtin import GoogleImageCrawler
import threading

def google_crawl(keyword):
    google_crawler = GoogleImageCrawler(
        feeder_threads=4,
        parser_threads=4,
        downloader_threads=12,
        storage={'root_dir':'./crawl_img'})

    filters = dict(
        #size='large',
        type='photo',
        
    # color='orange',
        #license='commercial,modify',
        date=((2008,1,1),(2018,4,30))

    )

    google_crawler.crawl(keyword=keyword,filters=filters,max_num=2000,file_idx_offset=0)
    print("terminated google crawler")

from icrawler.builtin import BingImageCrawler

def bing_crawl(keyword):
    bing_crawl = BingImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=32,
        storage={'root_dir':'./crawl_img'})

    filters = dict(
        #size='large',
        type='photo',
        
    # color='orange',
        #license='commercial,modify',
        #date=((2010,1,1),(2018,4,30))

    )

    bing_crawl.crawl(keyword=keyword,filters=filters,max_num=2000,file_idx_offset=1000)
    print("terminated bing crawler")

#google + bing crawler
def runCrawl(keyword):
    t1 = threading.Thread(target=google_crawl,args=(keyword,))
    t2 = threading.Thread(target=bing_crawl,args=(keyword,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('finished crawling')

keyword = 'street people'
runCrawl(keyword) #google + bing crawling
#google_crawl(keyword)
#bing_crawl(keyword)

