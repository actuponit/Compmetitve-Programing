class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        d = deque([i for i in range(len(deck))])
        deck.sort()
        arr = [0] * len(deck)
        i = 0
        while d:
            first = d.popleft()
            if d:
                second = d.popleft() 
                d.append(second)
            arr[first] = deck[i]
            i += 1
        return arr
        