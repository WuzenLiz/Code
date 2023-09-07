/*
Game Input
Input
Line 1: Number N of elements which make up the association table.

Line 2: Number Q of file names to be analyzed.

N following lines: One file extension per line and the corresponding MIME type (separated by a blank space).

Q following lines: One file name per line.

Output
For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
Constraints
0 < N < 10000
0 < Q < 10000
File extensions are composed of a maximum of 10 alphanumerical ASCII characters.
MIME types are composed of a maximum 50 alphanumerical and punctuation ASCII characters.
File names are composed of a maximum of 256 alphanumerical ASCII characters and dots (full stops).
There are no spaces in the file names, extensions or MIME types.
*/
using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class solution{

  static void Main(string[] args){
    // read input
    int N = int.Parse(Console.ReadLine()); // Number of elements which make up the association table.
    int Q = int.Parse(Console.ReadLine()); // Number Q of file names to be analyzed.
    Dictionary<string, string> mimeTypes = new Dictionary<string, string>();
    for (int i = 0; i < N; i++){
      string[] inputs = Console.ReadLine().Split(' ');
      string EXT = inputs[0]; // file extension
      string MT = inputs[1]; // MIME type.
      mimeTypes.Add(EXT.ToLower(), MT);
    }

    for (int i = 0; i < Q; i++){
      string FNAME = Console.ReadLine(); // One file name per line.
      string[] file = FNAME.Split('.');
      string ext = file.Length > 1 ? file[file.Length - 1].ToLower() : "";
      if (mimeTypes.ContainsKey(ext)){
        Console.WriteLine(mimeTypes[ext]);
      } else {
        Console.WriteLine("UNKNOWN");
      }
    }
  }

}