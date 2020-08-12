import re
import sys
import requests
from urllib import error

num = 0
numPicture = 0
file = ''
List = []
fl = open('./downpic.txt', mode='w')
def dowmloadPicture(html, keyword):
    global num
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)  # 先利用正则表达式找到图片url
    fl.write('找到关键词:' + keyword + '的图片，开始下载图片...'+ "\n")
    for each in pic_url:
        fl.write('下载的第' + str(num + 1) + '张图片，图片地址:' + str(each) + "\n")
        try:
            if each is not None:
                pic = requests.get(each, timeout=7)
            else:
                continue
        except BaseException:
            fl.write('错误，当前图片无法下载')
            continue
        else:
            string = file + r'\\' + keyword + '_' + str(num) + '.jpg'
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()
            num += 1
        if num >= numPicture:
            return

if __name__ == '__main__':  # 主函数入口
    argv=sys.argv
    word = argv[1]
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='
    numPicture = int(argv[2],10)
    file = "./add_photo"
    t = 0
    tmp = url
    while t < numPicture:
        try:
            url = tmp + str(t)
            result = requests.get(url, timeout=10)
            #print(url)
        except error.HTTPError as e:
            #print('网络错误，请调整网络后重试')
            fl.write('网络错误，请调整网络后重试'+"\n")
            t = t + 60
        else:
            dowmloadPicture(result.text, word)
            t = t + 60

    fl.write("\n")
    fl.write("============================================="+ "\n")
    fl.write("              下载完成！"+ "\n")
    fl.write("============================================="+ "\n")
