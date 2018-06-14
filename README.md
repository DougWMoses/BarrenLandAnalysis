# BarrenLandAnalysis
Calculate fertile land area in square meters, sorted from smallest area to greatest and separated by a 
space, given submitted coordinates of barren land .
## Preparation
Install [Python](https://www.python.org/)  
Pull down the repo.  
Navigate to the root of the BarrenLandAnalysis folder  
Open a terminal window or command prompt to accomplish the following tasks
## Running the unit tests 
The following command will execute all of the tests.
```
py -m unittest discover -v
```
## Running the application
```
py run.py
```
At the prompt, enter barren sections. For example,
````
{"0 292 399 307"}
or
{"48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"}
