/*  https://leetcode.com/problems/plus-one/  */

class Solution {
public:
    vector<int> plusOne(vector<int>& arr) {
        int i = arr.size() - 1;
        while(i > -1)
        {
            if (arr[i] == 9)
                arr[i] = 0;
            else
            {
                arr[i] += 1;
                return arr;
            }
        i--;
        }
        arr.push_back(0);
        arr[0] = 1;
        return arr;
    }
};

