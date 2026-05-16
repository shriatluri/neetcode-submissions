class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {')': '(', '}': '{', ']': '['}
        check_stack = []

        for char in s:
            if char in hash_map.keys():
                if not check_stack:
                    return False
                elif check_stack[-1] == hash_map[char]:
                    check_stack.pop()
                    continue
                else:
                    return False
            else:
                check_stack.append(char)
        
        if not check_stack:
            return True
        else:
            return False
            
