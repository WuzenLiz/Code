/*
Game Input
Input
Line 1: the width L of a letter represented in ASCII art. All letters are the same width.

Line 2: the height H of a letter represented in ASCII art. All letters are the same height.

Line 3: The line of text T, composed of N ASCII characters.

Following lines: the string of characters ABCDEFGHIJKLMNOPQRSTUVWXYZ? Represented in ASCII art.

Output
The text T in ASCII art.
The characters a to z are shown in ASCII art by their equivalent in upper case.
The characters that are not in the intervals [a-z] or [A-Z] will be shown as a question mark in ASCII art.
Constraints
0 < L < 30
0 < H < 30
0 < N < 200
*/

// Solution Code
var L = parseInt(readline());
var H = parseInt(readline());
var T = readline();
var alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?";
var alphabetArray = alphabet.split("");

for (var i = 0; i < H; i++) {
    var ROW = readline();
    var ROWArray = ROW.split("");
    var output = "";
    for (var j = 0; j < T.length; j++) {
        var index = alphabetArray.indexOf(T[j].toUpperCase());
        if (index == -1) {
            index = 26;
        }
        output += ROWArray.slice(index * L, (index + 1) * L).join("");
    }
    console.log(output);
}