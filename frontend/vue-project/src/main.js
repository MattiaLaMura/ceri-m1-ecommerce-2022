import { createApp } from 'vue'
import App from './App.vue'
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css';
import 'bootstrap'; import 'bootstrap/dist/css/bootstrap.min.css';
// import dotenv from 'dotenv'

// dotenv.config()
const app = createApp(App)

import router from '/src/router';
app.use(router)

app.component('v-select', vSelect)
app.mount('#app')
// console.log("HOIZOHIODHFZIOHO" + process.env.BACKEND_URL)