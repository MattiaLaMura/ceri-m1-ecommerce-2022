import { createRouter, createWebHistory } from "vue-router";
import Accueil from "/src/views/Accueil.vue"
import DetailItem from "/src/views/DetailItem.vue"
import Inscription from "/src/views/Inscription.vue"

const router = createRouter({
    history: createWebHistory(),
    routes :[
        {
            name: 'accueil',
            path: '/',
            component: Accueil
        },
        {
            name: 'detailItem',
            path: '/item/:idAlbum',
            component: DetailItem,
            props: true
        },
        {
            name: 'inscription',
            path: '/inscription',
            component: Inscription
        }
    ]
})

export default router;