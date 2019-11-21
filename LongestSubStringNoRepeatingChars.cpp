class LongestSubStringNoRepeatingChars {
public:
    int lengthOfLongestSubstring(string s) {
        string nrcs = "";
        int* visited = new int[256];
        int max_nrcs = 0;
        int curr_nrcs = 0;
        string max_nrcs_str ="";
        
        for (int i=0;i<256;i++){
            visited[i] = -1;
        }
        int size_str = s.size();
        for(int i=0;i < size_str; i++){
            char curr = s[i];

            if(nrcs.find(curr) != string::npos){
                if(curr_nrcs > max_nrcs){
                    max_nrcs = curr_nrcs;
                    max_nrcs_str = nrcs;
                }
                nrcs = s.substr(visited[curr]+1,i-visited[curr]);
                curr_nrcs = nrcs.size();
            }
            else{
                nrcs.append(1, curr);
                curr_nrcs++;
                if(curr_nrcs > max_nrcs){
                    max_nrcs = curr_nrcs;
                    max_nrcs_str = nrcs;
                }
            }
                            visited[curr] = i;
        }
        return max_nrcs;
    }
};