class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        candidate_vote = {}
        for candidate in arr:
            candidate_vote[candidate] = candidate_vote.get(candidate, 0) + 1
        max_vote = -1
        winner = ""
        for candidate, votes in candidate_vote.items():
            if votes > max_vote:
                max_vote = votes
                winner = candidate
            elif votes == max_vote:
                if candidate < winner:
                    winner = candidate
        return [winner, str(max_vote)]