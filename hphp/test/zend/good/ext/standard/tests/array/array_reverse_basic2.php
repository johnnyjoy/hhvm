<?hh
/* Prototype  : array array_reverse(array $array [, bool $preserve_keys])
 * Description: Return input as a new array with the order of the entries reversed 
 * Source code: ext/standard/array.c
*/

/*
 * Testing array_reverse() with associative array for $array argument
*/
<<__EntryPoint>> function main(): void {
echo "*** Testing array_reverse() : basic functionality ***\n";

// Initialise the array
$array = dict["a" => "hello", 123 => "number", 'string' => 'blue', "10" => 13.33];

// Calling array_reverse() with default arguments
var_dump( array_reverse($array) );

// Calling array_reverse() with all possible arguments
var_dump( array_reverse($array, true) );  // expects the keys to be preserved
var_dump( array_reverse($array, false) );  // expects the keys not to be preserved

echo "Done";
}
