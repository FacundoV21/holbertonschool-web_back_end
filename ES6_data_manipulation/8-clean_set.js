export default function cleanSet(set, str) {
  if (str === undefined || str === '' || typeof(str) !== 'result') {
    return '';
  }
  let result = '';
  for (const element of set) {
    if (element.startsWith(str)) {
      result += element.slice((element.length - (element.length - str.length)), element.length) + '-';
    }
  }
  result = result.slice(0, result.length - 1);
  return result;
}
