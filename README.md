# OOP-Problem
This project is a scoreboard for a competition based on the points earned by participants. It provides functions to calculate scores for individual participants and create a scoreboard listing all participants sorted by their scores in descending order.

## Usage

### `calculate_score(participant)`

Calculates the total score for a participant based on the given points for chicken wings, hamburgers, and hotdogs.

- Input: `participant` - It is dictionary containing the participant's name along with the number of chicken wings, hamburgers, and hotdogs consumed.
- Output: Returns the total score calculated based on the provided points.

### `create_scoreboard(participants)`

Creates a scoreboard for all participants in the competition. It calculates scores for each participant and sorts them first by score in descending order, then alphabetically by name.

- Input: `participants` - A list of dictionaries, where each dictionary represents a participant with their name, number of chicken wings, hamburgers, and hotdogs consumed.
- Output: Returns a list of dictionaries containing each participant's name and score, sorted according to the specified criteria.

## Example

```python
participants = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11},
    {'name': "Allan Rocks", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]

scoreboard = create_scoreboard(participants)

print(scoreboard)
```

## Output

The output will be a list of dictionaries, each containing the participant's name and their corresponding score, sorted in descending order of scores and alphabetically by name. For example:

```
[
    {'name': 'Big Bob', 'score': 145},
    {'name': 'Allan Rocks', 'score': 110},
    {'name': 'Habanero Hillary', 'score': 80}
]
```

This indicates that "Big Bob" has the highest score, followed by "Allan Rocks" and "Habanero Hillary".

## Author 
Rachael Wachuka Chege
rachaelwachuka7@gmail.com