package main

import (
	"bufio"
	"fmt"
	"os"
)

var L, H int

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 100000000), 100000000)
	// input L H
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &L)
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &H)
	// Map input
	landMap := make([]string, L*H)
	for y := 0; y < H; y++ {
		scanner.Scan()
		line := scanner.Text()
		for x := 0; x < L; x++ {
			landMap[calculateIndex(x, y)] = line[x : x+1]
		}
	}
	// input N
	scanner.Scan()
	N := 0
	fmt.Sscanf(scanner.Text(), "%d", &N)
	// input x y list
	for i := 0; i < N; i++ {
		scanner.Scan()
		x, y := 0, 0
		fmt.Sscanf(scanner.Text(), "%d %d", &x, &y)
		area := calculateArea(landMap, x, y, 2)
		fmt.Println(area)
		resetLandMap(landMap)
	}

}

func calculateIndex(x, y int) int {
	return y*L + x
}

func calculateArea(landMap []string, x, y, ndx int) int {
	// stack for DFS
	queue := make([]int, 0, L*H)
	area := 0
	// push
	queue = append(queue, calculateIndex(x, y))
	// while stack is not empty
	for len(queue) > 0 {
		// pop
		current := queue[0]
		queue = queue[1:]
		// if current is not visited
		if landMap[current] == "O" {
			// mark as visited
			landMap[current] = fmt.Sprintf("%d", ndx)
			// add to area
			area++
			// add neighbors to stack
			queue = append(queue, getNeighbors(landMap, current)...)
		}
	}
	return area
}

func getNeighbors(landMap []string, current int) []int {
	neighbors := []int{}
	// up
	if current >= L {
		neighbors = append(neighbors, current-L)
	}
	// down
	if current < L*(H-1) {
		neighbors = append(neighbors, current+L)
	}
	// left
	if current%L != 0 {
		neighbors = append(neighbors, current-1)
	}
	// right
	if (current+1)%L != 0 {
		neighbors = append(neighbors, current+1)
	}
	return neighbors
}

func resetLandMap(landMap []string) {
	for i := 0; i < len(landMap); i++ {
		if landMap[i] == "2" {
			landMap[i] = "O"
		}
	}
}
