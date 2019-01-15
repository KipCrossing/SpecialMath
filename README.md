# Special Math

I created this labary to contain spcific methods that help me solve novel, yet common, problems.

These are written light-weight to run on micropython

## Usage

Import the special math object that contains the methods

```python
from specialmath import SpecialMath

sm = SpecialMath()
```

## Methods

### Mean

Mean takes a list of numbers and returns the average

```python
sm.mean([1,2,3])
```
returns 2.0

### SSE

SSE takes 2 lists of equal length and returns the sum of square error

```python
sm.SSE([1,2,3],[2,3,4])
```

returns 3

### Gen Sine

Returns a list that is a full rotation of a sine wave

* Argument 1: length of output list
* Argument 2: amplitude of sine wave
* Argument 3: phase shift of sine wave

```python
sm.gen_sin(10,8,2.5)
```

```
returns [-20.0, -16.18033988749895, -6.180339887498947, 6.180339887498947, 16.18033988749895, 20.0, 16.18033988749895, 6.180339887498959, -6.18
0339887498954, -16.180339887498945]
```

### Fit sine

Returns a tuple size 2 that contains (1) the amplitude and (2) the phase shift.
Takes 2 arguments :

* Argument 1: Imput list containing the data to shape the sine wave to
* Argument 2: Accuract factor, detirmines the number of itterations taken to estimate the wave properties. The higher the number, the more accurate and the longer computational time

```python
sm.fit_sin([-4,0,4,0],8)
```

returns (3.9999744, 0.99993896484375)


## To Do

Add a methof to calculate the Standard Deviation

## Acknowledgements
Written By Kipling Crossing
