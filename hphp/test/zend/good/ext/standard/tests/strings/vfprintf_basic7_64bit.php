<?hh
/* Prototype  : int vfprintf  ( resource $handle  , string $format , array $args  )
 * Description: Write a formatted string to a stream
 * Source code: ext/standard/formatted_print.c
*/
<<__EntryPoint>> function main(): void {
echo "*** Testing vfprintf() : basic functionality - using unsigned format ***\n";

// Initialise all required variables
$format = "format";
$format1 = "%u";
$format2 = "%u %u";
$format3 = "%u %u %u";
$arg1 = vec[-1111];
$arg2 = vec[-1111,-1234567];
$arg3 = vec[-1111,-1234567,-2345432];

/* creating dumping file */
$data_file = sys_get_temp_dir().'/'.'vfprintf_basic7_64bit.txt';
if (!($fp = fopen($data_file, 'wt')))
   return;
   
vfprintf($fp, $format1,$arg1);
fprintf($fp, "\n");

vfprintf($fp, $format2,$arg2);
fprintf($fp, "\n");

vfprintf($fp, $format3,$arg3);
fprintf($fp, "\n");

fclose($fp);
print_r(file_get_contents($data_file));

unlink($data_file);

echo "===DONE===\n";
}
