import { createRouter, createWebHistory } from "vue-router";
import Accueil from "/src/views/Accueil.vue"
import DetailItem from "/src/views/DetailItem.vue"
import Inscription from "/src/views/Inscription.vue"
import Panier from "/src/views/Panier.vue"

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
        },
        {
            name: 'panier',
            path: '/panier',
            component: Panier
        }
    ]
})

export default router;