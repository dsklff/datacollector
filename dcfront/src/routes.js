import Vue from 'vue'
import VueRouter from 'vue-router'
import Publications from './views/Publications'
import Login from './views/Login'
import Logout from './views/Logout'
import Register from './views/Register'
import Test from './views/Test'
import Profile from './views/Profile'
import Activate from './views/Activate'
import Publication from './views/Publication'
import EditProfile from './views/EditProfile'
import Discipline from './views/Discipline'
import Disciplines from './views/Disciplines'

Vue.use(VueRouter);

export default new VueRouter({

    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'publications',
            component: Publications,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/login',
            name: 'login',
            component: Login,
        },
        {
            path: '/logout',
            name: 'logout',
            component: Logout,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/register',
            name: 'register',
            component: Register,
        },
        {
            path: '/test',
            name: 'test',
            component: Test,
        },
        {
            path: '/profile',
            name: 'profile',
            component: Profile,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/activate',
            name: 'activate',
            component: Activate,
        },
        {
            path: '/publication/:id',
            name: 'publication',
            component: Publication,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/edit-profile',
            name: 'edit-profile',
            component: EditProfile,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/disciplines',
            name: 'disciplines',
            component: Disciplines,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/discipline/:id',
            name: 'discipline',
            component: Discipline,
            meta: {
                requiresLogin: true
            }
        }
    ]
})
