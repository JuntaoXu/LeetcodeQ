package leetcode

import (
	"reflect"
	"testing"
)

// 1901.找出顶峰元素II
// https://leetcode-cn.com/problems/find-a-peak-element-ii/
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
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
