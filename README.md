# SortingAlgorithmVisualiser
This project is designed to display four major (popular) sorting algorithms using multi-threading to show the methodology and time complexity of each algorithm. Each algorithm will be timed and displayed on the console in three different cases Random array, Sorted array and Reverse sorted array (Average, Best and Worst cases). The GUI is mainly used to display the method of the algorithm swaps, as some algorithms (eg. quicksort) compare more values relative to swapping values in comparison to others (eg. bubblesort). The GUI is a decent indicator to the relative timing of each algorithm as the threads switch after each value swap.

## Screenshots
<p align="center">
  <img src="https://github.com/JamesWingar/sortingAlgorithmsVisualiser/blob/master/src/gui-output.png" width="400">
  <img src="https://github.com/JamesWingar/sortingAlgorithmsVisualiser/blob/master/src/gui-output2.png" width="400">
  <img src="https://github.com/JamesWingar/sortingAlgorithmsVisualiser/blob/master/src/console-output.png">
</p>

## Summary
* This project displays four algorithms: bubble sort, quick sort, heap sort and merge sort.
* The GUI tackles a random array that all four algorithms complete.
* Comparative timing data for all algorithms solving is displayed in the console.
* The GUI is useful to see the methodology of the algorithm and relative time complexity between each algorithm.

## Install
Sorting Algorithm Visualiser supports being run on Python 3.8+ with the pygame library as the only python module for the GUI.    
- [git](https://git-scm.com/downloads)
- [python3](https://www.python.org/download/releases/3.0/)
- [pip](https://pypi.org/project/pip/)
- [pygame](https://www.pygame.org/)

To install follow the instructions below:
1. Open a command line tool (eg. Linux -> Terminal, Windows -> Powershell)
2. Install [git](https://git-scm.com/downloads)
3. Change directory to where you want the folder using the `cd` command
4. 
```python
git clone https://github.com/JamesWingar/sortingAlgorithmsVisualiser
```
5. Change directory to inside the directory `sortingAlgorithmsVisualiser`
6. 
```python
pip install -r requirements.txt
```
7. You are ready to go!

(*Note: you can use a virtual environment at step 6 to install the packages*)

## Usage
* Run the python software by the command:
```
python main.py
```
* The algorithms will automatically begin solving
* Press R to reset and generate a new random array to solve
* When completed the algorithm graphs turns green

## ToDo
* ~~Add iterative sorting algorithms~~
* ~~Design visual algorithms GUI~~
* ~~Add GUI class~~
* ~~Run step through algorithms~~
* ~~Clean up GUI code~~
* ~~Add utility functions to create best and worse arrays (ordered and reverse order)~~
* ~~Add running of worst, average and best case scenarios~~
* ~~Display above timings~~
* ~~Tidy project~~
