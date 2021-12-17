class Solution:
    def decodeString(self, s):
        stack, currNum, curString = [], 0, ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(currNum)
                curString = ''
                currNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
            elif c.isdigit():
                currNum = currNum * 10 + int(c)
            else:
                curString += c
        return curString


if __name__ == "__main__":
    t = Solution()
    print(t.decodeString("3[abc]2[ab]c"))
