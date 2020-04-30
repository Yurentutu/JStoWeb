import urllib.request
import urllib.parse

try:
    province = urllib.parse.quote("广东")
    city = urllib.parse.quote("深圳")
    data ="province="+province+"&city="+city

    #post方法向服务器发送数据,并接收返回的html页面
    data = data.encode()
    html = urllib.request.urlopen("http://127.0.0.1:5000",data = data)#data参数接收二进制数据

    #get方法向服务器发送数据,并接收返回的html页面
    #url = "http://127.0.0.1:5000?province="+province+"&city="+city#方法一
    #html = urllib.request.urlopen("http://127.0.0.1:5000?"+data)#方法二
    #html = urllib.request.urlopen(url)


    html = html.read()
    html = html.decode()
    print(html)
except Exception as err:
    print(err)
