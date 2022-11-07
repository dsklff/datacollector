import Axios from 'axios'

const $http = Axios
$http.defaults.baseURL = 'http://localhost:8000'
const accessToken = localStorage.getItem('access_token')

if (accessToken) {
    $http.defaults.headers.Authorization = accessToken
}

export default $http

// const getApi = axios.create({
//     baseURL: 'http://localhost:8000',
//     timeout: 3000,
// })

// export { getApi }
