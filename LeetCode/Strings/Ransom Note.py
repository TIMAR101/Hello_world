class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransomeList = list(ransomNote)

        magazineList = list(magazine)

        for item in magazineList:

            try:
                ransomeList.remove(item)

            except:
                continue

            if len(ransomeList) == 0:
                return True
        return False

class Solution1:
    def canConstruct(self, ransomNote, magazine):
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True

class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # Create Counter objects for the ransomNote and magazine strings
        note, mag = Counter(ransomNote), Counter(magazine)

        # Check if the intersection of note and mag Counter objects is equal to note Counter object
        # If it is, it means that all the letters in ransomNote can be formed using the letters in magazine
        if note & mag == note: return True
        return False

class Solution3:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i,"",1)
            else: return False

        return True

class Solution4:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter      = Counter(ransomNote)
        magazine_counter    = Counter(magazine)
        return ransom_counter == ransom_counter & magazine_counter

S1 = Solution()

print(S1.canConstruct(ransomNote = "aa", magazine = "aab"))

S4 = Solution4()

print(S4.canConstruct(ransomNote = "aa", magazine = "aab"))


