>markdown_rules: https://markdown.tw/#overview
## 1.T C P / I P协议族分四层协议:
1.  链路层，有时也称作数据链路层或网络接口层，通常包括操作系统中的设备驱动程序和计算机中对应的网络接口卡。
    它们一起处理与电缆（或其他任何传输媒介）的物理接口细节。A R P（地址解析协议）和R A R P（逆地址解析协
    议）是某些网络接口（如以太网和令牌环网）使用的特殊协议，用来转换I P层和网络接口层使用的地址。
2.  网络层,用于处理分组在网络中的活动，例如分组的选路。在T C P / I P协议族中，网络层协议包括I P协议（网际
    协议），I C M P协议（I n t e r n e t互联网控制报文协议），以及I G M P协议（I n t e r n e t组管理协
    议）。I C M P是I P协议的附属协议，I P层用它来与其他主机或路由器交换错误报文和其他重要信息，应用程序也
    有可能访问它。I G M P用来把一个U D P数据报多播到多个主机。
3.  运输层，为两台主机上的应用程序提供端到端的通信。T C P把应用程序交给它的数据分成合适的小块交给下面的网络
    层，确认接收到的分组，设置发送最后确认分组的超时时钟等。由于运输层提供了高可靠性的端到端的通信，因此应用
    层可以忽略所有这些细节。U D P把称作数据报的分组从一台主机发送到另一台主机，但并不保证该数据报能到达另一
    端。
4.  应用层负责处理特定的应用程序细节。
>   路由器( R o u t e r )，从历史上说，这些盒子称作网关（ g a t e w a y）。现在网关这个术语只用来表示应用
    层网关：一个连接两种不同协议族的进程？

IP分类。是32位地址,开头不同:
* A: 0网络号7位，主机号24位
* B: 10网14主16--从128.0.0.0-191.255.255.255
* C: 110网21主8
* D: 1110多播组号28位
* E: 11110待用27位
>   互联网络信息中心（ Internet Network InformationC e n t r e），称作I n t e r N I C。I n t e r N I C只分
    配网络号，为接入互联网的网络分配I P地址。主机号的分配由系统管理员来负责。域名系统（ D N S）是一个分布的数据库
    ，由它来提供I P地址和主机名之间的映射信息.
    
### 1.1数据进入协议栈时封装，将数据加上报文（message）首部、尾部信息
1.  I P传给网络接口层的数据单元称作I P数据报(IP datagram)。通过以太网传输的比特流称作帧(Fr a m e )。以太网数据帧
    的物理特性是其长度必须在4 6～1 5 0 0字节之间（不含以太网首部14字节及以太网尾部4字节，含IP首部20字节及TCP首部20字
    节，若为udp首部则为8字节）？I P首部中加入某种标识，以表明数据属于哪一层，占8bit（=1字节），称作协议域。T C P和U D P
    都用一个1 6 b i t（=2字节）的端口号来表示不同的应用程序。T C P和U D P把源端口号和目的端口号分别存入报文首部中。
2.  当目的主机收到一个以太网数据帧时，数据就开始从协议栈中由底向上升，同时去掉各层协议加上的报文首部。每层协议盒都要
    去检查报文首部中的协议标识，以确定接收数据的上层协议。
3.  服务器的知名端口号是固定的。客户端口号又称作临时端口号，通常只是在用户运行该客户程序时才存在，大多数T C P / I P实
    现给临时端口分配1 0 2 4～5 0 0 0之间的端口号。
>   i n t e r n e t意思是用一个共同的协议族把多个网络连接在一起。而I n t e r n e t指的是世界范围内通过T C P / I P互
    相通信的所有主机集合（超过1 0 0万台）。I n t e r n e t是一个i n t e r n e t，但i n t e r n e t不等于I n t e r n e t。
4.  应用编程接口: 使用T C P / I P协议的应用程序通常采用两种应用编程接口（ A P I）：s o c k e t和T L I（Transport Layer Interface）

## 2.链路层
### 2.1三个目的:
1.  为I P模块发送和接收I P数据报；
2.  为A R P模块发送A R P请求和接收A R P应答
3.  为R A R P发送R A R P请求和接收R A R P应答。
### 2.2 首尾部结构
常见协议： 以太网协议和IEEE 802协议

*   以太网协议和IEEE 802协议的链路层首部14字节包含6字节目的地址，6字节源地址，2字节长度，地址指硬件地址，需要通过A R P和R A R P
    协议（第4章和第5章）对32 bit的I P地址和48 bit的硬件地址进行映射。链路层尾部4字节为C R C字段（或F C S，帧检验序列），是一个循
    环冗余检验码，以检测数据帧中的错误。

*   SLIP（Serial Line IP）：串行线路IP，是一种在串行线路上对I P数据报进行封装的简单形式。IP数据报以一个称作E N D（0 x c 0）的特
    殊字符结束。同时，为了防止数据报到来之前的线路噪声被当成数据报内容，大多数实现在数据报的开始处也传一个E N D字符（如果有线路噪声
    ，那么E N D字符将结束这份错误的报文。速率通常较低（ 19200 b/s或更低）
*   PPP：（peer-to-peer-protocol）点对点协议，修改了S L I P协议中的所有缺陷。(1) PPP支持在单根串行线路上运行多种协议，不只是I P协议；(2) 每一帧都有循环冗
    余检验； (3) 通信双方可以进行I P地址的动态协商(使用I P网络控制协议)； (4) 与C S L I P类似，对T C P和I P报文首部进行压缩；
    (5) 链路控制协议可以对多个数据链路选项进行设置。
*   环回接口（ Loopback Interface）允许运行在同一台主机上的客户程序和服务器程序通过T C P / I P进行通信，即I P地址1 2 7 . 0 . 0
    . 1分配给这个接口
