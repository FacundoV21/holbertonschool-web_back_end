export default function getListStudentIds(arr) {
  const retArr = [];
  if (Array.isArray(arr)) {
    let retArr = arr.map(function(element){
        return arr.id;
    })
  }
  return (retArr);
}
