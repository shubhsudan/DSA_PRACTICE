# string1 = 'shu'
# string2 = 'raja'
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         new_str = []
        
#         # 1. Find the minimum length to know how many times to alternate
#         min_length = min(len(word1), len(word2))

#         # 2. Add letters in alternating order up to the min_length
#         for i in range(min_length):
#             new_str.append(word1[i])
#             new_str.append(word2[i])

#         # 3. AFTER the loop, append the remainder of the longer string.
#         # Slicing from min_length to the end will naturally grab the leftovers 
#         # from the longer string, and return an empty string for the shorter one.
#         new_str.append(word1[min_length:])
#         new_str.append(word2[min_length:])

#         return "".join(new_str)







class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = []
        
        # 1. Find the minimum length to know how many times to alternate
        min_length = min(len(word1), len(word2))

        # 2. Add letters in alternating order up to the min_length
        for i in range(min_length):
            new_str.append(word1[i])
            new_str.append(word2[i])

        # 3. AFTER the loop, append the remainder of the longer string.
        # Slicing from min_length to the end will naturally grab the leftovers 
        # from the longer string, and return an empty string for the shorter one.
        new_str.append(word1[min_length:])
        new_str.append(word2[min_length:])

        return "".join(new_str)