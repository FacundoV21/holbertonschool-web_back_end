export default function getListStudentIds(arr) {
  const retArr = [];
  if (Array.isArray(arr)) {
    for (user of arr) {
      retArr.push(user.id);
    }
  }
  return (retArr);
}
