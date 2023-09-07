package main

/*
	The Goal
Once teleported inside the structure, your mission is to:
find the control room from which you will be able to deactivate the tracker beam
get back to your starting position once you've deactivated the tracker beam
 	Rules
The structure is arranged as a rectangular maze composed of cells. Within the maze Rick can go in any of the following directions: UP, DOWN, LEFT or RIGHT.

Rick is using his tricorder to scan the area around him but due to a disruptor field, he is only able to scan the cells located in a 5-cell wide square centered on him.

Unfortunately, Spock was correct, there is a trap! Once you reach the control room an alarm countdown is triggered and you have only a limited number of rounds before the alarm goes off. Once the alarm goes off, Rick is doomed...

Rick will die if any of the following happens:
Rick's jetpack runs out of fuel. You have enough fuel for 1200 movements.
Rick does not reach the starting position before the alarm goes off. The alarm countdown is triggered once the control room has been reached.
Rick touches a wall or the ground: he is ripped apart by a mechanical trap.
You will be successful if you reach the control room and get back to the starting position before the alarm goes off.

Maze format
A maze in ASCII format is provided as input. The character # represents a wall, the letter . represents a hollow space, the letter T represents your starting position, the letter C represents the control room and the character ? represents a cell that you have not scanned yet. For example:

###########
#T..#.....#
#.#.###.#.#
#.#.#C#.#.#
#.###.#.#.#
#...#...#.#
###########
The maze is surrounded by walls. It is always possible to go from any cell to any other cell in the maze.


Initialization input
Line 1: 3 integers: R C A
R,C are the numbers of rows and columns of the maze.
A, is the number of rounds between the time the alarm countdown is activated and the time the alarm goes off.

Input for one game turn
Line 1: 2 integers: KR and KC. Rick is located at row KR and column KC within the maze. The cell at row 0 and column 0 is located in the top left corner of the maze.

Next R lines: C characters  # or  . or  T or  C or  ? (i.e. one line of the ASCII maze)

Output for one game turn
A single line containing one of: UP DOWN LEFT or RIGHT
*/
import (
	"fmt"
	"math/rand"
)

type Direction int

const (
	UP Direction = iota
	DOWN
	LEFT
	RIGHT
)

func (d Direction) String() string {
	switch d {
	case UP:
		return "UP"
	case DOWN:
		return "DOWN"
	case LEFT:
		return "LEFT"
	case RIGHT:
		return "RIGHT"
	}
	return "UNKNOWN"
}

type Cell struct {
	x, y  int
	value byte
}

var hollowCells []Cell

type Maze struct {
	row, column int
	cells       []Cell
}
type Game struct {
	maze             Maze
	alarm            int
	startingPoint    Cell
	controlRoom      Cell
	triggered        bool
	currentDirection Direction
	foundControlRoom bool
}

func (g *Game) init(r, c, a int) {
	g.maze.row = r
	g.maze.column = c
	g.alarm = a
	g.maze.cells = make([]Cell, r*c)
}

// add StartingPoint and ControlRoom
func (g *Game) addCell(x, y int, c byte) {
	g.maze.cells[g.maze.row*x+y] = Cell{x, y, c}
	switch c {
	case 'T':
		g.startingPoint = Cell{x, y, c}
	case 'C':
		g.controlRoom = Cell{x, y, c}
		g.foundControlRoom = true
	}
}

// player reached the control room
func (g *Game) reachedControlRoom(kr, kc int) bool {
	if g.controlRoom.x == kr && g.controlRoom.y == kc {
		g.triggered = true
		return true
	}
	return false
}

// find direction to move
func (g *Game) findDirection(kr, kc int, d Direction) Direction {
	direction := d
	nextCell := g.nextCell(kr, kc, direction)
	if nextCell.value == '#' {
		return g.findDirection(kr, kc, Direction(rand.Intn(4)))
	} else {
		return direction
	}

}

// find next cell
func (g *Game) nextCell(kr, kc int, d Direction) Cell {
	switch d {
	case UP:
		return g.maze.cells[g.maze.row*(kr-1)+kc]
	case DOWN:
		return g.maze.cells[g.maze.row*(kr+1)+kc]
	case LEFT:
		return g.maze.cells[g.maze.row*kr+(kc-1)]
	case RIGHT:
		return g.maze.cells[g.maze.row*kr+(kc+1)]
	}
	return Cell{}
}

// D* algorithm to find the shortest path
func shortestPath(tX, tY, cX, cY int) {
	// find the shortest path from current position(cX,cY) to target position (tX,tY)
	// using D* algorithm
	for len(hollowCells) > 0 {
		point := hollowCells[0]
		expand(point)
	}
}

func expand(point Cell) {
	is
}

func isRaise(point Cell) bool {
	var cost int
	if point.getCurrentCost() > point.getMinCost() {
		// for each neighbor of point
		// cost = min(cost, neighbor.getCurrentCost()+1)
		// point.setMinCost(cost)
		for _, neighbor := range point.getNeighbors() {
			cost = min(cost, neighbor.getCurrentCost()+1)
		}
	}
}

// get all cell is '.'
func (g *Game) getHollowCells() []Cell {
	var hollowCells []Cell
	for _, cell := range g.maze.cells {
		if cell.value == '.' {
			hollowCells = append(hollowCells, cell)
		}
	}
	return hollowCells
}

// Main function
func main() {
	var game Game
	var r, c, a int
	fmt.Scan(&r, &c, &a)
	game.init(r, c, a)
	for {
		var kr, kc int
		fmt.Scan(&kr, &kc)

		for i := 0; i < r; i++ {
			var row string
			fmt.Scan(&row)
			for j := 0; j < c; j++ {
				game.addCell(i, j, row[j])
			}
		}

		if game.triggered {
			// Go back to starting point by using BFS all visited cells
			// and find the shortest path to starting point

		} else {
			for !game.foundControlRoom { // greedy algorithm to find the control room
				game.currentDirection = game.findDirection(kr, kc, game.currentDirection)
				fmt.Println(game.currentDirection)
				hollowCells = game.getHollowCells()
			}
			if game.foundControlRoom {
				// Go back to starting point by using BFS all visited cells
				// and find the shortest path to starting point
				tX := game.controlRoom.x
				tY := game.controlRoom.y
				fmt.Println(game.shortestPath(tX, tY, kr, kc))
			}
		}
	}

}
