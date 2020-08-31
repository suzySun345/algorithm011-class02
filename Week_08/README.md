#### 学习笔记

------

##### 位运算

- 左移
- 右移
- 与
- 或
- 取反
- 异或

异或运算

相同为0，不同为1

x ^ 0 = x

x ^ 1s = ~x

x ^ x = 0

x ^ ~x = 1s

指定位置的位运算

1. 将x最右边的n位清零。x&(~0<<n)
2. 获取x的第n位值（x>>n)&1
3. 获取x的第n位幂值 x&(1<<n)
4. 仅将第n位位置为1，x|(1<<n）
5. 仅将第n位位置为0，x &（~(1<<n)）
6. 将x的最高位至第n位清零，x&((1<<n)-1)

判断奇偶

x % 2 == 1 ->(x&1) == 1

x % 2 == 0  ->(x&1) == 0

使用最后一位与1做与运算，可以判断奇偶性，能用位运算判断奇偶性就用位运算

x>>1 = x/2，即x = x/2

例如：mid = (left +right) / 2 等于 mid = (left + right) >>1

x = x & (x-1) 清零最低位的1

x & -x 得到最低位的1

x & -x = 0

##### 布隆过滤器

由一个很长的二进制向量和一系列随机映射函数组成。用于检测元素是否存在一个集合中。

优点是空间效率和查询时间远超一般数据结构

缺点是有一定的误识别率和删除困难

对应的二进制位都为1有可能并不存在，但是不都为1肯定不存在

通常是挡在数据库之前的快速查询的缓存



[布隆过滤器的原理和实现](https://www.cnblogs.com/cpselvis/p/6265825.html)

[使用布隆过滤器解决缓存击穿、垃圾邮件识别、集合判重](https://blog.csdn.net/tianyaleixiaowu/article/details/74721877)

[布隆过滤器 Python 实现示例](https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/)

[高性能布隆过滤器 Python 实现示例](https://github.com/jhgg/pybloof)

[布隆过滤器 Java 实现示例 1](https://github.com/lovasoa/bloomfilter/blob/master/src/main/java/BloomFilter.java)

[布隆过滤器 Java 实现示例 2](https://github.com/Baqend/Orestes-Bloomfilter)

**案例**

1. 比特币网络
2. 分布式系统（Map Reduce)-Hadoop、search engin
3. Redis缓存
4. 垃圾邮件、评论等的过滤

**python的简单实现**

1. bitarray，数组，存储的都是二进制位
2. 一个元素进来对应多少个二进制位
3. 循环hash_num次，每次把seed和元素进行哈希，再模上二进制数组的size长度，得到二进制位的索引
4. 查询元素是，循环hash_num次，每次找到对应的索引下标

##### LRU cache

两个要素，大小和替换策略

Hash Table + Double LinkedList

替换策略：LRU和LFU，[替换算法总揽](https://en.wikipedia.org/wiki/Cache_replacement_policies)

查询O(1)

修改、更新O(1)

##### 排序算法

比较类排序

通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlogn)，因此也成为非线性时间比较类排序

- 交换排序
  - 冒泡排序
  - 快速排序
- 插入排序
  - 简单插入排序
  - 希尔排序
- 选择排序
  - 简单选择排序
  - 堆排序
- 归并排序
  - 二路归并排序
  - 多路归并排序

非比较类排序

不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时间下界，以线性时间运行，因此也称为线性时间非比较类排序

- 计数排序
- 桶排序
- 基数排序

![image-20200830170937731](C:\Users\sunsu\AppData\Roaming\Typora\typora-user-images\image-20200830170937731.png)

**初级排序**

- 选择排序

  每次找最小值，放入待排序数组的起始位置

- 插入排序

  从前到后构建有序序列；对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入

- 冒泡排序

  嵌套循环，每次查看相邻的元素如果逆序，则交换

  每次都是两两交换排序，知道不再发生交换为止

**高级排序**

- 快速排序

  数组取标杆pivot，将小元素放左侧，大元素放右侧，然后依次对右边和右边的子数组继续快排；以达到整个序列有序。

- 归并排序

  - 把长度为n的输入序列分成两个长度为n/2的子序列
  - 对这两个子序列分别采用归并排序
  - 将两个排序好的子序列合并成一个最终的排序序列

  [十大经典排序算法](https://www.cnblogs.com/onepixel/p/7674659.html)

  [快速排序代码示例](https://shimo.im/docs/TX9bDbSC7C0CR5XO)

  [归并排序代码示例](https://shimo.im/docs/sDXxjjiKf3gLVVAU)

  [堆排序代码示例](https://shimo.im/docs/M2xfacKvwzAykhz6)

  [9 种经典排序算法可视化动画](https://www.bilibili.com/video/av25136272)

  [6 分钟看完 15 种排序算法动画展示](https://www.bilibili.com/video/av63851336)