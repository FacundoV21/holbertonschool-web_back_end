export default function appendToEachArrayValue(array, appendString) {
  const arr2 = []
  for (const idx in array) {
    arr2.push(appendString + idx)   ;
  }

  return arr2;
}
