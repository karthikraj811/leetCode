class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <=1:
            return s
        res = ""
        while len(s)>1:
            s_rev = s[::-1]
            while s[0] in s_rev:
                index = s_rev.index(s[0])

                reqStr = s[:len(s)-index]

                if (reqStr[:len(reqStr)//2] == reqStr[len(reqStr)//2:][::-1] or reqStr[:len(reqStr)//2+1] == reqStr[len(reqStr)//2:][::-1]) and len(reqStr)>len(res):
                    res = reqStr


                s_rev = s_rev[:index] +"_"+ s_rev[index+1:]

            s = s[1:]
        return res
        

        


sol = Solution()

print(sol.longestPalindrome("jcwwnkwiajicysmdueefqjnrokunucidhgkswbgjkkrujkxkxeanrpjvpliomxztalhmvcldnqmkslkprhgtwlnsnygbzdvtdbsdzsdjggzgmhogknpfhtgjmclrkgfqdbiagwrqqcnagosnqrnpapxfrtrhzlyhszdtgkqggmewqmwugrbufiwfvtjhczqgcwpcyjioeacggiwyinpkyxrpxhglrtojgjmmswxnvirfsrbhmpqgjyyagjqfwkqkjkumywvgfutmiwihwnnhbfxcijaoiyxbdnrckexqfhsmmxflaneccyaoqoxfbaylcvvpfafsikebzcdufvhluldguwsmrtjaljpcjestranfrvgvytozxpcvnwquhnsxlmzkehwopgxvifajmrlwqiqylgxibnypxwpkggxevyfoxywfsfpjbzfxxysgxgwxrzkwdqlkrpajlltzqfqshdokibakkhydizsgwbygqulljqmtxkwepitsukwjlrrmsjptwabtlqytprkkuxtqdmptctkfabxsohrfrqvrbjfbppfkpthosveoppiywkkuoasefviegormlqkqlbhnhblkmglxcbszblfipsyumcrjrkrnzplkveznbtdbtlcptgswhiqsjugqrvujkzuwvoxbjremyxqqzxkgerhgtidsefyemtmstsznvgohexdgetqbhrxaomzsamapxhjibfvtbquhowyrwyxthpwvmfyyqsyibemnfbwkddtyoijzwfxhossylygxmnznpegtgvlrsreepkrcdgbujkghrgtsxwlvxrgrqxnvgqkppbkrxjupjfjcsfzepdemaulfetn"))



