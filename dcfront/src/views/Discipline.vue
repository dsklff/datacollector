<template>
    <div>
        <NavBar></NavBar>
        <div>
            <b-card no-body>
                <b-tabs v-model="tabIndex" card>
                    <b-tab title="LabWorks" href="#labworks">
                        <div>
                            <b-button id="show-btn" @click="showLabWorkModal">Add Lab Work</b-button>
                            <table>
                                <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>File</th>
                                    <th>Description</th>
                                    <th>Delete</th>
                                </tr>
                                </thead>
                                <tbody>
                                <tr v-for="labwork in discipline.labworks" :key="labwork.id">
                                    <td><strong>{{labwork.id}}</strong></td>
                                    <td>{{labwork.name}}</td>
                                    <td><a v-bind:href="labwork.file_url">Download</a></td>
                                    <td>{{labwork.desc}}</td>
                                    <td><button @click="deleteLabWork(labwork.id)">Delete</button></td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    </b-tab>


                    <b-tab title="Quizes" href="#quizes">
                        <div>
                            <b-button id="show-btn" @click="showQuizModal">Add Quiz</b-button>
                            <table>
                                <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>File</th>
                                    <th>Description</th>
                                    <th>Delete</th>

                                </tr>
                                </thead>
                                <tbody>
                                <tr v-for="quiz in discipline.quizes" :key="quiz.id">
                                    <td><strong>{{quiz.id}}</strong></td>
                                    <td>{{quiz.name}}</td>
                                    <td><a v-bind:href="quiz.file_url">Download</a></td>
                                    <td>{{labwork.desc}}</td>
                                    <td><button @click="deleteQuiz(quiz.id)">Delete</button></td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    </b-tab>


                    <b-tab title="Midterms" href="#midterms">
                        <div>
                            <b-button id="show-btn" @click="showMidtermModal">Add Midterm</b-button>
                            <table>
                                <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>File</th>
                                    <th>Description</th>
                                    <th>Delete</th>

                                </tr>
                                </thead>
                                <tbody>
                                <tr v-for="midterm in discipline.midterms" :key="midterm.id">
                                    <td><strong>{{midterm.id}}</strong></td>
                                    <td>{{midterm.name}}</td>
                                    <td><a v-bind:href="midterm.file_url">Download</a></td>
                                    <td>{{midterm.desc}}</td>
                                    <td><button @click="deleteMidterm(midterm.id)">Delete</button></td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    </b-tab>


                    <b-tab title="Endterms" href="#endterms">
                        <div>
                            <b-button id="show-btn" @click="showEndtermModal">Add Endterm</b-button>
                            <table>
                                <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>File</th>
                                    <th>Description</th>
                                    <th>Delete</th>

                                </tr>
                                </thead>
                                <tbody>
                                <tr v-for="endterm in discipline.endterms" :key="endterm.id">
                                    <td><strong>{{endterm.id}}</strong></td>
                                    <td>{{endterm.name}}</td>
                                    <td><a v-bind:href="endterm.file_url">Download</a></td>
                                    <td>{{endterm.desc}}</td>
                                    <td><button @click="deleteEndterm(endterm.id)">Delete</button></td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    </b-tab>


                    <b-tab title="TSIS" href="#tsises">
                        <div>
                            <b-button id="show-btn" @click="showTSISModal">Add TSIS</b-button>
                            <table>
                                <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>File</th>
                                    <th>Description</th>
                                    <th>Delete</th>

                                </tr>
                                </thead>
                                <tbody>
                                <tr v-for="tsis in discipline.tsises" :key="tsis.id">
                                    <td><strong>{{tsis.id}}</strong></td>
                                    <td>{{tsis.name}}</td>
                                    <td><a v-bind:href="tsis.file_url">Download</a></td>
                                    <td>{{tsis.desc}}</td>
                                    <td><button @click="deleteTSIS(tsis.id)">Delete</button></td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    </b-tab>


                    <b-tab title="SIS" href="#sises">
                        <div>
                            <b-button id="show-btn" @click="showSISModal">Add SIS</b-button>
                            <table>
                                <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>File</th>
                                    <th>Description</th>
                                    <th>Delete</th>

                                </tr>
                                </thead>
                                <tbody>
                                <tr v-for="sis in discipline.sises" :key="sis.id">
                                    <td><strong>{{sis.id}}</strong></td>
                                    <td>{{sis.name}}</td>
                                    <td><a v-bind:href="sis.file_url">Download</a></td>
                                    <td>{{sis.desc}}</td>
                                    <td><button @click="deleteSIS(sis.id)">Delete</button></td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    </b-tab>


                    <b-tab title="Lectures" href="#lectures">
                        <div>
                            <b-button id="show-btn" @click="showLectureModal">Add Lecture</b-button>
                            <table>
                                <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>File</th>
                                    <th>Description</th>
                                    <th>Delete</th>

                                </tr>
                                </thead>
                                <tbody>
                                <tr v-for="lecture in discipline.lectures" :key="lecture.id">
                                    <td><strong>{{lecture.id}}</strong></td>
                                    <td>{{lecture.name}}</td>
                                    <td><a v-bind:href="lecture.file_url">Download</a></td>
                                    <td>{{lecture.desc}}</td>
                                    <td><button @click="deleteLecture(lecture.id)">Delete</button></td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    </b-tab>


                    <b-tab title="Syllabuses" href="#syllabuses">
                        <div>
                            <b-button id="show-btn" @click="showSyllabusModal">Add Syllabus</b-button>
                            <table>
                                <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>File</th>
                                    <th>Description</th>
                                    <th>Delete</th>

                                </tr>
                                </thead>
                                <tbody>
                                <tr v-for="syllabus in discipline.syllabuses" :key="syllabus.id">
                                    <td><strong>{{syllabus.id}}</strong></td>
                                    <td>{{syllabus.name}}</td>
                                    <td><a v-bind:href="syllabus.file_url">Download</a></td>
                                    <td>{{syllabus.desc}}</td>
                                    <td><button @click="deleteSyllabus(syllabus.id)">Delete</button></td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    </b-tab>


                    <b-tab title="Finals" href="#finals">
                        <div>
                            <b-button id="show-btn" @click="showFinalModal">Add Final</b-button>
                            <table>
                                <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>File</th>
                                    <th>Description</th>
                                    <th>Delete</th>

                                </tr>
                                </thead>
                                <tbody>
                                <tr v-for="final in discipline.finals" :key="final.id">
                                    <td><strong>{{final.id}}</strong></td>
                                    <td>{{final.name}}</td>
                                    <td><a v-bind:href="final.file_url">Download</a></td>
                                    <td>{{final.desc}}</td>
                                    <td><button @click="deleteFinal(final.id)">Delete</button></td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    </b-tab>

                </b-tabs>
            </b-card>
        </div>
        <div>
            <b-modal ref="labwork-modal" hide-footer title="Add Labwork">
                <div class="d-block text-center">
                    <form v-on:submit.prevent="addLabWork">
                        <div class="form-group">
                            <input type="text" name="name" id="labworkName" v-model="labwork.name" class="form-control" placeholder="Labwork Name">
                        </div>
                        <div class="form-group">
                            <input type="text" name="name" id="labworkDesc" v-model="labwork.desc" class="form-control" placeholder="Labwork Desc">
                        </div>
                        <div class="form-group">
                            <input type="file" name="file" id="labworkFile" ref="file" v-on:change="handleLabWorkFileUpload" class="form-control" placeholder="Labwork File">
                        </div>
                        <button type="submit" class="btn btn-lg btn-primary btn-block">Add labwork</button>
                    </form>
                </div>
                <!--                <b-button class="mt-3" variant="outline-danger" block @click="hideAttachmentModal">Close Me</b-button>-->
            </b-modal>


            <b-modal ref="quiz-modal" hide-footer title="Add Quiz">
                <div class="d-block text-center">
                    <form v-on:submit.prevent="addQuiz">
                        <div class="form-group">
                            <input type="text" name="name" id="quizName" v-model="quiz.name" class="form-control" placeholder="Quiz Name">
                        </div>
                        <div class="form-group">
                            <input type="text" name="name" id="quizDesc" v-model="quiz.desc" class="form-control" placeholder="Quiz Desc">
                        </div>
                        <div class="form-group">
                            <input type="file" name="file" id="quizFile" ref="file" v-on:change="handleQuizFileUpload" class="form-control" placeholder="Quiz File">
                        </div>
                        <button type="submit" class="btn btn-lg btn-primary btn-block">Add quiz</button>
                    </form>
                </div>
                <!--                <b-button class="mt-3" variant="outline-danger" block @click="hideAttachmentModal">Close Me</b-button>-->
            </b-modal>


            <b-modal ref="midterm-modal" hide-footer title="Add Midterm">
                <div class="d-block text-center">
                    <form v-on:submit.prevent="addMidterm">
                        <div class="form-group">
                            <input type="text" name="name" id="midtermName" v-model="midterm.name" class="form-control" placeholder="Midterm Name">
                        </div>
                        <div class="form-group">
                            <input type="text" name="name" id="midtermDesc" v-model="midterm.desc" class="form-control" placeholder="Midterm Desc">
                        </div>
                        <div class="form-group">
                            <input type="file" name="file" id="midtermFile" ref="file" v-on:change="handleMidtermFileUpload" class="form-control" placeholder="Midterm File">
                        </div>
                        <button type="submit" class="btn btn-lg btn-primary btn-block">Add midterm</button>
                    </form>
                </div>
                <!--                <b-button class="mt-3" variant="outline-danger" block @click="hideAttachmentModal">Close Me</b-button>-->
            </b-modal>


            <b-modal ref="endterm-modal" hide-footer title="Add Endterms">
                <div class="d-block text-center">
                    <form v-on:submit.prevent="addEndterm">
                        <div class="form-group">
                            <input type="text" name="name" id="endtermName" v-model="endterm.name" class="form-control" placeholder="Endterm Name">
                        </div>
                        <div class="form-group">
                            <input type="text" name="name" id="endtermDesc" v-model="endterm.desc" class="form-control" placeholder="Endterm Desc">
                        </div>
                        <div class="form-group">
                            <input type="file" name="file" id="endtermFile" ref="file" v-on:change="handleEndtermFileUpload" class="form-control" placeholder="Endterm File">
                        </div>
                        <button type="submit" class="btn btn-lg btn-primary btn-block">Add endterm</button>
                    </form>
                </div>
                <!--                <b-button class="mt-3" variant="outline-danger" block @click="hideAttachmentModal">Close Me</b-button>-->
            </b-modal>


            <b-modal ref="sis-modal" hide-footer title="Add SIS">
                <div class="d-block text-center">
                    <form v-on:submit.prevent="addSIS">
                        <div class="form-group">
                            <input type="text" name="name" id="sisName" v-model="sis.name" class="form-control" placeholder="SIS Name">
                        </div>
                        <div class="form-group">
                            <input type="text" name="name" id="sisDesc" v-model="sis.desc" class="form-control" placeholder="SIS Desc">
                        </div>
                        <div class="form-group">
                            <input type="file" name="file" id="sisFile" ref="file" v-on:change="handleSISFileUpload" class="form-control" placeholder="SIS File">
                        </div>
                        <button type="submit" class="btn btn-lg btn-primary btn-block">Add SIS</button>
                    </form>
                </div>
                <!--                <b-button class="mt-3" variant="outline-danger" block @click="hideAttachmentModal">Close Me</b-button>-->
            </b-modal>


            <b-modal ref="tsis-modal" hide-footer title="Add TSIS">
                <div class="d-block text-center">
                    <form v-on:submit.prevent="addTSIS">
                        <div class="form-group">
                            <input type="text" name="name" id="tsisName" v-model="tsis.name" class="form-control" placeholder="TSIS Name">
                        </div>
                        <div class="form-group">
                            <input type="text" name="name" id="tsisDesc" v-model="tsis.desc" class="form-control" placeholder="TSIS Desc">
                        </div>
                        <div class="form-group">
                            <input type="file" name="file" id="tsisFile" ref="file" v-on:change="handleTSISFileUpload" class="form-control" placeholder="TSIS File">
                        </div>
                        <button type="submit" class="btn btn-lg btn-primary btn-block">Add TSIS</button>
                    </form>
                </div>
                <!--                <b-button class="mt-3" variant="outline-danger" block @click="hideAttachmentModal">Close Me</b-button>-->
            </b-modal>


            <b-modal ref="lecture-modal" hide-footer title="Add Lecture">
                <div class="d-block text-center">
                    <form v-on:submit.prevent="addLecture">
                        <div class="form-group">
                            <input type="text" name="name" id="lectureName" v-model="lecture.name" class="form-control" placeholder="Lecture Name">
                        </div>
                        <div class="form-group">
                            <input type="text" name="name" id="lectureDesc" v-model="lecture.desc" class="form-control" placeholder="Lecture Desc">
                        </div>
                        <div class="form-group">
                            <input type="file" name="file" id="lectureFile" ref="file" v-on:change="handleLectureFileUpload" class="form-control" placeholder="Lecture File">
                        </div>
                        <button type="submit" class="btn btn-lg btn-primary btn-block">Add lecture</button>
                    </form>
                </div>
                <!--                <b-button class="mt-3" variant="outline-danger" block @click="hideAttachmentModal">Close Me</b-button>-->
            </b-modal>


            <b-modal ref="syllabus-modal" hide-footer title="Add Syllabus">
                <div class="d-block text-center">
                    <form v-on:submit.prevent="addSyllabus">
                        <div class="form-group">
                            <input type="text" name="name" id="syllabusName" v-model="syllabus.name" class="form-control" placeholder="Syllabus Name">
                        </div>
                        <div class="form-group">
                            <input type="text" name="name" id="syllabusDesc" v-model="syllabus.desc" class="form-control" placeholder="Syllabus Desc">
                        </div>
                        <div class="form-group">
                            <input type="file" name="file" id="syllabusFile" ref="file" v-on:change="handleSyllabusFileUpload" class="form-control" placeholder="Syllabus File">
                        </div>
                        <button type="submit" class="btn btn-lg btn-primary btn-block">Add syllabus</button>
                    </form>
                </div>
                <!--                <b-button class="mt-3" variant="outline-danger" block @click="hideAttachmentModal">Close Me</b-button>-->
            </b-modal>


            <b-modal ref="final-modal" hide-footer title="Add Final">
                <div class="d-block text-center">
                    <form v-on:submit.prevent="addFinal">
                        <div class="form-group">
                            <input type="text" name="name" id="finalName" v-model="final.name" class="form-control" placeholder="Final Name">
                        </div>
                        <div class="form-group">
                            <input type="text" name="name" id="finalDesc" v-model="final.desc" class="form-control" placeholder="Final Desc">
                        </div>
                        <div class="form-group">
                            <input type="file" name="file" id="file" ref="file" v-on:change="handleFinalFileUpload" class="form-control" placeholder="Final File">
                        </div>
                        <button type="submit" class="btn btn-lg btn-primary btn-block">Add final</button>
                    </form>
                </div>
                <!--                <b-button class="mt-3" variant="outline-danger" block @click="hideAttachmentModal">Close Me</b-button>-->
            </b-modal>
        </div>
    </div>
