
# PyRoll20

A simple Roll20 dice roller. 

### Usage Example

 **This rolls two d20 and returns the output.**
```python
import pyroll20
pyroll20.roll(user_input="2d20") 
```
or with a modifier
```python
import pyroll20
pyroll20.roll(user_input="2d20") 
```
### Installing
```bash
pip3 install pyroll20
```
### Modifiers
   **'h'** # Highest Rolls - **5d20h3** returns highest 3 rolls from the five d20<br/>
    **'l'** # Lowest Rolls - **5d20l3** returns lowest 3 rolls from the five d20<br/>
    **'+'**  # Adds to sum - **5d20+3** adds 3 to the sum of the five d20<br/>
    **'-'**  # Subtracts from sum - **5d20-3** subtracts from the sum of the five d20<br/>
    **'.+'** # Add to individual roll - **5d20.+3** adds 3 to each one of the five d20<br/>
   **'.-'**  # Subtract from individual roll - **5d20.-3** subtracts 3 from each one of the five d20<br/>
    **'t'**  # Sum of all rolls - **5d20t** sum of the five d20<br/>
    **'e'**  # "Exploding dice - **5d20e** if a d20 is rolled, it rolls again and adds to it<br/>
## Notes
If sides are provided but no roll number, the roll number defaults to 1, for example -> **d20** is a valid input.



## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE v3.



