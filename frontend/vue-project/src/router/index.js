import { createRouter, createWebHistory } from "vue-router";
import Accueil from "/src/views/Accueil.vue"
import DetailItem from "/src/views/DetailItem.vue"
import Inscription from "/src/views/Inscription.vue"
import Panier from "/src/views/Panier.vue"
import Commandes from "/src/views/Commandes.vue"
import BackofficeConnexion from "/src/views/BackofficeConnexion.vue"

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
        },
        {
            name: 'commandes',
            path: '/commandes',
            component: Commandes
        },
        {
            name: 'backoffice',
            path: '/backoffice',
            component: BackofficeConnexion
        }
    ]
})

export default router;