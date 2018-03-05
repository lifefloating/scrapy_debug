from scrapy import cmdline

'''debug用'''
name = 'yourspidername'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())