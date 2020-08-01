/* https://leetcode.com/problems/detect-capital/  */

class Solution {
public:
    bool detectCapitalUse(string s) {
        if (s.size() == 1)
            return true;
        
        char first = s[0];
        bool ok = false;
        if (isupper(first))
            ok = true;
        
        if (ok)
        {
            if (isupper(s[1]))
            {
                int i = 2;
                while (i < s.size())
                {
                    if (islower(s[i]))
                        return false;
                    i++;
                }
                return true;
            }
            else
            {
                int i = 2;
                while (i < s.size())
                {
                    if (isupper(s[i]))
                        return false;
                    i++;
                }
                return true;
            }
        }
        else
        {
            int i = 1;
            while (i < s.size())
            {
                if (isupper(s[i]))
                    return false;
                i++;
            }
        }   return true;
    }
};
