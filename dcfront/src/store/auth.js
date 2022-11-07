import $http from '../axios-api'

export default {
    state: {
        token: localStorage.getItem('access_token') || null
    },
    getters: {
        isAuth ({ token }) {
            return Boolean(token)
        }
    },
    mutations: {
        SET_TOKEN (state, token) {
            state.token = `JWT ${token}`
            localStorage.setItem('access_token', `JWT ${token}`)
        }
    },
    actions: {
        login: async ({ commit }, payload) => {
            const { data } = $http.post('/user/api/token/', payload)
                .then(function (res) {
                    if (res.status === 200) {
                        commit('SET_TOKEN', res.data.access)
                        location.href='/'
                    }
                })
            return data
        }
    }
}
