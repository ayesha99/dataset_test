from icrawler.builtin import GoogleImageCrawler

def google_crawl():
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

    google_crawler.crawl(keyword='차량 삼각대',filters=filters,max_num=2000,file_idx_offset=0)

from icrawler.builtin import BingImageCrawler

def bing_crawl():
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

    bing_crawl.crawl(keyword='차량 삼각대',filters=filters,max_num=2000,file_idx_offset=1000)



#google_crawl()
bing_crawl()

