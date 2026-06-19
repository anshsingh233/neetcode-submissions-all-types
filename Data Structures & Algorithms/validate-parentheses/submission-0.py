class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        closetoopen={ ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in closetoopen:
                if st and st[-1]==closetoopen[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        return True if not st else False