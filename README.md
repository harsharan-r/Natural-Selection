# Natural Selection

***Note: This code is quite old, created before I learned about version control, which is why the different iterations are stored in separate folders. Due to this, the code is somewhat messy. However, it still demonstrates an interesting concept, even if it’s not the most polished.***

This is my first natural selection program, where a dot is "genetically trained" to reach a goal. Initially, the dot's movements are random. After each generation, the best-performing dots (those closest to the goal) have their movements (genes) copied and slightly mutated. Over generations, this simulates natural selection and shows the evolution over generations. Since natural selection doesn't occur this simply, it is a very fast progressing algorithm and is prone to genetic drift, where you will see the dots conform to a sub-optimal path. The program can also handle basic obstacles, which can be enabled or disabled in the code. I rewrote Code Bullet's Java tutorial in Python using numpy, pandas, and pygame. The project is in various folders, with the working version in NatSelect Game 3 (Working).

Attribution to video: [Code Bullet's AI Tutorial](https://www.youtube.com/watch?v=BOZfhUcNiqk&pp=ygUUY29kZSBidWxsZXQgdHV0b3JpYWw%3D)

## Demo

![Natural Selection](https://github.com/user-attachments/assets/4345d34c-08a2-454b-b70a-b79356d2bf9e)
![Natural Selection with Obsticle](https://github.com/user-attachments/assets/aa179d98-89c3-468c-aaae-dfe62f337618)

## Installation

1. Clone this repository to your local machine:
    ```
    git clone https://github.com/harsharan-r/Natural-Selection.git
    ```

2. Install dependencies if any (e.g., NumPy, Matplotlib):
    ```
    pip install -r requirements.txt
    ```

## Running the Game
Navigate to the `NatSelect Game 3 (Working)` folder:
```
cd Natural-Selection/First\ Natural\ Selection/NatSelect\ Game\ 3\ \(Working\)
```

To run the simulation, execute the following in your terminal:
```
python Main.py
```

### Turning Obstacles On/Off
Change `Obsticles` from `True` to `False`  in `Natural-Selection/First Natural Selection/NatSelect Game 3/(Working)/Main.py`
Change `self.Obsticles` from `True` to `False`  in `Natural-Selection/First Natural Selection/NatSelect Game 3/(Working)/Dot.py`

