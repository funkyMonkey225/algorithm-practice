// Throws error if value undefined or no arguments given, otherwise returns value

function ensure(value) {
  if(value === undefined) {
    throw new Error('no arguments');
  }

  return value;
}
