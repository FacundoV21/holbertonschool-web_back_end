export default function handleResponseFromAPI(promise) {
  promise
    .then(() => { console.log('Got a response from the API'); })
    .then(() => ({
      body: 'success',
      status: 200
    }))
    .catch(() => new Error());
}
