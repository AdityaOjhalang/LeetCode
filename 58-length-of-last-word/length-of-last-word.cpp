class Solution {
public:
    int lengthOfLastWord(string s) {
        int n = s.size();
        int count=0;
        for(int i=n-1;i>=0;i--){

            if(s[i] == ' ' && count==0) continue;
            else if(s[i] == ' ' & count>0) return count;
            else if(s[i] != ' ') count++;
        }
        return count;
    }
};