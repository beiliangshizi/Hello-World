# NovelDownloaderbyPython
使用爬虫爬取顶点小说网小说，涉及selenium、PhantomJS、anaconda等
思路：
使用 selenium + PhantomJS 模拟浏览器访问 顶点小说网 首页；
用户输入下载的书名，然后找到首页搜索框的，输入书名，再模拟点击回车进行搜索；
浏览器切换到搜索页界面，并且返回搜索结果页第一页 JS 渲染后的源码，一般搜索的书都会出现在第一页，这个大家应该都知道；
根据用户输入的书名匹配到小说对应的链接；
得到小说全部章节的 url，然后访问每个章节，使用正则匹配所有章节的文章内容；
开启多进程，增加抓取速度，内容保存对应文件夹。
