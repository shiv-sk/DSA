class Solution:

    def winner(self, arr):
        candidate_votes = {}
        for candidate in arr:
            candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1
        max_votes = 0
        max_votes_candidate = ""
        for candidate in arr:
            if candidate_votes[candidate] > max_votes:
                max_votes = candidate_votes[candidate]
                max_votes_candidate = candidate
            elif candidate_votes[candidate] == max_votes:
                if candidate < max_votes_candidate:
                    max_votes_candidate = candidate
        return [max_votes_candidate, max_votes]