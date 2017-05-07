#coding:utf-8
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class MyImagesPipeline(ImagesPipeline):


    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_url'])   #这里因为我这里的url不是数组

    # def file_path(self, request, response=None, info=None):
    #     img_uid=request.url.splite('/')[-1].splite('.')[0]
    #     print request.url
    #     print '-----------------------------------------------------------'
    #     print img_uid
    #     filename=u'full/image/{0}.jpg'.format(img_uid)
    #     return filename

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        print image_paths
        if not image_paths:
            raise DropItem("Item contains no images")

        return item

