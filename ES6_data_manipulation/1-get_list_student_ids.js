export default function getListStudentIds(arr) {
  let respuesta = [];
  if (Array.isArray(arr)) {
    respuesta = arr.map((item) => item.id);
  }
  return respuesta;
}
