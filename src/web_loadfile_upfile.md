#### web下载服务器程序和web文件客户端程序结合，就可以进行web下载文件

改程序先不带参数地访问https://127.0.0.1:5000,服务器会返回一个可以
下载的文件名称给客户端，客户端获取这个文件名称fileName，之后再采用把文件
名称放在地址栏后面的方式再次访问这个网站，即：
   
    data=urllib.request.urlopen(url+'?fileName='+urllib.parse.quote(fileName))
服务器就把该文件的二进制发给发送给客户端，客户端接收到就保存在本地


####web上传服务器程序和web文件客户端程序结合，就可以进行web上传
 
 - 客户端要上传二进制数据，要设置表头content-type的值为'application/octet-stream',
 设置时定义headers字典来指定content-type的值，即：
 
        headers={'content-type':'application/octet-stream'}
    
    表头要加入到http请求中，可以先定义一个urllib.request.Request
    对象如下：
    
        req=urllib.request.Request(url,data,headers)
      这个对象的第一个参数url是访问的网址，第二个参数data是要上传的数据，第三个参数
      headers就是表头字典