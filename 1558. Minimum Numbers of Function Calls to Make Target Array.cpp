%*  https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/  *%

class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        int cnt = 0, arr[n];
        for(int i = 0; i < n; i++){
            int d = 0;
            while(nums[i] !=0){
                if (nums[i] % 2 == 1){
                    nums[i] -= 1;
                    cnt++;
                }
                else{
                    nums[i] /= 2;
                    d++;
                }
            }
            arr[i] = d;
        }
        return cnt + *max_element(arr, arr + n);
        
    }
};
