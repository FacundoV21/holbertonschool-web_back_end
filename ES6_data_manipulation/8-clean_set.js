function cleanSet(inputSet, startString) {
  const filteredValues = Array.from(inputSet).filter(value => value.startsWith(startString));
  const resultString = filteredValues.map(value => value.substring(startString.length)).join('-');
  return resultString;
}
