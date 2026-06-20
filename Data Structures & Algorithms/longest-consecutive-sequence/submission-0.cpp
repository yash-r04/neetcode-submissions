class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> st;
        for(int i : nums){
            st.insert(i); //inserting all elements in set
        }
        int max_len=0, len=0;
        for(auto i : st){
            if(st.find(i-1)==st.end()){//starting of the series
                len=1;
                int current_element = i;
                while(st.find(current_element+1)!=st.end()){
                    len++;
                    current_element++;
                }
                max_len=max(max_len,len);
            }

        }

        return max_len;
    }
};
