class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Transform string in array
        # iterate through chars from index to end
            # push into aux array while char not in aux array
            # if repetition detected or end of substring reached
                # push aux_array to result_arrays
                # clear aux_array
                # increment starting index
            # take len of all arrays inside result_arrays
            # return the max(len)

        control_index = 0
        highest_len = 0
        aux_array = []
        
        while control_index < len(s):
            substring = s[control_index:]
            for idx, char in enumerate(substring):
                if char not in aux_array:
                    aux_array.append(char)
                else:
                    highest_len=max(len(aux_array), highest_len)
                    aux_array = []
                if idx == len(substring) -1:
                    highest_len=max(len(aux_array), highest_len)
                    aux_array = []
            control_index += 1

        return highest_len