<?hh

function expects_required_a_at_int(
  shape('a' => int) $s,
): void {
}

function passes_optional_a_at_int(
  shape(?'a' => int) $s,
): void {
  expects_required_a_at_int($s);
}