</template>

<script>
    import NavBar from "../components/Navbar";
    import $http from "../axios-api";

    export default {
        name: 'Discipline',
        data () {
            return {
                discipline: '',
                labwork: {
                    name: '',
                    desc: '',
                    file: []
                },
                quiz: {
                    name: '',
                    desc: '',
                    file: []
                },
                midterm: {
                    name: '',
                    desc: '',
                    file: []
                },
                endterm: {
                    name: '',
                    desc: '',
                    file: []
                },
                lecture: {
                    name: '',
                    desc: '',
                    file: []
                },
                sis: {
                    name: '',
                    desc: '',
                    file: []
                },
                tsis: {
                    name: '',
                    desc: '',
                    file: []
                },
                syllabus: {
                    name: '',
                    desc: '',
                    file: []
                },
                final: {
                    name: '',
                    desc: '',
                    file: []
                },
                tabIndex: 0,
                tabs: ['#labworks', '#quizes', '#midterms', '#endterms', '#lectures', '#sises', '#tsises', '#syllabuses', '#finals']
            }
        },
        components: {
            NavBar,
        },

        methods: {
            async getDiscipline () {
                try {
                    await $http.get(`/disciplines/${this.$route.params.id}/`)
                        .then(response => {
                            this.discipline = response.data
                        })
                    console.log(this.discipline)
                } catch(error) {
                    console.log(error)
                }
            },

            showLabWorkModal () {
                this.$refs['labwork-modal'].show()
            },

            showQuizModal () {
                this.$refs['quiz-modal'].show()
            },

            showLectureModal () {
                this.$refs['lecture-modal'].show()
            },

            showMidtermModal () {
                this.$refs['midterm-modal'].show()
            },

            showEndtermModal () {
                this.$refs['endterm-modal'].show()
            },

            showSISModal () {
                this.$refs['sis-modal'].show()
            },

            showTSISModal () {
                this.$refs['tsis-modal'].show()
            },

            showFinalModal () {
                this.$refs['final-modal'].show()
            },

            showSyllabusModal () {
                this.$refs['syllabus-modal'].show()
            },




            handleLabWorkFileUpload () {
                this.labwork.file = this.$refs.file.files[0];
            },

            addLabWork () {

                let data = new FormData();
                data.append('name', this.labwork.name);
                data.append('file', this.labwork.file);
                data.append('desc', this.labwork.desc)
                for (let key of data.entries()) {
                    console.log(key[0] + ', ' + key[1])
                }

                // let config = {
                //     header : {
                //         'Content-Type' : 'multipart/form-data'
                //     }
                // }

                try {
                    $http.post(`/disciplines/${this.$route.params.id}/labworks/`, data, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                        .then((response) => {
                            console.log(response)
                            location.reload();
                        })
                } catch(error) {
                    console.log(error)
                }
            },



            handleQuizFileUpload () {
                this.quiz.file = this.$refs.file.files[0];
            },

            addQuiz () {

                let data = new FormData();
                data.append('name', this.quiz.name);
                data.append('file', this.quiz.file);
                data.append('desc', this.quiz.desc)
                for (let key of data.entries()) {
                    console.log(key[0] + ', ' + key[1])
                }

                // let config = {
                //     header : {
                //         'Content-Type' : 'multipart/form-data'
                //     }
                // }

                try {
                    $http.post(`/disciplines/${this.$route.params.id}/quizes/`, data, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                        .then((response) => {
                            console.log(response)
                            location.reload();
                        })
                } catch(error) {
                    console.log(error)
                }
            },


            handleMidtermFileUpload () {
                this.midterm.file = this.$refs.file.files[0];
            },

            addMidterm () {

                let data = new FormData();
                data.append('name', this.midterm.name);
                data.append('file', this.midterm.file);
                data.append('desc', this.midterm.desc)
                for (let key of data.entries()) {
                    console.log(key[0] + ', ' + key[1])
                }

                // let config = {
                //     header : {
                //         'Content-Type' : 'multipart/form-data'
                //     }
                // }

                try {
                    $http.post(`/disciplines/${this.$route.params.id}/midterms/`, data, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                        .then((response) => {
                            console.log(response)
                            location.reload();
                        })
                } catch(error) {
                    console.log(error)
                }
            },


            handleEndtermFileUpload () {
                this.endterm.file = this.$refs.file.files[0];
            },

            addEndterm () {

                let data = new FormData();
                data.append('name', this.endterm.name);
                data.append('file', this.endterm.file);
                data.append('desc', this.endterm.desc)
                for (let key of data.entries()) {
                    console.log(key[0] + ', ' + key[1])
                }

                // let config = {
                //     header : {
                //         'Content-Type' : 'multipart/form-data'
                //     }
                // }

                try {
                    $http.post(`/disciplines/${this.$route.params.id}/endterms/`, data, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                        .then((response) => {
                            console.log(response)
                            location.reload();
                        })
                } catch(error) {
                    console.log(error)
                }
            },


            handleSISFileUpload () {
                this.sis.file = this.$refs.file.files[0];
            },

            addSIS () {

                let data = new FormData();
                data.append('name', this.sis.name);
                data.append('file', this.sis.file);
                data.append('desc', this.sis.desc)
                for (let key of data.entries()) {
                    console.log(key[0] + ', ' + key[1])
                }

                // let config = {
                //     header : {
                //         'Content-Type' : 'multipart/form-data'
                //     }
                // }

                try {
                    $http.post(`/disciplines/${this.$route.params.id}/sises/`, data, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                        .then((response) => {
                            console.log(response)
                            location.reload();
                        })
                } catch(error) {
                    console.log(error)
                }
            },


            handleTSISFileUpload () {
                this.tsis.file = this.$refs.file.files[0];
            },

            addTSIS () {

                let data = new FormData();
                data.append('name', this.tsis.name);
                data.append('file', this.tsis.file);
                data.append('desc', this.tsis.desc)
                for (let key of data.entries()) {
                    console.log(key[0] + ', ' + key[1])
                }

                // let config = {
                //     header : {
                //         'Content-Type' : 'multipart/form-data'
                //     }
                // }

                try {
                    $http.post(`/disciplines/${this.$route.params.id}/tsises/`, data, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                        .then((response) => {
                            console.log(response)
                            location.reload();
                        })
                } catch(error) {
                    console.log(error)
                }
            },


            handleSyllabusFileUpload () {
                this.syllabus.file = this.$refs.file.files[0];
            },

            addSyllabus () {

                let data = new FormData();
                data.append('name', this.syllabus.name);
                data.append('file', this.syllabus.file);
                data.append('desc', this.syllabus.desc)
                for (let key of data.entries()) {
                    console.log(key[0] + ', ' + key[1])
                }

                // let config = {
                //     header : {
                //         'Content-Type' : 'multipart/form-data'
                //     }
                // }

                try {
                    $http.post(`/disciplines/${this.$route.params.id}/syllabuses/`, data, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                        .then((response) => {
                            console.log(response)
                            location.reload();
                        })
                } catch(error) {
                    console.log(error)
                }
            },


            handleLectureFileUpload () {
                this.lecture.file = this.$refs.file.files[0];
            },

            addLecture () {

                let data = new FormData();
                data.append('name', this.lecture.name);
                data.append('file', this.lecture.file);
                data.append('desc', this.lecture.desc)
                for (let key of data.entries()) {
                    console.log(key[0] + ', ' + key[1])
                }

                // let config = {
                //     header : {
                //         'Content-Type' : 'multipart/form-data'
                //     }
                // }

                try {
                    $http.post(`/disciplines/${this.$route.params.id}/lectures/`, data, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                        .then((response) => {
                            console.log(response)
                            location.reload();
                        })
                } catch(error) {
                    console.log(error)
                }
            },


            handleFinalFileUpload () {
                this.final.file = this.$refs.file.files[0];
            },

            addFinal () {

                let data = new FormData();
                data.append('name', this.final.name);
                data.append('file', this.final.file);
                data.append('desc', this.final.desc)
                for (let key of data.entries()) {
                    console.log(key[0] + ', ' + key[1])
                }

                // let config = {
                //     header : {
                //         'Content-Type' : 'multipart/form-data'
                //     }
                // }

                try {
                    $http.post(`/disciplines/${this.$route.params.id}/finals/`, data, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                        .then((response) => {
                            console.log(response)
                            location.reload();
                        })
                } catch(error) {
                    console.log(error)
                }
            },

            async deleteLabWork(id) {
                try {
                    await $http.delete(`disciplines/labwork/${id}/`)
                        .then(response => {
                            console.log(response)
                            location.reload()
                        })
                } catch(error) {
                    console.log(error)
                }
            },

            async deleteQuiz(id) {
                try {
                    await $http.delete(`disciplines/quiz/${id}/`)
                        .then(response => {
                            console.log(response)
                            location.reload()
                        })
                } catch(error) {
                    console.log(error)
                }
            },

            async deleteMidterm(id) {
                try {
                    await $http.delete(`disciplines/midterm/${id}/`)
                        .then(response => {
                            console.log(response)
                            location.reload()
                        })
                } catch(error) {
                    console.log(error)
                }
            },

            async deleteEndterm(id) {
                try {
                    await $http.delete(`disciplines/endterm/${id}/`)
                        .then(response => {
                            console.log(response)
                            location.reload()
                        })
                } catch(error) {
                    console.log(error)
                }
            },

            async deleteSIS(id) {
                try {
                    await $http.delete(`disciplines/sis/${id}/`)
                        .then(response => {
                            console.log(response)
                            location.reload()
                        })
                } catch(error) {
                    console.log(error)
                }
            },

            async deleteTSIS(id) {
                try {
                    await $http.delete(`disciplines/tsis/${id}/`)
                        .then(response => {
                            console.log(response)
                            location.reload()
                        })
                } catch(error) {
                    console.log(error)
                }
            },

            async deleteLecture(id) {
                try {
                    await $http.delete(`disciplines/lecture/${id}/`)
                        .then(response => {
                            console.log(response)
                            location.reload()
                        })
                } catch(error) {
                    console.log(error)
                }
            },

            async deleteSyllabus(id) {
                try {
                    await $http.delete(`disciplines/syllabus/${id}/`)
                        .then(response => {
                            console.log(response)
                            location.reload()
                        })
                } catch(error) {
                    console.log(error)
                }
            },

            async deleteFinal(id) {
                try {
                    await $http.delete(`disciplines/final/${id}/`)
                        .then(response => {
                            console.log(response)
                            location.reload()
                        })
                } catch(error) {
                    console.log(error)
                }
            },




        },

        mounted() {
            this.getDiscipline()
        }
    }
</script>

<style>

</style>
