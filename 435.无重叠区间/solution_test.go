package leetcode

import (
	"reflect"
	"testing"
)

// 435.无重叠区间
// https://leetcode-cn.com/problems/non-overlapping-intervals/
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
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
