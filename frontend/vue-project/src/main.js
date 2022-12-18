import { createApp } from 'vue'
import App from './App.vue'

import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css';
//import './assets/main.css'
import 'bootstrap'; import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios'


const app = createApp(App)

import router from '/src/router';
app.use(router)

app.component('v-select', vSelect)
app.mount('#app')
// app.use(axios)