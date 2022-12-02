<script>
import ConnexionModal from './ConnexionModal.vue'

export default{
    data() {
        return {
            showModal: false,
            user_name : ''
        }
    },
    created(){
        if(localStorage.getItem('user_name') != null){
            this.user_name = localStorage.getItem('user_name')
        } else this.user_name = '';
    },
    methods:{
        scrollToTop() {
            window.scrollTo(0,0);
        },
        test(){
            console.log(this.showModal)
            
        },
        updateHeader(){
            if(localStorage.getItem('user_name') != null){
                this.user_name = localStorage.getItem('user_name')
            } else this.user_name = '';
        },
        disconnect(){
            localStorage.clear();
        }
    },
    components: { ConnexionModal },
    
}
</script>

<template>
    <h4 v-if="user_name != ''" class="text-white text-center"> Bonjour {{user_name}}</h4>
    <ConnexionModal v-show="showModal" @close-modal="showModal = false" @updateHeader="updateHeader()" />
    <div class="container bg-dark rounded-3">
        <header class="d-flex justify-content-center py-3">
        <ul class="nav nav-pills">

            <router-link v-on:click="scrollToTop()" to="/" class="nav-link text-white" aria-current="page" >Accueil</router-link>
            
            <li class="nav-item"><a href="#" class="nav-link text-white">FAQs</a></li>
            <li class="nav-item"><a href="#" class="nav-link text-white">A propos</a></li>
            <div  v-if="user_name == ''">
                <a href="#" class="nav-link text-white" v-on:click="showModal = true" >Connexion</a>
            </div>
            <div v-else>
                <a v-on:click="(disconnect(), updateHeader())" href="#" class="nav-link text-white">Déconnexion</a>
            </div>
            <router-link to="/panier" class="nav-link text-white" aria-current="page" >Panier</router-link>

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