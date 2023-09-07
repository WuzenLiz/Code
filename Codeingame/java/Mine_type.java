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
import java.util.*;
import java.io.*;
import java.math.*;

class Mine_type{
 public static void main(String[] args){
  Scanner in = new Scanner(System.in);
  int N = in.nextInt();
  int Q = in.nextInt();
  HashMap<String, String> map = new HashMap<String, String>();
  for(int i = 0; i < N; i++){
   String EXT = in.next();
   String MT = in.next();
   map.put(EXT.toLowerCase(), MT);
  }
  for(int i = 0; i < Q; i++){
   String FNAME = in.next();
   String ext = "UNKNOWN";
   if(FNAME.lastIndexOf(".") > 0){
    ext = FNAME.substring(FNAME.lastIndexOf(".") + 1, FNAME.length()).toLowerCase();
   }
   if(map.containsKey(ext)){
    System.out.println(map.get(ext));
   }else{
    System.out.println("UNKNOWN");
   }
  }
  in.close();
 }
}