import { createRouter, createWebHistory } from "vue-router";
import Accueil from "@/views/Accueil.vue"
import DetailItem from "@/views/DetailItem.vue"

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
            path: '/item/:nomAlbum',
            component: DetailItem,
            props: true
        },
        {
           
            path: '/item',
            component: DetailItem

        }
    ]
})

export default router;