class Solution {
public:

    string encode(vector<string>& strs) {

        string en;
        for(string &i: strs){
            int len = i.size();
            en += to_string(len);
            en+= '#';
            en+=i;
        }

        return en;

    }

    vector<string> decode(string s) {

        vector<string> de;

        size_t i =0; //size_t is used for storing sizes
        
        while(i<s.size()){
            //read length untill "#"
            int len = 0;
            while(i<s.size()&& s[i]!='#')
            {
                len = len *10 + (s[i]-'0'); // according to place value
                i++;
            }
            i++;
            de.push_back(s.substr(i, len));
            i+=len;
            
        }

        return de;

    }
};
