package leetcode

import (
	"reflect"
	"testing"
)

// 1799.N次操作后的最大分数和
// https://leetcode-cn.com/problems/maximize-score-after-n-operations/
class Solution:
    def maxScore(self, nums: List[int]) -> int:
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
