#### 学习笔记

------

##### 深度优先搜索（DFS）

从根结点开始，纵向地遍历树结构，既沿着某条子路径一直下探到叶子结点，然后回溯，再沿着另一条子路径进行再次下探，直到所有的结点都被访问过为止。通常使用递归方法来实现DFS。

```
def dfs(node):
  if node in visited:
    return
  visited.add(node)
  dfs(node.left)
  dfs(node.right)
```

##### 广度优先搜索（BFS）

从根结点开始，横向地遍历树结构，访问其所有子结点，然后继续遍历孙子结点，不断向下层遍历，直到遍历结束。通常使用队列来实现

```
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```

##### 贪心算法

贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择， 从而希望导致结果是全局最好或最优的算法。

贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。 动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

适用场景：简单地说，问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。 这种子问题最优解称为最优子结构。

##### 二分查找

二分查找的前提：

- 目标函数单调性（单调递增或者递减）；

- 存在上下界（bounded）；

- 能够通过索引访问（index accessible)。

  就是每次比较中间结点来缩小一半的搜索范围，直到找到目标值

```
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1
```

练习题：使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方。

每次查找中间元素，比较start 、end元素和其的比较结果

测试用例：

[4, 5, 6, 7, 0, 1, 2]

[0, 1, 2, 7, 6, 5, 4]

step1: mid = (0+len(list)-1)/2 = 3， compare(list[0],list[mid])和compare(list[mid],list[6])，确定无序范围

step2: 然后以mid为边界，继续重复step1