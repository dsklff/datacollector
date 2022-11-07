<template>
    <div class="nav-bar">
        <div>
            <b-navbar toggleable="lg" type="dark" variant="dark">
                <b-navbar-brand href="#">Diploma</b-navbar-brand>

                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

                <b-collapse id="nav-collapse" is-nav>
                    <b-navbar-nav>
                        <b-nav-item class="test" type="dark"><router-link style="color: #ffffff" :to = "{ name: 'publications' }">Publications</router-link></b-nav-item>
                        <b-nav-item class="test" type="dark"><router-link style="color: #ffffff" :to="{ name:'disciplines'}">Disciplines</router-link></b-nav-item>
                    </b-navbar-nav>

                    <!-- Right aligned nav items -->
                    <b-navbar-nav class="ml-auto">
                        <b-nav-item-dropdown right>
                            <!-- Using 'button-content' slot -->
                            <template #button-content>
                                <em>{{ usersdata.user.kbtu_mail }}</em>
                            </template>
                            <b-dropdown-item><router-link :to = "{ name:'profile' }">Profile</router-link></b-dropdown-item>
                            <b-dropdown-item @click="logout">Sign Out</b-dropdown-item>
                        </b-nav-item-dropdown>
                    </b-navbar-nav>
                </b-collapse>
            </b-navbar>
        </div>




<!--        <nav class="navbar navbar-expand-lg navbar-light bg-white nav-1">-->
<!--            <div class="container mw-0 px-3">-->

<!--                <a class="navbar-brand" href="#">-->
<!--                    <img src="../assets/logo.png" width="" height="27" class="d-inline-block align-top" alt="" loading="lazy">-->
<!--                </a>-->
<!--                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">-->
<!--                    <span class="navbar-toggler-icon"></span>-->
<!--                </button>-->

<!--                <div class="collapse navbar-collapse" id="navbarSupportedContent">-->
<!--                    <ul class="navbar-nav mr-auto">-->
<!--                        <li class="nav-item" v-if="accessToken!=null"><router-link :to = "{ name:'profile' }">Profile</router-link></li>-->
<!--                    </ul>-->
<!--                </div>-->

<!--                <div class="collapse navbar-collapse" id="navbarSupportedContent2">-->
<!--                    <ul class="navbar-nav mr-auto">-->
<!--&lt;!&ndash;                        <li class="nav-item" v-if="accessToken!=null"><router-link :to = "{ name:'logout' }">Logout</router-link></li>&ndash;&gt;-->
<!--                            <button @click="logout"></button>-->
<!--                    </ul>-->
<!--                </div>-->

<!--            </div>-->
<!--        </nav>-->





    </div>
</template>



<script>
    import { mapState } from 'vuex'
    import $http from "../axios-api";
    export default {
        data () {
            return {
                usersdata: ''
            }
        },
        name: 'Navbar',
        computed: mapState(['accessToken']),
        methods: {
            logout() {
                localStorage.removeItem('access_token');
                document.location.reload()
            },

            getProfile() {
                $http.get('/user/get_profile/')
                    .then(response => {
                        this.usersdata = response.data
                    })
            }
        },

        mounted() {
            this.getProfile()
        },

    }
</script>

<style scoped>
    a {
        color:#000;
    }

    .test {
        color: #ffffff;
    }
</style>
