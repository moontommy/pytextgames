## List of games:

| Game                  | Variables                                  | Return type  |
| --------------------- |:------------------------------------------:| ------------:|
| Guess the number      | playername:string, lowest:int, highest:int | void         |
| Hangman               | playername:string                          | void         |
| Blackjack             | playername:string                          | void         |
| Rock, Paper, Scissors | playername:string                          | void         |

## Example for playing Hangman:

```python
# Declare playername
playername = "John Doe"

# Import Hangman Class
from pytextgames import Hangman

# Declare game for our friend John
g = Hangman(playername)

# Let's go play
g.play()
```
