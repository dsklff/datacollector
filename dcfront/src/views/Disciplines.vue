<template>
    <div class="publications">
        <NavBar></NavBar>
        <b-button class="add-discipline-button" id="show-btn" @click="showDisciplineModal">Add Discipline</b-button>
        <b-modal ref="discipline-modal" hide-footer title="Add discipline">
            <div class="d-block text-center">
                <form v-on:submit.prevent="addDiscipline">
                    <div class="form-group">
                        <input type="text" name="name" id="name" v-model="discipline.name" class="form-control" placeholder="Discipline name">
                    </div>
                    <div class="form-group">
                        <input type="text" name="credit_amount" id="credit_amount" v-model="discipline.credit_amount" class="form-control" placeholder="Discipline credit amount">
                    </div>
                    <div class="form-group">
                        <input type="text" name="desc" id="desc" v-model="discipline.desc" class="form-control" placeholder="Discipline description">
                    </div>

                    <button type="submit" class="btn btn-lg btn-primary btn-block">Add discipline</button>
                </form>
            </div>
            <!--                <b-button class="mt-3" variant="outline-danger" block @click="hideJournalModal">Close Me</b-button>-->
        </b-modal>

        <div>
            <table>
                <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Credit amount</th>
                    <th>Description</th>
                    <th>Delete</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="discipline in disciplines" :key="discipline.id">
                    <td><strong>{{discipline.id}}</strong></td>
                    <td><a @click="getDiscipline(discipline.id)" class="text-secondary">{{discipline.name}}</a></td>
                    <td>{{discipline.credit_amount}}</td>
                    <td>{{discipline.desc}}</td>
                    <td><button @click="deleteDiscipline(discipline.id)">Delete</button></td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>




<script>
    import NavBar from '../components/Navbar'
    import $http from '../axios-api'
    // import { mapState } from 'vuex'

    export default {
        name: 'Disciplines',
        data () {
            return {
                disciplines: {},
                discipline: {
                    name: '',
                    desc: '',
                    credit_amount: ''
                }
            }
        },
        components: {
            NavBar
        },
        methods: {
            async getDisciplines () {
                try {
                    await $http.get('/disciplines/')
                        .then(response => {
                            this.disciplines = response.data
                        })
                    console.log(this.disciplines)
                } catch(error) {
                    console.log(error)
                }
            },

            getDiscipline (id) {
                this.$router.push({ path: `discipline/${id}`})
            },

            async deleteDiscipline(id) {
                try {
                    await $http.delete(`/disciplines/${id}/`)
                        .then(response => {
                            console.log(response)
                            location.reload()
                        })
                } catch(error) {
                    console.log(error)
                }
            },

            showDisciplineModal () {
                this.$refs['discipline-modal'].show()
            },

            async addDiscipline () {
                try {
                    await $http.post('/disciplines/', {
                        name: this.discipline.name,
                        credit_amount: this.discipline.credit_amount,
                        desc: this.discipline.desc
                    })
                        .then(() => {
                            // console.log(response)
                            location.reload()
                        })
                } catch(error) {
                    console.log(error)
                }
            },


        },
        // created () {
        //     $http.get('/publications/')
        //         .then(response => {
        //             this.$store.state.APIData = response.data
        //         })
        //         .catch(err => {
        //             console.log(err)
        //         })
        // }

        mounted() {
            this.getDisciplines()
        }
    }
</script>

<style>
    body {
        background: #fafafa url(https://jackrugile.com/images/misc/noise-diagonal.png);
        color: #444;
        font: 100%/30px 'Helvetica Neue', helvetica, arial, sans-serif;
        text-shadow: 0 1px 0 #fff;
    }

    strong {
        font-weight: bold;
    }

    em {
        font-style: italic;
    }

    table {
        background: #f5f5f5;
        border-collapse: separate;
        box-shadow: inset 0 1px 0 #fff;
        font-size: 12px;
        line-height: 24px;
        margin: 30px auto;
        text-align: left;
        width: 800px;
    }

    th {
        background: url(https://jackrugile.com/images/misc/noise-diagonal.png), linear-gradient(#777, #444);
        border-left: 1px solid #555;
        border-right: 1px solid #777;
        border-top: 1px solid #555;
        border-bottom: 1px solid #333;
        box-shadow: inset 0 1px 0 #999;
        color: #fff;
        font-weight: bold;
        padding: 10px 15px;
        position: relative;
        text-shadow: 0 1px 0 #000;
    }

    th:after {
        background: linear-gradient(rgba(255,255,255,0), rgba(255,255,255,.08));
        content: '';
        display: block;
        height: 25%;
        left: 0;
        margin: 1px 0 0 0;
        position: absolute;
        top: 25%;
        width: 100%;
    }

    th:first-child {
        border-left: 1px solid #777;
        box-shadow: inset 1px 1px 0 #999;
    }

    th:last-child {
        box-shadow: inset -1px 1px 0 #999;
    }

    td {
        border-right: 1px solid #fff;
        border-left: 1px solid #e8e8e8;
        border-top: 1px solid #fff;
        border-bottom: 1px solid #e8e8e8;
        padding: 10px 15px;
        position: relative;
        transition: all 300ms;
    }

    /*td:first-child {*/
    /*    box-shadow: inset 1px 0 0 #fff;*/
    /*}*/

    /*td:last-child {*/
    /*    border-right: 1px solid #e8e8e8;*/
    /*    box-shadow: inset -1px 0 0 #fff;*/
    /*}*/

    tr {
        background: url(https://jackrugile.com/images/misc/noise-diagonal.png);
    }

    tr:nth-child(odd) td {
        background: #f1f1f1 url(https://jackrugile.com/images/misc/noise-diagonal.png);
    }

    /*tr:last-of-type td {*/
    /*    box-shadow: inset 0 -1px 0 #fff;*/
    /*}*/

    /*tr:last-of-type td:first-child {*/
    /*    box-shadow: inset 1px -1px 0 #fff;*/
    /*}*/

    /*tr:last-of-type td:last-child {*/
    /*    box-shadow: inset -1px -1px 0 #fff;*/
    /*}*/

    tbody:hover td {
        color: transparent;
        text-shadow: 0 0 3px #aaa;
    }

    tbody:hover tr:hover td {
        color: #444;
        text-shadow: 0 1px 0 #fff;
    }

    .add-discipline-button {
        margin-top: 25px;
        margin-left: 25px;
    }
</style>
