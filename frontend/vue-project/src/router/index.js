import { createRouter, createWebHistory } from "vue-router";
import Accueil from "/src/views/Accueil.vue"
import DetailItem from "/src/views/DetailItem.vue"
import Inscription from "/src/views/Inscription.vue"
import Panier from "/src/views/Panier.vue"
import Commandes from "/src/views/Commandes.vue"
import BackofficeConnexion from "/src/views/backoffice/BackofficeConnexion.vue"
import Backoffice from "/src/views/backoffice/Backoffice.vue"
import AjoutAlbum from "/src/views/backoffice/AjoutAlbum.vue"
import ListeUtilisateurs from "/src/views/backoffice/ListeUtilisateurs.vue"
import CommandesUtilisateur from "/src/views/backoffice/CommandesUtilisateur.vue"


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
        },
        {
            name: 'backofficeListeAlbum',
            path: '/backoffice/listeAlbum',
            component: Backoffice
        },
        {
            name: 'ajoutAlbum',
            path: '/backoffice/ajoutAlbum',
            component: AjoutAlbum
        },
        {
            name: 'listeUtilisateurs',
            path: '/backoffice/commandes/listeUtilisateurs',
            component: ListeUtilisateurs
        },
        {
            name: 'commandesUtilisateur',
            path: '/backoffice/commandes/:idUtilisateur',
            component: CommandesUtilisateur,
            props:true
        },
    ]
})

export default router;