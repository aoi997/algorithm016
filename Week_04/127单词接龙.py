class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        front, back, visited = set(), set(), set()
        front.add(beginWord)
        back.add(endWord)
        visited.add(beginWord)
        visited.add(endWord)
        cnt = 0

        while front and back:
            cnt += 1
            next_level = set()
            for word in front:
                for i in range(len(word)):
                    for k in range(26):
                        ch = chr(ord('a') + k)
                        new_word = word[:i] + ch + word[i+1:]
                        if new_word in back:
                            return cnt + 1
                        if new_word in wordSet and new_word not in visited:
                            next_level.add(new_word)
                            visited.add(new_word)
            front = next_level
            if len(front) > len(back):
                front, back = back, front

        return 0