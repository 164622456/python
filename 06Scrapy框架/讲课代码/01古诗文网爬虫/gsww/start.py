from scrapy import cmdline

# "scrapy crawl gsww_spider".split(" ")
cmds = ['scrapy','crawl','gsww_spider']
cmdline.execute(cmds)