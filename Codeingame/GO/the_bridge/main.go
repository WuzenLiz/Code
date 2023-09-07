package main

import "fmt"

func run(speed int, grid [][]string, motorbikes [][]int) string {
	/* return the next move ( SPEED SLOW JUMP WAIT UP DOWN )
	 * SPEED: increase speed
	 * SLOW: decrease speed
	 * JUMP: jump
	 * WAIT: wait
	 * UP: turn up
	 * DOWN: turn down
	 */
	for i := 0; i < len(motorbikes); i++ {
		if motorbikes[i][2] == 1 { // if motorbike is alive
			// check if there is a hole in front of the motorbike (1 to speed have holes)
			for j := 1; j <= speed; j++ {
				if motorbikes[i][1]+j < len(grid) && grid[motorbikes[i][1]+j][motorbikes[i][0]] == "0" {
					return "JUMP"
				}
				// check if there is a hole in front of the motorbike (1 to speed have holes) but can't jump so tried to Up or Down
			}
			if motorbikes[i][1]+speed < len(grid) && grid[motorbikes[i][1]+speed][motorbikes[i][0]] == "." || grid[motorbikes[i][1]-speed][motorbikes[i][0]] == "." {
				if motorbikes[i][0] > 0 && grid[motorbikes[i][1]+speed][motorbikes[i][0]-1] == "0" {
					return "UP"
				} else if motorbikes[i][0] < len(grid[0])-1 && grid[motorbikes[i][1]-speed][motorbikes[i][0]+1] == "0" {
					return "DOWN"
				}
			}
		}
	}
	return "SPEED"
}

func main() {
	// M: the amount of motorbikes to control
	var M int
	fmt.Scan(&M)

	// V: the minimum amount of motorbikes that must survive
	var V int
	fmt.Scan(&V)

	// L0: L0 to L3 are lanes of the road. A dot character . represents a safe space, a zero 0 represents a hole in the road.
	var L0 string
	fmt.Scan(&L0)

	var L1 string
	fmt.Scan(&L1)

	var L2 string
	fmt.Scan(&L2)

	var L3 string
	fmt.Scan(&L3)

	grid := [][]string{{L0}, {L1}, {L2}, {L3}}

	for {
		// S: the motorbikes' speed
		var S int
		fmt.Scan(&S)

		moto := make([][]int, M)
		for i := 0; i < M; i++ {
			// X: x coordinate of the motorbike
			// Y: y coordinate of the motorbike
			// A: indicates whether the motorbike is activated "1" or detroyed "0"
			var X, Y, A int
			fmt.Scan(&X, &Y, &A)
			moto[i] = []int{X, Y, A}
		}

		fmt.Println(run(S, grid, moto))

	}
}
