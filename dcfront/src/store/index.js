import Vue from 'vue'
import Vuex from 'vuex'
import auth from './auth'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        accessToken: localStorage.getItem('access_token') || '',
        currentUser: {},
        APIData: '',
    },
    mutations: {

    },
    actions: {

    },
    modules: {
        auth
    },
    getters: {
        getAccessToken: state => {
            return state.accessToken
        }
    }
})
