import { createApp } from 'vue'
import App from './App.vue'

//import './assets/main.css'
import 'bootstrap'; import 'bootstrap/dist/css/bootstrap.min.css';


const app = createApp(App)

import router from '/src/router';
app.use(router)

app.mount('#app')