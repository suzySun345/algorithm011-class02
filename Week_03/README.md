#### 学习笔记

------

**学习内容**

1. 泛型递归

2. 树结构的递归实例

3. 分治

4. 回溯

   

**学习扩展**

- 递归(Recursion)

  递归模板

  ```
  public void recur(int level,int param){
      //terminator
      if(level>MAX_LEVEL){
          //process result
          return;
      }
      //process curren level logic
      process(level,param);
      //dill down
      recur(level:level+1,newParam);
      //restore current status
  
  }
  ```

  递归思维：

  - 只考虑当层，不要下探
  - 找到问题的可重复的部分
  - 学习数学归纳思维

- 树结构遍历、求深度

  一般两种方法，一种是递归，一种是迭代。迭代需要依靠栈表辅助

  

- 分治

  将一个大问题，拆解成一些相同的子问题，递归地解决这些问题，最后将各子问题的解合并得到原问题的解。

  ```
  def divide_Conquer(problem, param1, param2, ...) {
  	//recursion terminator
  	//深入到叶子结点，也就是无问题可解决
      if problem is None:
          print Result
          return;    
      
      // prepare data
      data = prepare_Data(problem);
      subProblems = split_Problem(problem, data);
      // conquer subProblems
      subResult1 = self.divide_Conquer(subProblems[0], p1, ...);
      subResult2 = self.divide_Conquer(subProblems[1], p1, ...);
      subResult3 = self.divide_Conquer(subProblems[2], p1, ...);
      // process and generate the final result
      result = process_Result(subResult1, subResult2, subResult3, ...);
  }
  ```

- 回溯

  采用试错的思想，它尝试分步地去解决一个问题。在分步解决问题的过程中，当它通过尝试发现现有的分步答案不能得到有效的正确解答的时候，它将取消上一步甚至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。

  核心思路就是穷举所有分步解决问题的可能，然后进行排错处理。以括号生成为例，先列举出左右括号的组合，然后通过条件判断筛除不正确的组合

  

**学习思考**

