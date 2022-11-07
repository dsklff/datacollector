<template>
    <div>
        <div class="container text-dark">
            <div class="row justify-content-md-center">
                <div class="col-md-5 p-3 login justify-content-md-center">
                    <h1 class="h3 mb-3 font-weight-normal text-center" style="font-size: 50px">Sign in</h1>

                    <p v-if="payload.incorrectAuth">Incorrect username or password entered - please try again</p>
                    <form v-on:submit.prevent="login">
                        <div class="form-group">
                            <img style="margin-left: 8px;" src="../assets/kbtu.png">
                        </div>
                        <div class="form-group">
                            <input type="text" name="username" id="user" v-model="payload.kbtu_mail" class="form-control" placeholder="KBTU domain email">
                        </div>
                        <div class="form-group">
                            <input type="password" name="password" id="pass" v-model="payload.password" class="form-control" placeholder="Password">
                        </div>
                        <button type="submit" class="btn btn-lg btn-primary btn-block">Login</button>
                        <p style="margin-top: 20px; margin-left: 100px">Don't have an account? <router-link :to = "{ name:'register' }">Sign up</router-link></p>
                    </form>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'login',
        data () {
            return {
                payload: {
                    kbtu_mail: '',
                    password: '',
                    incorrectAuth: false
                },
            }
        },
        methods: {
            // login () {
            //     this.$store.dispatch('userLogin', {
            //         username: this.username,
            //         password: this.password
            //     })
            //         .then(() => {
            //             this.$router.push({ name: 'publications' })
            //         })
            //         .catch(err => {
            //             console.log(err)
            //             this.incorrectAuth = true
            //         })
            // }

            // gekyume

            async login () {
                try {
                    const response = await this.$store.dispatch('login', this.payload)
                    console.log(response)
                } catch (error) {
                    this.payload.incorrectAuth = true
                    console.log(error)
                }
            }
        },

        created() {
            localStorage.removeItem('access_token');
        }
    }
</script>

<style>
    body {
        background-color:#f4f4f4;
    }
    .login{
        background-color:#fff;
        margin-top:10%;
    }
    input {
        padding: 25px 10px;
    }
</style>
