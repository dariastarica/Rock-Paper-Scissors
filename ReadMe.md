# Rock Paper Scissors

### Disclaimer: I do not own any icon used for this project.

* Paper, Rock and Scissors Icons:
    <div>made by <a href="https://www.flaticon.com/authors/darius-dan" title="Darius Dan">Darius Dan</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
  
### To Run the program:
* Run MainWindow.py

## Logic used for Computer Choice:
* Discrete Markov Chains: 
  * I stored in a Matrix the number of events passing from a choice to another
  * The computer decides his move based on the previous moves of the player. It computes what is the most probable passing from one choice to another and chooses the item that would beat that choice
