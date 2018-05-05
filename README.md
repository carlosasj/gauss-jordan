# Gauss-Jordan Algorithm implementation

9167910 - Carlos Alberto Schneider Junior
9364865 - Julia Diniz Ferreira
9293651 - Vinícius do Nascimento Fontenele

## Requirements

python 3.6 or greater

## Disclaimer

Only the files inside the `project` folder represents my submission to the assignemnt.
Note that the only `import` statements are for importing
(1) other objects I wrote,
(2) typing definitions to make my autocomplete working better,
(3) a library to work with Regular Expressions and
(4) the `gcd` function from `math` lib to calculate the Geatest Commom Divisor (i've wrote my own function to prove that this import was made only for performance reasons).

## How to use the functions

### 1. Use in Command Line

```bash
python main.py [options]
```

**Options:**

`-h`, `--help` : Shows help message

`--file FILE`, `-f FILE` : File to Read (eg.: `-f case1.in`)

`--result-format {fraction,float}`, `-rf {fraction,float}` : Which format the output should be.
It can accept `fraction` or `float` as argument (eg.: `--result-format fraction`)

### Use as import in another file

On the top of the file, write:

```python
from project.main import do_gauss_jordan
from project.line import Line

...

matrix = [  # Replace to your own terms
    Line([2, -1,  3,  5],  -7),
    Line([6, -3, 12, 11],   4),
    Line([4, -1, 10,  8],   4),
    Line([0, -2, -8, 10], -60),
]

result = do_gauss_jordan(matrix)
```

`result` will have the same format as `matrix` (a list of `Line`), but the "normal"
matrix will be a identity matrix, and the `augmented` argument of each `Line` will
be the value corresponding the term in this line that have 1 as value.

## What about this Jupyter?

This is used just to demonstrate the algorithm.

You can run a online version of this notebook here: [https://mybinder.org/v2/gh/carlosasj/gauss-jordan/master?filepath=Gauss-Jordan.ipynb](https://mybinder.org/v2/gh/carlosasj/gauss-jordan/master?filepath=Gauss-Jordan.ipynb)

Or, you can learn how to run a Jupyter Notebook from their docs: [http://jupyter.org/install](http://jupyter.org/install)
