class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        L = list(S)
        L_final = []
        for i in range(len(L)):
            L_final.append(L[i])
            if i>0:
                if L_final[-2:] == ['(',')']: L_final = L_final[:-2]
        return len(L_final)
