export default function cleanSet(set, startString) {
  if (startString === undefined || startString === '' || typeof(startString) !== 'string') {
    return '';
  }
  let string = '';
  for (const element of set) {
    if (element.startsWith(startString)) {
      string += element.slice((element.length - (element.length - startString.length)), element.length) + '-';
    }
  }
  string = string.slice(0, string.length - 1);
  return string;
}
