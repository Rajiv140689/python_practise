"abcabcbb"
# Output: The longest substring without repeating characters, e.g., "abc".

class LongestSubstring():
    def longSubstring(self):
        # inp_str = "abcabcbb"
        inp_str = "pwwkew"
        freq_map = {}
        start_idx = 0
        start_idx_substring = 0
        end_idx = 0
        max_length = 0
        for idx, char in enumerate(inp_str):
            if char in freq_map and idx >= start_idx:
                start_idx = freq_map[char]+1

            freq_map[char] = idx

            if idx-start_idx+1 > max_length:
                max_length = idx-start_idx+1
                start_idx_substring = start_idx
                end_idx = idx

        print("maxlen:",max_length)
        print("longest substring:", inp_str[start_idx_substring:end_idx+1])

if __name__=="__main__":
    longestSubstring = LongestSubstring()
    longestSubstring.longSubstring()
