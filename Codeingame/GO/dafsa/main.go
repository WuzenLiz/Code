package main

import (
	"bufio"
	"fmt"
	"os"
)

type State struct {
	Transitions map[rune]*State
	IsFinal     bool
}

func NewState() *State {
	return &State{
		Transitions: make(map[rune]*State),
		IsFinal:     false,
	}
}

type DAFSA struct {
	Start *State
}

func NewDAFSA() *DAFSA {
	return &DAFSA{
		Start: NewState(),
	}
}

func (d *DAFSA) AddWord(word string) {
	current := d.Start
	for _, char := range word {
		nextState, exists := current.Transitions[char]
		if !exists {
			nextState = NewState()
			current.Transitions[char] = nextState
		}
		current = nextState
	}
	current.IsFinal = true
}

func NodeCount(node *State) int {
	count := 1 // Count the current node

	for _, nextState := range node.Transitions {
		count += NodeCount(nextState) // Recursively count nodes in child states
	}

	return count
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	// N: the number of words
	var N int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &N)

	dafsa := NewDAFSA()

	// Add words to the graph
	words := make([]string, N)
	for i := 0; i < N; i++ {
		scanner.Scan()
		words[i] = scanner.Text()
		dafsa.AddWord(words[i])
	}

	// Count nodes in the DAFSA
	nodeCount := NodeCount(dafsa.Start)
	fmt.Printf("%d\n", nodeCount)
}
