from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=2,
    downloader_threads=8,
    storage={'root_dir':'./crawl_img'})

filters = dict(
    size='medium',
    type='photo',
    
   # color='orange',
    #license='commercial,modify',
    date=((2010,1,1),(2018,4,30))

)

google_crawler.crawl(keyword='보행자',filters=filters,max_num=500,file_idx_offset=0,language='ko')


