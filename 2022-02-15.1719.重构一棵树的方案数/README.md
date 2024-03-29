# 2022-02-15.1719.重构一棵树的方案数
[https://leetcode-cn.com/problems/number-of-ways-to-reconstruct-a-tree/](https://leetcode-cn.com/problems/number-of-ways-to-reconstruct-a-tree/)
## 原题
给你一个数组  `pairs` ，其中  `pairs[i] = [x<sub>i</sub>, y<sub>i</sub>]`  ，并且满足：
-  `pairs`  中没有重复元素
-  `x<sub>i</sub> < y<sub>i</sub>` 
令  `ways`  为满足下面条件的有根树的方案数：
- 树所包含的所有节点值都在 `pairs`  中。
- 一个数对  `[x<sub>i</sub>, y<sub>i</sub>]` 出现在  `pairs`  中  **当且仅当** ** ** `x<sub>i</sub>`  是  `y<sub>i</sub>`  的祖先或者  `y<sub>i</sub>`  是  `x<sub>i</sub>` <sub> </sub>的祖先。
-  **注意：** 构造出来的树不一定是二叉树。
两棵树被视为不同的方案当存在至少一个节点在两棵树中有不同的父节点。

请你返回：
- 如果  `ways == 0`  ，返回  `0`  。
- 如果  `ways == 1`  ，返回 `1`  。
- 如果  `ways > 1`  ，返回  `2`  。
一棵 **有根树**  指的是只有一个根节点的树，所有边都是从根往外的方向。

我们称从根到一个节点路径上的任意一个节点（除去节点本身）都是该节点的 **祖先**  。根节点没有祖先。

 

 **示例 1：** 
<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/09/trees2.png" style="width: 208px; height: 221px;" />
```

输入：pairs = [[1,2],[2,3]]
输出：1
解释：如上图所示，有且只有一个符合规定的有根树。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/09/tree.png" style="width: 234px; height: 241px;" />
```

输入：pairs = [[1,2],[2,3],[1,3]]
输出：2
解释：有多个符合规定的有根树，其中三个如上图所示。

```
 **示例 3：** 

```

输入：pairs = [[1,2],[2,3],[2,4],[1,5]]
输出：0
解释：没有符合规定的有根树。
```
 

 **提示：** 
-  `1 <= pairs.length <= 10^5` 
-  `1 <= x<sub>i </sub>< y<sub>i</sub> <= 500` 
-  `pairs`  中的元素互不相同。
 
**标签**
`树` `图` `拓扑排序` 


##
```go

```
>
