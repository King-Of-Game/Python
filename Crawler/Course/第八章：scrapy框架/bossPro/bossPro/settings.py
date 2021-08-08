# -*- coding: utf-8 -*-

# Scrapy settings for bossPro project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bossPro'
Hm_lvt_194df3105ad7148dcf2b98a91b5e727a = 1605272636, 1
SPIDER_MODULES = ['bossPro.spiders']
NEWSPIDER_MODULE = 'bossPro.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure log level to show log content
LOG_LEVEL = 'ERROR'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cookie': 'lastCity=100010000; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1605344272,1605414348,1605433881,1605440586; __fid=359feb99a2ef63e117a2126787aea581; __c=1605414348; __l=l=%2Fwww.zhipin.com%2Fc101280100%2F%3Fquery%3Dpython%26ka%3Dsel-city-101280100&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DmkG6TaIYhZqKYru9oMLuXPdyRsIBURWndpRcpgHf5Xj0VS5D7mOpqOPD6t0BnXvP%26wd%3D%26eqid%3D8923a17000007108000000065fb11446&g=&friend_source=0&friend_source=0; __a=71300573.1605328514.1605328514.1605414348.63.2.30.63; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1605443679; __zp_stoken__=af16bYXhuUQxmO34CNWJfRDkvdQdTdVAmOF00MSV0XnFSAgBlRm16AHIaVRc3NXN0FyB%2BDD10GDNKXilmCFARFioFP2IoBFMlFUQbDiwqFFRVbA5BDgZ8SgJMGmA7KlkmEXF0H3gAFxtIPGAFdA%3D%3D',
#     'referer': 'https://www.zhipin.com/c101280100/?query=python&ka=sel-city-101280100',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bossPro.middlewares.BossproSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'bossPro.middlewares.BossproDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'bossPro.pipelines.BossproPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
