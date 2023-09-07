/*
Using recursive functions on a large 2 dimensional grid, you implement flood filling algorithm and have to improve the performance of your code using memoization.

Algorithm: Flood Fill, Memoization (Dynamic Programming), BFS, recursion
Rule: Your program receives as input a list of coordinates. For each one you must determine the surface area of the lake which is located there. If there is no lake, then the surface area equals 0.
Input:
Line 1: Two integers L and H representing the width and height of the map.
Next H lines: L characters representing one line of the ASCII map.
Next line: An integer N representing the number of coordinates to be processed.
Next N lines: Two integers X and Y representing the coordinates for which you have to compute the surface area of the lake.
Output:
N lines: The surface area of the lake for each coordinate.
*/

use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn calculate_for_area(map: Vec<char>, x: i32, y: i32, ndx: i32) -> i32 {
    let stack = [(x,y)];
    let area = 0;

    while stack.len() > 0 {
        // remove last element from stack
        let index = stack.iter().possition(|&r| r == stack.len() - 1).unwrap();
        let (x, y) = stack[index];
        stack.remove(index);
        // if current cell is 'O' then replace it with ndx and add neighbors to stack
        if map[(y * x) as usize] == 'O' {
            map[(y * x) as usize] = ndx.to_string().chars().nth(0).unwrap();
            area += 1;
            if x > 0 {
                stack.push((x-1, y));
            }
            if x < map.len() as i32 {
                stack.push((x+1, y));
            }
            if y > 0 {
                stack.push((x, y-1));
            }
            if y < map.len() as i32 {
                stack.push((x, y+1));
            }
        }
    }
    return area
}

fn main() {
    // input L H
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let inputs = input_line.split(" ").collect::<Vec<_>>();
    let l = parse_input!(inputs[0], i32); // width of the map
    let h = parse_input!(inputs[1], i32); // height of the map
    let mut map = Vec::new();

    // input map
    for y in 0..h as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let row = input_line.trim_matches('\n').to_string();
        for x in 0..l as usize {
            map.push(row.chars().nth(x).unwrap());
        }
    }

    // input N
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32); // number of coordinates to be processed

    // input coordinates
    for i in 0..n as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let inputs = input_line.split(" ").collect::<Vec<_>>();
        let x = parse_input!(inputs[0], i32);
        let y = parse_input!(inputs[1], i32);

        println!("{}", calculate_for_area(map, x, y, i+2));
    }
}