def calculate_score(participant):
    # Calculating the total score for a participant based on the given points
    score = participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2
    return score

def create_scoreboard(participants):
    # Calculating scores for all participants
    scores = [{'name': participant['name'], 'score': calculate_score(participant)} for participant in participants]
    
    # Sorting scores first by score in descending order, then alphabetically by name
    scores.sort(key=lambda x: (-x['score'], x['name']))
    
    return scores

#test cases
participants = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11},
    {'name': "Allan Rocks", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]

scoreboard = create_scoreboard(participants)
print(scoreboard)

