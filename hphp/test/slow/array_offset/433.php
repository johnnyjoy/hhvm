<?hh

function foo($p) :mixed{ return $p; }

<<__EntryPoint>> function main(): void {
$a = darray(vec[1, 2, 3, 4]);
$a[123] = 5;
$a["0000"] = 6;
var_dump(foo(__LINE__));
var_dump(foo(vec[]));
var_dump(foo(vec[1, 2, 3]));
var_dump(foo($a[123]));
var_dump(foo($a[0000]));
try { var_dump(foo("$a[123]")); } catch (Exception $e) { echo $e->getMessage()."\n"; }
var_dump(foo("$a[0000]"));
}
