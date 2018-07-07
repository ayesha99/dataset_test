from icrawler.builtin import GoogleImageCrawler
import threading

def google_crawl(keyword,offset=0):
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

    google_crawler.crawl(keyword=keyword,filters=filters,max_num=50,file_idx_offset=offset)
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


from datetime import date
from icrawler.builtin import BaiduImageCrawler
def baidu_crawl(keyword):
    baidu_crawler = BaiduImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=32,
        storage={'root_dir': './crawl_img'})
    baidu_crawler.crawl(keyword=keyword, offset=0, max_num=50,
                    min_size=(400,400), max_size=None)



#google + bing crawler
def runCrawl(keyword):
    t1 = threading.Thread(target=google_crawl,args=(keyword,))
    t2 = threading.Thread(target=bing_crawl,args=(keyword,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('finished crawling')

keyword = '앰뷸런스'
google_crawl("불꽃신호기",0)
google_crawl("안전삼각대",50)
google_crawl("개",100)
google_crawl("고양이",150)
google_crawl("고라니",200)
google_crawl("보행자",250)
google_crawl("소방차",300)
google_crawl("구급차",350)
#runCrawl(keyword) #google + bing crawling
#google_crawl(keyword)
#bing_crawl(keyword)

