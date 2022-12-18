<script>
import ConnexionModal from '../ConnexionModal.vue'

export default{
    data() {
        return {
            showModal: false,
            user_name : '',
            clicked : false,
            clickedPanier : false,
            clickedCommandes : false,
            clickedAccueil : false,
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
        },
        changeTxtColor(element) {
            if(element == "panier"){
                this.clickedPanier = true;
                console.log("panier")
            } else if (element == "commandes"){
                this.clickedCommandes = true;
            } else if (element == "accueil"){
                this.clickedAccueil = true;
            }
            
        }
    },
    components: { ConnexionModal },
    
}
</script>

<template>
    <!-- <h4 v-if="user_name != ''" class="text-white text-center"> Bonjour {{user_name}}</h4> -->
    <ConnexionModal v-show="showModal" @close-modal="showModal = false" @updateHeader="updateHeader()" />
    <div class="container bg-dark rounded-3">
        <header class="d-flex justify-content-center py-3">
        <ul class="nav nav-pills">

            <router-link v-on:click="scrollToTop(), changeTxtColor('accueil')" to="/backoffice/listeAlbum" class="nav-link text-white" v-bind:class="{ 'selected': clickedAccueil, 'text-white': !clickedAccueil }" aria-current="page" >Liste Albums</router-link>
        
            <div  v-if="user_name == ''">
                <a href="#" class="nav-link text-white" v-on:click="showModal = true" >Connexion</a>
            </div>
            <div v-if="user_name != ''">
                <a v-on:click="(disconnect(), updateHeader())" href="#" class="nav-link text-white">Déconnexion</a>
            </div>
            <!-- <router-link v-if="user_name != ''" to="/panier" class="nav-link text-white" v-bind:class="{ 'selected': clickedPanier, 'text-white': !clickedPanier }" v-on:click="changeTxtColor('panier')"  aria-current="page" >Panier</router-link> -->
            <router-link v-if="user_name != ''" to="/backoffice/commandes" class="nav-link text-white" v-bind:class="{ 'selected': clickedCommandes, 'text-white': !clickedCommandes }" v-on:click="changeTxtColor('commandes')" aria-current="page" >Liste Commandes</router-link>
            

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

.selected {
  background-color: #dc6e00;
}
</style>