# Word Ladder - Hard
from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        setWords = set(wordList)
        if endWord not in setWords:
            return 0
        
        def isAdjacent(a, b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
                if count > 1:
                    return False
            return True

        wordList.append(beginWord)
        graph = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if isAdjacent(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        
        visited = set([beginWord])
        queue = deque([beginWord])
        count = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                for nei in graph[word]:
                    if nei == endWord:
                        return count + 1
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            count += 1
        return 0

    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int: # Better Adjacent Search
        setWords = set(wordList)
        if endWord not in setWords:
            return 0
        
        graph = defaultdict(list)

        def findAdjacent(word):
            for i in range(len(word)):
                for order in range(ord('a'), ord('z') + 1):
                    if ord(word[i]) == order:
                        continue
                    adj = word[:i] + chr(order) + word[i+1:]
                    if adj in setWords:
                        graph[word].append(adj)

        findAdjacent(beginWord)
        for word in wordList:
            findAdjacent(word)

        visited = set([beginWord])
        queue = deque([beginWord])
        count = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                for nei in graph[word]:
                    if nei == endWord:
                        return count + 1
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            count += 1
        return 0

    def ladderLength3(self, beginWord: str, endWord: str, wordList: List[str]) -> int: # Without Constructing Graph
        setWords = set(wordList)
        if endWord not in setWords:
            return 0
        
        queue = deque([beginWord])
        count = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                if word == endWord:
                    return count
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in setWords:
                            setWords.remove(next_word)
                            queue.append(next_word)
            count += 1
        return 0