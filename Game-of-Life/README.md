# Game of Life

Long ago, I came across the concept of **Game of Life** which immediately got my attention. As I always have been a fan of philosophy and programming (in case you don’t know me), I decided to program it myself.

This game is a non-player, which means you just play it by watching it happen.

The universe of this game is an infinite 2-dimensional grid. Furthermore, at the initiation time, a fixed amount of cells come to life at random coordinates. Let’s call them the next generation.

This universe has some rules that are as follows:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction

At each iteration, these rules will be applied to every position in the grid. so some cells will die, some will live, and some might even live and reproduce.

The fascinating outcome of this game is the patterns that are created in the grid. Clone this repository and see for yourself!
</br></br>
<img width="450" alt="image" src="https://user-images.githubusercontent.com/47675870/183294849-1a9f7399-d86d-42b4-a6a6-645860ff38c1.png">
<img width="450" alt="image" src="https://user-images.githubusercontent.com/47675870/183294854-fb0e941c-f16b-4058-b60f-0d4be117923c.png">
