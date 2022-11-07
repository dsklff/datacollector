<template>
    <div>
        <div class="container text-dark">
            <div class="row justify-content-md-center">
                <div class="col-md-5 p-3 login justify-content-md-center">
                    <h1 class="h3 mb-3 font-weight-normal text-center" style="font-size: 50px">Sign up</h1>
                    <form v-on:submit.prevent="register">
                        <div class="form-group">
                            <img style="margin-left: 8px;" src="../assets/kbtu.png">
                        </div>
                        <div class="form-group">
                            <input type="text" name="username" id="user" v-model="username" class="form-control" placeholder="Username">
                        </div>
                        <div class="form-group">
                            <input type="password" name="password" id="pass" v-model="password" class="form-control" placeholder="Password">
                        </div>
                        <div class="form-group">
                            <input type="password" name="confirm_password" id="confirm_pass" v-model="confirm_password" class="form-control" placeholder="Confirm Password">
                        </div>
                        <button type="submit" class="btn btn-lg btn-primary btn-block">Register</button>
                        <p style="margin-top: 20px; margin-left: 160px"><router-link :to = "{ name:'login' }">Back to Sign In</router-link></p>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import $http from '../axios-api'
    export default {
        name: 'register',
        data () {
            return {
                username: '',
                password: '',
                confirm_password: ''
            }
        },
        methods: {
            register () {
                try {
                    $http.post('/user/register/', {
                        kbtu_mail: this.username,
                        password: this.password,
                        confirm_password: this.confirm_password
                    })
                        .then(() => {
                            this.$router.push({ name: 'activate' });
                        })
                } catch(error) {
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

</style>
