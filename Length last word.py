# Given two sorted arrays nums1 and nums2 of size m and n respectively, return 
# the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n))

def lengthOfLastWord(s: str) -> int:
    pre = s.strip()
    res = pre.split(' ')
    return len(res[-1])

if __name__ == '__main__':
    s1 = "Hello World"
    s2 = "   fly me   to   the moon  "
    s3 = "luffy is still joyboy"

    print(lengthOfLastWord(s1))
    print(lengthOfLastWord(s2))
    print(lengthOfLastWord(s3))