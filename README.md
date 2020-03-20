# AI_HW_2
Mesterséges Intelligencia házi feladat #2 - A* algoritmus _n_ tologatós játékra

_A* algorithm - Solving n-puzzle with it_

The __readme__ is also available in English [here](#task).

## Feladat
Jussunk el a kezdeti állapotból a végső állapotba. Végállapot a következőt jelenti, például _n=3_ esetén, ahol az üres helyet 0 jelöli:
```
1 2 3
4 5 6
7 8 0
```
## Program
A program implementálja a kért kapcsolókat:
* ```–input <FILE>```: a kezdeti állapotot tartalmazó állomány neve. Ha a kapcsoló hiányzik, a standard bemenetről olvassa be a kezdeti állapotot.
* ```–solseq```: a standard kimenetre írja a teljes megoldási szekvenciát
* ```–pcost```: a standard kimenetre írja a megoldás költségét
* ```–nvisited```: a standard kimenetre írja a meglátogatott csomópontok számát
* ```–h <H>```: a heurisztika típusa. Ha H=1, használja a „rossz helyen levő csempék száma” heurisztikát. Ha Ha H=2, használja a Manhattan heurisztikát.
* ```–rand <N> <M>``` egy véletlenszerű, N méretű állapotot ír ki a standard kimenetre. M a véletlenszerű tologatások számát jelenti.

A parancsokat egymás után is lehet fűzni, kivéve a ```-rand <N> <M>```-et, ez esetben nem lesz figyelembe véve a többi parancs.
Pythonban lett megírva, a 3.6-os verzióban.

## Eredmények, n=3
**5 lépés esetén:**

H = 1: meglátogatott csomópontok száma 5, költség 5

H = 2: meglátogatott csomópontok száma 5, költség 5

**12 lépés esetén:**

H = 1: meglátogatott csomópontok száma 518, költség 12

H = 2: meglátogatott csomópontok száma 316, költség 12

**16 lépés esetén:**

H = 1: meglátogatott csomópontok száma 3164, költség 16

H = 2: meglátogatott csomópontok száma 181, költség 16

A tesztesetek a readme végén találhatóak.

## Eredmények, n=4
**10 lépés esetén:**

H = 1: meglátogatott csomópontok száma 21, költség 10

H = 2: meglátogatott csomópontok száma 165, költség 10

___
___

## Task 
Let's get from the initial state to the final state. Let's use the following convention: if _n = 3_, the end state should look like this (where 0 denotes the empty space):
```
1 2 3
4 5 6
7 8 0
```
## The code
The code implements the following requirements/switches:
* ```–input <FILE>```: the name of the file which contains the initial state. If the switch is missing, read the initial state from the standard input. 
* ```–solseq```: writes the complete solution sequence to the standard output
* ```–pcost```: writes the cost of the solution to the standard output
* ```–nvisited```: writes the number of visited nodes to the standard output
* ```–h <H>```: the type of the heuristic technique. If H = 1, use the "number of tiles in the wrong place" heuristics. If H = 2, use the Manhattan heuristics.
* ```–rand <N> <M>``` prints a random state of size N to the standard output. M is the number of random shifts.

The commands can be appended sequentially, except for ```-rand <N> <M>```, in which case the other commands are ignored.
It is written in Python, version 3.6.

## Results, n=3
**For 5 steps:**

H = 1: number of visited nodes 5, cost is 5

H = 2: number of nodes visited 5, cost is 5

**For 12 steps:**

H = 1: number of nodes visited 518, cost is 12

H = 2: number of nodes visited 316, cost is 12

**For 16 steps:**

H = 1: number of nodes visited 3164, cost is 16

H = 2: number of nodes visited 181, cost is 16

## Results, n=4
**For 10 steps:**

H = 1: number of visited nodes 21, cost is 10

H = 2: number of nodes visited 165, cost is 10

## Tesztesetek / Test cases:

```
5 lépés/steps: 
1 2 3
5 7 6
4 0 8

12 lépés/steps:
2 3 5       
4 0 6
1 7 8

16 lépés/steps:
2 3 4
8 1 7
0 6 5

10 lépés/steps, n=4
2   5  3  4
9   1  7  8
0   6 11 12
13 10 14 15

```

