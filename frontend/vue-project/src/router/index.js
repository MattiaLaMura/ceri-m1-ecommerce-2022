import { createRouter, createWebHistory } from "vue-router";
import Accueil from "/src/views/Accueil.vue"
import DetailItem from "/src/views/DetailItem.vue"

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
        }
    ]
})

export default router;