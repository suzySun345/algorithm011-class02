#### 学习笔记

**Hashmap的介绍**

------

正常情况下，大多操作的时间复杂度为(O(logn))，contains操作是O(n)，最坏情况下，多个元素映射到同一个hash code，就会造成大多数操作的时间复杂度为O(n)。

Hash Map不同于Hash table的是它接收null key和null value，并且它不同步的，所以在多线程编程时，最好声明synchronizeMap类对象。

通过hash的方法，通过put和get存储和获取对象。存储对象时，我们将K/V传给put方法时，它调用hashCode计算hash从而得到bucket位置，进一步存储，HashMap会根据当前bucket的占用情况自动调整容量(超过Load Facotr则resize为原来的2倍)。获取对象时，我们将K传给get，它调用hashCode计算hash从而得到bucket位置，并进一步调用equals()方法确定键值对。如果发生碰撞的时候，Hashmap通过链表将产生碰撞冲突的元素组织起来，在Java 8中，如果一个bucket中碰撞冲突的元素超过某个限制(默认是8)，则使用红黑树来替换链表，从而提高速度。



**HashMap的继承和类属性**

------

两个静态全局类属性，一个是容量，一个是负载因子

```
public class HashMap<K, V> extends AbstractMap<K, V>
    implements Map<K, V>, Cloneable, Serializable
{	
	static final int DEFAULT_CAPACITY = 11; //容量
	static final float DEFAULT_LOAD_FACTOR = 0.75f; //负载因子
}
```



**HashMap的常用方法**

------

| 方法           | 功能                | 备注           |
| -------------- | ------------------- | -------------- |
| size()         | 获取HashMap的大小   | 返回键值对个数 |
| isEmpty()      | 判断HashMap是否为空 | 返回布尔值     |
| hash(object k) | 计算k值的哈希值     | 返回哈希值     |
| HashEntry      |                     |                |
|                |                     |                |
|                |                     |                |



**get方法和put方法**

------

get方法的代码实现：

1. 计算出key的hash值，通过hash值确定bucket的下标值
2. 找到下标所对应的结点，查找是否有要获取的key值
3. 如果有，就返回key值所对应的value值，如果没有，就指向链表下一个结点，最终仍没结果就返回null

```
public V get(Object key){
	int idx = hash(key);
    HashEntry<K, V> e = buckets[idx];
    while (e != null){
    	if (equals(key, e.key))
        return e.value;
        e = e.next;
        }
    return null;
   }
```

put方法的代码实现

1. 计算出key的hash值，通过hash值确定bucket的下标值
2. 找到下标值所对应的结点，看看其所对应的Key值是否等于我们要插入的key值
3. 挨个遍历entry链表中的结点，查找是否有与要插入的key值相等的key值
4. 如果存在，再比较下其对应的value值是否等于要插入的value值
5. 如果是则返回value值，否则就查询下一个结点
6. 如果空间大小超过了threshold，则再次哈希，重新对key进行哈希，再确定bucket的下标
7. 添加一个entry结点，传入新结点的key值、value值和hash值
8. 返回null

```
public V put(K key, V value)
    {
      int idx = hash(key);
      HashEntry<K, V> e = buckets[idx];
  
      while (e != null)
        {
          if (equals(key, e.key))
            {
              e.access(); // Must call this for bookkeeping in LinkedHashMap.
          	  V r = e.value;
              e.value = value;
              return r;
            }
          else
            e = e.next;
        }
  
      // At this point, we know we need to add a new entry.
      modCount++;
      if (++size > threshold)
        {
          rehash();
          // Need a new hash value to suit the bigger table.
          idx = hash(key);
        }
  
      // LinkedHashMap cannot override put(), hence this call.
      addEntry(key, value, idx, true);
      return null;
    }
```

总结下，这两个方法的原理都是通过对key的进行hash计算，得出buckets的下标位置。如果有哈希碰撞，就去链表查找对应的节点