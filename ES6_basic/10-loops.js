export default function appendToEachArrayValue(array, appendString) {
  const arr2 = []
  for (const idx of array) {
    arr2.push(appendString + idx);
  }

  return arr2;
}
