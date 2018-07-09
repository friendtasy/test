import socket
import threading
#针对某ip进行端口探测
def pingport(ip,port):      #定义函数，传递ip及端口，打印有应用程序回响的ip及端口
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.settimeout(1)
    try:
        s1.connect((ip, port))
        print(f'{ip}:{port}是开放的')
        s1.close()
    except:
        #print(f'{ip}:{port}是关闭的')
        s1.close()


ip="163.177.151.110"      #定义ip
th=[]                   #线程池，基于硬件系统限制不应大于2000
x1=0                    #初始化变量
x2=0                    #初始化变量

while 1:
    if x1<=65536:
        if not x2==2000:     #线程池
            t1=threading.Thread(target=pingport,args=(ip,x1))     #创建线程及传参
            th.append(t1)                                         #加入到线程池
            t1.start()                                            #启动线程
            x1+=1                            #自加1
            x2+=1                            #自加1

        else:
            x2=0         #重新初始变量
            for x3 in th:   #线程池批量检查并等待所有线程结果才执行主线程
                x3.join()
            th=[]           #初始化线程池
            t1=threading.Thread(target=pingport,args=(ip,x1))   #条件分支词句也执行上面代码
            t1.start()
            t1.join()
            x1+=1     #对x1一样需自加

    else:
        break