<?hh
/* Prototype  : int vfprintf  ( resource $handle  , string $format , array $args  )
 * Description: Write a formatted string to a stream
 * Source code: ext/standard/formatted_print.c
*/
<<__EntryPoint>> function main(): void {
echo "*** Testing vfprintf) : basic functionality - using hexadecimal format ***\n";

// Initialising different format strings
$format = "format";
$format1 = "%x";
$format2 = "%x %x";
$format3 = "%x %x %x";

$format11 = "%X";
$format22 = "%X %X";
$format33 = "%X %X %X";

$arg1 = vec[11];
$arg2 = vec[11,132];
$arg3 = vec[11,132,177];

/* creating dumping file */
$data_file = sys_get_temp_dir().'/'.'vfprintf_basic9.txt';
if (!($fp = fopen($data_file, 'wt')))
   return;

vfprintf($fp, $format1, $arg1);
fprintf($fp, "\n");
vfprintf($fp, $format11, $arg1);
fprintf($fp, "\n");

vfprintf($fp, $format2, $arg2);
fprintf($fp, "\n");
vfprintf($fp, $format22, $arg2);
fprintf($fp, "\n");

vfprintf($fp, $format3, $arg3);
fprintf($fp, "\n");
vfprintf($fp, $format33, $arg3);
fprintf($fp, "\n");

fclose($fp);
print_r(file_get_contents($data_file));

unlink($data_file);
echo "===DONE===\n";
}
