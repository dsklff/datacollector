<template>
    <div>
    <NavBar></NavBar>
    <div>
        <b-card no-body>
            <b-tabs v-model="tabIndex" card>
                <b-tab title="Journals" href="#journals">
                    <div>
                        <b-button id="show-btn" @click="showJournalModal">Add Journal</b-button>
                        <table>
                            <thead>
                            <tr>
                                <th>ID</th>
                                <th>Name</th>
                                <th>Issue</th>
                                <th>Date of issue</th>
                                <th>ISSN</th>
                                <th>Delete</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr v-for="journal in publication.journals" :key="journal.id">
                                <td><strong>{{journal.id}}</strong></td>
                                <td>{{journal.name}}</td>
                                <td>{{journal.issue}}</td>
                                <td>{{journal.date_of_issue}}</td>
                                <td>{{journal.issn}}</td>
                                <td><button @click="deleteJournal(journal.id)">Delete</button></td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                </b-tab>
                <b-tab title="Attachments" href="#attachments">
                    <div>
                        <b-button id="show-btn" @click="showAttachmentModal">Add Attachment</b-button>
                        <table>
                            <thead>
                            <tr>
                                <th>ID</th>
                                <th>Name</th>
                                <th>Link</th>
                                <th>Delete</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr v-for="attachment in publication.attachments" :key="attachment.id">
                                <td><strong>{{attachment.id}}</strong></td>
                                <td>{{attachment.name}}</td>
                                <td><a v-bind:href="attachment.file_url">Download</a></td>
                                <td><button @click="deleteAttachment(attachment.id)">Delete</button></td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                </b-tab>
            </b-tabs>
        </b-card>
    </div>
        <div>
            <b-modal ref="journal-modal" hide-footer title="Add journal">
                <div class="d-block text-center">
                    <form v-on:submit.prevent="addJournal">
                        <div class="form-group">
                            <input type="text" name="name" id="name" v-model="journal.name" class="form-control" placeholder="Journal Name">
                        </div>
                        <div class="form-group">
                            <input type="text" name="issue" id="issue" v-model="journal.issue" class="form-control" placeholder="Journal Issue">
                        </div>
                        <div class="form-group">
                            <input type="text" name="date_of_issue" id="date_of_issue" v-model="journal.date_of_issue" class="form-control" placeholder="Date of Issue">
                        </div>
                        <div class="form-group">
                            <input type="text" name="issn" id="issn" v-model="journal.issn" class="form-control" placeholder="Journal ISSN">
                        </div>
                        <button type="submit" class="btn btn-lg btn-primary btn-block">Add journal</button>
                    </form>
                </div>
<!--                <b-button class="mt-3" variant="outline-danger" block @click="hideJournalModal">Close Me</b-button>-->
            </b-modal>

            <b-modal ref="attachment-modal" hide-footer title="Add attachment">
                <div class="d-block text-center">
                    <form v-on:submit.prevent="addAttachment">
                        <div class="form-group">
                            <input type="text" name="name" id="attachmentName" v-model="attachment.name" class="form-control" placeholder="Journal Name">
                        </div>
                        <div class="form-group">
                            <input type="file" name="file" id="file" ref="file" v-on:change="handleFileUpload" class="form-control" placeholder="Journal Issue">
                        </div>
                        <button type="submit" class="btn btn-lg btn-primary btn-block">Add attachment</button>
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
        name: 'Publication',
        data () {
            return {
                publication: '',
                journal: {
                    name: '',
                    issue: '',
                    date_of_issue: '',
                    issn: ''
                },
                attachment: {
                    name: '',
                    file: []
                },
                tabIndex: 0,
                tabs: ['#journals', '#attachments']
            }
        },
        components: {
            NavBar,
        },

        methods: {
            async getPublication () {
                try {
                    await $http.get(`/publications/${this.$route.params.id}/`)
                        .then(response => {
                            this.publication = response.data
                        })
                    console.log(this.publication)
                } catch(error) {
                    console.log(error)
                }
            },

            showAttachmentModal () {
                this.$refs['attachment-modal'].show()
            },

            hideAttachmentModal () {
                this.$refs['my-modal'].hide()
            },

            showJournalModal () {
                this.$refs['journal-modal'].show()
            },

            hideJournalModal () {
                this.$refs['my-modal'].hide()
            },

            async addJournal () {
                try {
                    await $http.post(`/publications/${this.$route.params.id}/journals/`, {
                        name: this.journal.name,
                        issue: this.journal.issue,
                        date_of_issue: this.journal.date_of_issue,
                        issn: this.journal.issn
                    })
                        .then(() => {
                            location.reload();
                        })
                } catch(error) {
                    console.log(error)
                }
            },

            handleFileUpload () {
                this.attachment.file = this.$refs.file.files[0];
            },

            addAttachment () {

                let data = new FormData();
                data.append('name', this.attachment.name);
                data.append('file', this.attachment.file);
                for (let key of data.entries()) {
                    console.log(key[0] + ', ' + key[1])
                }

                // let config = {
                //     header : {
                //         'Content-Type' : 'multipart/form-data'
                //     }
                // }

                try {
                    $http.post(`/publications/${this.$route.params.id}/attachments/`, data, {
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

            async deleteAttachment(id) {
                try {
                    await $http.delete(`publications/attachment/${id}/`)
                        .then(response => {
                            console.log(response)
                            location.reload()
                        })
                } catch(error) {
                    console.log(error)
                }
            },

            async deleteJournal(id) {
                try {
                    await $http.delete(`publications/journal/${id}/`)
                        .then(response => {
                            console.log(response)
                            location.reload()
                        })
                } catch(error) {
                    console.log(error)
                }
            }
        },

        mounted() {
            this.getPublication()
        }
    }
</script>

<style>

</style>
