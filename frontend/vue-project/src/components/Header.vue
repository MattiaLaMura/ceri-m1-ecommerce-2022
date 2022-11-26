<script>
import ConnexionModal from './ConnexionModal.vue'

export default{
    methods:{
        scrollToTop() {
            window.scrollTo(0,0);
        },
        test(){
            console.log(this.showModal)
        }
    },
    components: { ConnexionModal },
    data() {
        return {
        showModal: false,
        }
    },
}
</script>

<template>
    
    <ConnexionModal v-show="showModal" @close-modal="showModal = false" />
    <div class="container bg-dark rounded-3">
        
        <header class="d-flex justify-content-center py-3">
        <ul class="nav nav-pills">

            <router-link v-on:click="scrollToTop()" to="/" class="nav-link text-white" aria-current="page" >Accueil</router-link>
            
            <li class="nav-item"><a href="#" class="nav-link text-white">FAQs</a></li>
            <li class="nav-item"><a href="#" class="nav-link text-white">A propos</a></li>
            <a href="#" class="nav-link text-white" v-on:click="showModal = true" >Connexion</a>
        </ul>
        </header>
    </div>
    
</template>

<style scoped>
.container{
    position: sticky;
    top: 0px;
    z-index:100;
}
</style>