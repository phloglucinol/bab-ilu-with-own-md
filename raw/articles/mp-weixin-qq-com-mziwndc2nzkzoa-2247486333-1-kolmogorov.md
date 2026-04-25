---
type: raw_article
source_url: http://mp.weixin.qq.com/s?__biz=MzIwNDc2NzkzOA%3D%3D&mid=2247486333&idx=1&sn=99a20286a3884d8158d58c9ad74f15a2
canonical_url: http://mp.weixin.qq.com/s?__biz=MzIwNDc2NzkzOA%3D%3D&mid=2247486333&idx=1&sn=99a20286a3884d8158d58c9ad74f15a2
source_domain: mp.weixin.qq.com
title: 柯尔莫哥洛夫（Kolmogorov）倒向方程之二
author: 
published_at: 
fetched_at: 2026-04-25T02:04:31Z
extractor: wechat_worker
content_hash: 02d888db143b7db471abaf6f07738d69d95b96af5c7ea671849a3b74bc92345a
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6Jrv12hmR3NovKFZdzw8h4ic43AtzNiaEG1lb8FpX25NWo5lr8RibqhTyQ/0.jpg) 

# 柯尔莫哥洛夫（Kolmogorov）倒向方程之二

原创 吕途 吕途 [ 做自由的人 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

背景回顾

 在文章《[布朗运动的程序动态演示](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwNDc2NzkzOA==&mid=2247485585&idx=1&sn=53e7dd4900a4e2f54864f93a752ed981&scene=21#wechat%5Fredirect)》中演示了布朗运动，如下图所示：在起点确定的情况下，终点是不确定的。

![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudR1aCBsAawzhhwAWfickM8ZtxM5Jhn5KgWicfAsR4RRjfNBo7A7bePKe8ia0JCAgR76x8GFtAlpnhRmg/640.png)图1

 因为终点是随机的，于是引出了终点的概率密度函数![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6atClXZWuIoiaUicG6UrAGia0VXP2ctMRTgzf13tOF3Skn2SwRYvQGJcQQ/640.png),概率密度函数是确定的。现在我们把终点固定，移动起点，观察概率密度函数的变化，即![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6TJSUp0zibDDhV3cbdxcxgdzv5iaOyuQiafhhM0eYvFcV7wvGYVGH8vPfg/640.png)，概率密度函数是变化的。这个变化的概率密度函数就是文章《[柯尔莫哥洛夫（Kolmogorov）倒向方程](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwNDc2NzkzOA==&mid=2247486304&idx=1&sn=2dac1a78c80bed6bdc27146a93427fe0&scene=21#wechat%5Fredirect)》提出的（3.42）式：

![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudR8iatjSz64TtZpJAcPHSQ2AoREcp5dcNMXM9g0h3LvXSaI5CXEnmibSF8lvEf54u9AQr1qrwc6RJOQ/640.png)

，然后，我对这个偏微分方程为什么是这样产生了疑问，于是有了本文。

 在![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6mhM1ichicmPa4ccCc1ibysazxguCYKPdAf5OzqLoryibDGpSiaF0SmnBspw/640.png)时，最终的解析解是：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6GTW1zoEuAo750er8YYPfZf9Xtibhriarfn9vnxRL1IrGVuxESiaTNy4OA/640.png)

  
分析过程

 概率密度函数![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6TJSUp0zibDDhV3cbdxcxgdzv5iaOyuQiafhhM0eYvFcV7wvGYVGH8vPfg/640.png)是x和t的函数，x是随机变量，于是p也是随机变量，也就是符合3.38式的定义：

![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudR8iatjSz64TtZpJAcPHSQ2AOyGgyPCfa7JtZDbicx6HhCibMFt6MDdSZvXI2NBlHicK4JiapduMicrAo0A/640.png)  

，那么，怎样求出p的解析解呢？这里要特意解释一件事：

（1）首先p是一个映射；

（2）同时p又是一个随机变量，因为它是随机变量x上的映射；

 p的最终解析解，如果是从 p是一个映射 这个角度看待的，此时p就不再是随机变量了，就是一个普通的函数；如果把p看作随机变量，那么才会符合3.38式。

  
 因为我们只有3.38式，所以只能从3.38式入手了。各项定义如下：

（1）![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6LLfHuQgd6hP9UCLQBX1qTLatZNo8L7Hicialf9clMM3gQIzXMHIzvp2Q/640.png)的定义：![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6L2fvtrntJ12NmptiagJhcBB2w63WAE1UeSUYsicZCOROfnFzNpw9YWdA/640.png)单位时间F改变量的条件期望

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6LLfHuQgd6hP9UCLQBX1qTLatZNo8L7Hicialf9clMM3gQIzXMHIzvp2Q/640.png)的泰勒项：

![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudR8iatjSz64TtZpJAcPHSQ2AYIe2I3ibBHxvV8gnIsjSXU2YsHNHHWiaklgHrIljvy88x7XaV8KEc3nw/640.png)

  
（2）![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6fO1347LIFPZ6PTMyGsRW1D7iaPON4Rj5Ypr6CRs4urcnQ8qd7zwpxOA/640.png)的定义：F的对X变量的一阶偏导数，在本例中，也就是概率密度函数p对x的一阶偏导数

  
（3）![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6NgianTYMibx1jr9ibVaFrBG2Tj73x7ib3aGMNHIyyYcbsSYamt7n6sFglA/640.png)的定义：单位时间的条件方差

![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudR8iatjSz64TtZpJAcPHSQ2AncKiaNbgTvNZmv4E9mbicTVukX4FzLibAQYUQ95JAsHFxYDnZGhyqCDtw/640.png)

  
（4）![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6y6uFZiasyhic65MJWOdWQJQAPWr3WARjV0F7ANZI5AYKtSSIwEh4agdg/640.png)是随机变量

![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudR8iatjSz64TtZpJAcPHSQ2A7hUykicCDHQUxZhzONx94jFGb6m3QfUHxXN3Awcx6VzyDXZxNXSTeiag/640.png)

  
 在原文推导中，认为![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ64fz72Msj5vrV75ibdaJhy9VloiaR0Xn3DicRUYEkLiaxIEVgQ9rlVica9tw/640.png)，即 概率密度函数 单位时间改变量的条件期望 是 0，于是就得到了3.42式，这一步我非常不理解，为什么必须等于0？ 这句话的直观表述如下：首先起点处于一个初始位置0，然后移动图1中的起点，每移动到一个位置，就会得到一个新的概率密度函数，但是这个移动是随机的，所以得到的概率密度函数也是随机的，这些个概率密度函数的期望和初始位置0的概率密度应该是一样的（连续时间金融的假设6：未来状态仅依赖初始状态），所以得到了![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ64fz72Msj5vrV75ibdaJhy9VloiaR0Xn3DicRUYEkLiaxIEVgQ9rlVica9tw/640.png)。

 根据![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ64fz72Msj5vrV75ibdaJhy9VloiaR0Xn3DicRUYEkLiaxIEVgQ9rlVica9tw/640.png)和![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6LLfHuQgd6hP9UCLQBX1qTLatZNo8L7Hicialf9clMM3gQIzXMHIzvp2Q/640.png)的泰勒项，最终得到了3.42式：

![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudR8iatjSz64TtZpJAcPHSQ2AoREcp5dcNMXM9g0h3LvXSaI5CXEnmibSF8lvEf54u9AQr1qrwc6RJOQ/640.png)

  
 从3.42式子中，完全看不出p是一个随机变量，这和p是一个随机变量有矛盾吗？

 例如，y=2x，这是一个非常简单的函数，假如x是随机变量，那么y也会变成随机变量，但是随机变量不会改变y是x的一个映射。如果把x表示成随机变量![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6PKXUQGWkQE0BylN6Gyuqcu51SIObDsymUm3C1HB4ibCTrTsYY2V2FGg/640.png)的函数，那么y也可以表示成x和![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6PKXUQGWkQE0BylN6Gyuqcu51SIObDsymUm3C1HB4ibCTrTsYY2V2FGg/640.png)的函数，这就会得到3.38式。

  
推导总结

（1）首先固定起点，随机到达终点，获得一个概率密度函数![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6atClXZWuIoiaUicG6UrAGia0VXP2ctMRTgzf13tOF3Skn2SwRYvQGJcQQ/640.png)

（2）然后固定终点，移动起点，再次获得一个概率密度函数![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6TJSUp0zibDDhV3cbdxcxgdzv5iaOyuQiafhhM0eYvFcV7wvGYVGH8vPfg/640.png)

（3）起点不一样，概率密度函数![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6TJSUp0zibDDhV3cbdxcxgdzv5iaOyuQiafhhM0eYvFcV7wvGYVGH8vPfg/640.png)也不一样

（4）把p看成x和t的函数，套在F(t)中，应用3.38式的一些推导结论

（5）应用假设6：未来状态仅依赖初始状态，获得![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ64fz72Msj5vrV75ibdaJhy9VloiaR0Xn3DicRUYEkLiaxIEVgQ9rlVica9tw/640.png)

（6）根据![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ64fz72Msj5vrV75ibdaJhy9VloiaR0Xn3DicRUYEkLiaxIEVgQ9rlVica9tw/640.png)，获得3.42式

![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudR8iatjSz64TtZpJAcPHSQ2AoREcp5dcNMXM9g0h3LvXSaI5CXEnmibSF8lvEf54u9AQr1qrwc6RJOQ/640.png)

（7）在![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6mhM1ichicmPa4ccCc1ibysazxguCYKPdAf5OzqLoryibDGpSiaF0SmnBspw/640.png)时，得到最终的解析解

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudThb3FXKTdJJIAY35ibibIqJ6GTW1zoEuAo750er8YYPfZf9Xtibhriarfn9vnxRL1IrGVuxESiaTNy4OA/640.png)

  
 到此为止，回答了文章的疑问，但这仅仅是拉开序幕，更大的话题才刚刚开始：如何把数学照到现实！

 未完，待续。。。

  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudR45nwib10GpnaWeOc5qict02HL6A2PFKFry1g5cRDtX8zMyjYN8PD0CpKtib905cibtasGJjW1EicOlVA/0.png) 

 做自由的人 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PXGicNeEFudR45nwib10GpnaWeOc5qict02HL6A2PFKFry1g5cRDtX8zMyjYN8PD0CpKtib905cibtasGJjW1EicOlVA/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
