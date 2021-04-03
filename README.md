# animeTrackerCFworker

给animeTackerList加速用的cloudflare worker. 

---

# status

弃用

# readme

由于github在国内的访问速度不佳，

使用了cloudflare的worker来做[AnimeTrackerList](https://github.com/DeSireFire/animeTrackerList)的转发接口。

![image](https://user-images.githubusercontent.com/18726905/113475315-76e37700-94a7-11eb-933f-46423a9027e0.png)

随着使用人数的增加，cfworker的每日免费额度已经无力支撑每日的调用消耗。

所以，在此废弃worker转发的加速方案。

jsdelivr 如今在国内访问速度优秀，以此作为替代。

https://at.raxianch.moe/xxxx.txt 的访问方式将作为本地备选。


```text
https://at.raxianch.moe/ 4月1日起，接口将发生变更。

https://at.raxianch.moe/?type=AT-best 这样的请求方式将废止。
改为(其他列表以此类推)：
https://at.raxianch.moe/xxxx.txt

可用以下临时地址，查看和测试预览效果（临时接口截至4月1日）：
https://atest.raxianch.moe/xxxx.txt
```
