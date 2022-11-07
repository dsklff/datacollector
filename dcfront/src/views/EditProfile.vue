<template>
    <div class="profile-edit">
        <NavBar></NavBar>
        <div class="container emp-profile">
            <form method="post">
                <div class="row">
                    <div class="col-md-4">
                        <div class="profile-img">
                            <img style="width: 150px; height: 150px; border-radius: 5px" v-bind:src="this.usersdata.avatar_url" alt=""/>                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="profile-head">
                            <h5>
                                {{this.usersdata.full_name}}
                            </h5>
                            <h6>
                                {{this.usersdata.degree}}
                            </h6>
                            <ul class="nav nav-tabs" id="myTab" role="tablist">
                                <li class="nav-item">
                                    <a class="nav-link active" id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-selected="true">About</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <router-link :to = "{ name: 'profile' }"><input type="submit" class="profile-edit-btn" name="btnAddMore" value="Profile"/></router-link>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-4">
                        <div class="profile-work">

                        </div>
                    </div>
                    <div class="col-md-8">
                        <div class="tab-content profile-tab" id="myTabContent">
                            <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
                                <form v-on:submit.prevent="editProfile">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <label>Name</label>
                                        </div>
                                        <div class="col-md-6 form-group">
                                            <input type="text" name="username" id="full_name" v-model="user.full_name" class="form-control" placeholder="Full Name">
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6">
                                            <label>Phone</label>
                                        </div>
                                        <div class="col-md-6 form-group">
                                            <input type="text" name="username" id="user" v-model="user.phone" class="form-control" placeholder="Phone">
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6">
                                            <label>Faculty</label>
                                        </div>
                                        <div class="col-md-6 form-group">
                                            <b-form-select v-model="user.faculty" :options="faculties"></b-form-select>
<!--                                            <select>-->
<!--                                                <option v-for="faculty in faculties" :key="faculty.faculty">-->
<!--                                                    {{faculty.faculty}}-->
<!--                                                </option>-->
<!--                                            </select>-->
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6 form-group">
                                            <label>Degree</label>
                                        </div>
                                        <div class="col-md-6 form-group">
                                            <b-form-select v-model="user.degree" :options="degrees"></b-form-select>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6">
                                            <label>Gender</label>
                                        </div>
                                        <div class="col-md-6 form-group">
                                            <b-form-select v-model="user.gender" :options="genders"></b-form-select>
                                        </div>
                                        <div class="col-md-6">
                                            <label>Profile image</label>
                                        </div>
                                        <div class="col-md-6 form-group">
                                            <input type="file" name="file" id="file" ref="file" v-on:change="handleFileUpload" class="form-control" placeholder="Journal Issue">
                                        </div>
                                    </div>
                                    <button type="submit" class="btn btn-lg btn-primary btn-block">Edit profile</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
    import NavBar from '../components/Navbar'
    import $http from '../axios-api'
    export default {
        data () {
            return {
                usersdata: '',
                faculties: [
                    {
                        value: 'Faculty of Information Technologies',
                        text: 'Faculty of Information Technologies'
                    },
                    {
                        value: 'Faculty of Geology and Geological Exploration',
                        text: 'Faculty of Geology and Geological Exploration'
                    },
                    {
                        value: 'Faculty of Energy and Oil and Gas Industry',
                        text: 'Faculty of Energy and Oil and Gas Industry'
                    },
                    {
                        value: 'Faculty of General Education',
                        text: 'Faculty of General Education'
                    },
                    {
                        value: 'Business School',
                        text: 'Business School'
                    },
                    {
                        value: 'International School of Economics',
                        text: 'International School of Economics'
                    },
                    {
                        value: 'Kazakhstan Maritime Academy',
                        text: 'Kazakhstan Maritime Academy'
                    },
                    {
                        value: 'School of Mathematics and Cybernetics',
                        text: 'School of Mathematics and Cybernetics'
                    },
                    {
                        value: 'School of Chemical Engineering',
                        text: 'School of Chemical Engineering'
                    }
                ],
                degrees: [
                    {
                        value: 'Laboratory assistant',
                        text: 'Laboratory assistant'
                    },
                    {
                        value: 'Senior laboratory assistant',
                        text: 'Senior laboratory assistant'
                    },
                    {
                        value: 'Assistant',
                        text: 'Assistant'
                    },
                    {
                        value: 'Lecturer',
                        text: 'Lecturer'
                    },
                    {
                        value: 'Senior Lecturer',
                        text: 'Senior Lecturer'
                    },
                    {
                        value: 'Assistant Professor',
                        text: 'Assistant Professor'
                    },
                    {
                        value: 'Associate Professor',
                        text: 'Associate Professor'
                    },
                    {
                        value: 'Professor',
                        text: 'Professor'
                    }
                ],
                genders: [
                    {
                        value: 'Male',
                        text: 'Male'
                    },
                    {
                        value: 'Female',
                        text: 'Female'
                    }
                ],
                user: {
                    full_name: '',
                    phone: '',
                    faculty: '',
                    degree: '',
                    gender: '',
                    avatar: []
                }
            }
        },
        name: 'Profile',
        components: {
            NavBar
        },
        methods: {
            async getProfile () {
                try {
                    await $http.get('/user/get_profile/')
                        .then(response => {
                            this.usersdata = response.data
                        })
                } catch(error) {
                    console.log(error)
                }
            },

            handleFileUpload () {
                this.user.avatar = this.$refs.file.files[0];
            },

            async editProfile () {

                let data = new FormData();
                data.append('full_name', this.user.full_name);
                data.append('phone', this.user.phone);
                data.append('faculty', this.user.faculty);
                data.append('degree', this.user.degree);
                data.append('gender', this.user.gender);
                data.append('avatar', this.user.avatar);

                try {
                    $http.put(`/user/edit_profile/`, data, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                        .then((response) => {
                            console.log(response)
                            this.$router.push({ name: 'profile' });
                        })
                } catch(error) {
                    console.log(error)
                }
            },




        },

        mounted() {
            this.getProfile()
        }
    }
</script>

<style>

</style>
