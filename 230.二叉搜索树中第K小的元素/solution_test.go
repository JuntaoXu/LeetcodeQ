package leetcode

import (
	"reflect"
	"testing"
)

// 230.二叉搜索树中第K小的元素
// https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
func TestSolution(t *testing.T) {
	testCases := []struct {
		desc string
		want 
	}{
		{
            want: ,
		},
	}
	for _, tC := range testCases {
		t.Run(tC.desc, func(t *testing.T) {
			get := 
			if !reflect.DeepEqual(tC.want,get){
				t.Errorf("input: %+v get: %v\n",tC,get)
			}
		})
	}
}
