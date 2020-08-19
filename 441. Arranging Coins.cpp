%*  https://leetcode.com/problems/arranging-coins/  *%


class Solution {
public:
    int arrangeCoins(int n) {
        int cycle = 0;
        while (n > cycle)
        {
            
            cycle += 1;
            n -= cycle;
        }
        return cycle;
    }
};
