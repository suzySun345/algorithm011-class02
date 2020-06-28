#### Queue源码分析

------

```
 public interface Queue<E> extends Collection<E>
```

队列继承自Collection，常用实现类LinkedList。

常规的队列操作顺序为FIFO，但是Priority Queue和类似栈队列这些特殊队列的操作顺序不同。前者的操作顺序是依据比较优先值，后者的操作顺序是LIFO。但不管是哪种，队列的常规方法如下，至于不同的操作顺序在继承队列时还需要具体定制。

**队列声明**

```
Queue<String> queue = new LinkedList<String>();
```

**常用的方法如下**

| 方法      | 功能               | 返回值                           |
| --------- | ------------------ | -------------------------------- |
| add(e)    | 在队列尾端添加元素 | True or False , 空间问题抛异常   |
| offer(e)  | 在队列尾端添加元素 | True or False，空间问题返回false |
| remove()  | 删除队首元素并返回 | 返回删除的元素，空队列抛异常     |
| poll()    | 删除队首元素并返回 | 返回删除的元素，空队列返回null   |
| element() | 返回队首元素不删除 | 返回队首元素，空队列抛异常       |
| peek()    | 返回队首元素不删除 | 返回队首元素，空队列返回null     |

**add(e)和offer(e)的区别**：

- 对于有空间限制的队列，推荐使用add(e)，这个会抛出IllegalStateException。而offer(e)则只能返回false。
- 对于定容的队列，那么就用offer(e)，这么没有add(e)麻烦的异常抛出，更简洁直接。
- 此外对于并发编程的阻塞队列，offer(e)除了继承队列的初始功能，还定义为空间不足会处于等待一定时间，等待空间条件满足，这个比粗暴的异常可能更有可操作的余地。

**源码**

```
//接口Queue：
public interface Queue<E> extends Collection<E> {
    //将指定元素插入到队列的尾部（队列满了话，会抛出异常）
    boolean add(E e);

    //将指定元素插入此队列的尾部(队列满了话，会返回false)
    boolean offer(E e);

    /返回取队列头部的元素，并删除该元素(如果队列为空，则抛出异常)
    E remove();

    //返回队列头部的元素，并删除该元素(如果队列为空，则返回null)
    E poll();

    //返回队列头部的元素,不删除该元素(如果队列为空，则抛出异常)
    E element();

    //返回队列头部的元素，不删除该元素(如果队列为空，则返回null)
    E peek();
}
```



#### Priority Queue源码分析

------

堆结构，堆结构是什么：树形结构，完全二叉树，堆中某个节点的值总是不大于或不小于其父节点的值

Queue接口的实现类

与传统的FIFO队列不同，不依赖入队顺序，有自己的优先级顺序设定，具体依据构造方法里的Comparator

PQ的Head指向最小值，如果有多个可以选择一个

优先队列是无界的，但是内部有容量管理机制，添加元素后，容量会自动增长

非同步的，当有线程对PQ进行修改时，其他线程不能访问PQ，反而使用阻塞队列



**各方法的时间复杂度**

| 方法                           | 时间复杂度 | 备注                             |
| ------------------------------ | ---------- | -------------------------------- |
| add(e)/poll()/remove()/offer() | O(logn)    | 与堆遍历相关，所以复杂度O(logn)? |
| remove(e)/contains(e)          | O(n)       |                                  |
| peek()/element()/size()        | O(1)       |                                  |

**Priority Queue初始化**

```
PriorityQueue<Integer> pq = new PriorityQueue();//默认容量11，order默认自然排序
```

构造方法可以指定容量，comparator，放入优先队列的元素集类型（collection、set、PQ）

**常用方法**

| 方法               | 功能                                                        |
| ------------------ | ----------------------------------------------------------- |
| add(e)             | 插入元素，无界性没有空间限制所以不会抛IllegalStateException |
| remove(object o)   | 删除指定元素                                                |
| clear()            | 清空元素                                                    |
| comparator()       | 返回比较器comparator，没有就返回null                        |
| offer(e)           | 插入元素                                                    |
| toArray()          | 返回一个元素序列                                            |
| peek()             | 获取Head元素                                                |
| poll()             | 删除队首元素                                                |
| contains(object o) | 判断是否包含元素                                            |
| spliterator()      | 给队列创建一个晚绑定和并发错误机制可分割迭代器              |

**源码**

PriorityQueue新增元素

```
//队列添加元素，底层调用offer:插入失败抛出异常
    public boolean add(E e) {
        return offer(e);
    }

    //队列添加元素: 插入失败返回false
    public boolean offer(E e) {
        //不支持添加为null的元素：
        if (e == null)
            throw new NullPointerException();

        //队列操作数+1：
        modCount++;
        int i = size;

        //队列长度 >= 数组长度时，扩容：
        if (i >= queue.length)
            grow(i + 1);

        //队列长度+1
        size = i + 1;

        //i==0，在数组角标为0处插入第一个元素：
        if (i == 0)
            queue[0] = e;
        else
            //插入的不是第一个元素：
            siftUp(i, e);
        return true;
    }

```

