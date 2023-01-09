<script>
import ConnexionModal from '../ConnexionModal.vue'

export default{
    data() {
        return {
            showModal: false,
            admin_name : '',
            clicked : false,
            clickedPanier : false,
            clickedCommandes : false,
            clickedAccueil : false,
        }
    },
    created(){
        if(localStorage.getItem('admin_name') != null){
            this.admin_name = localStorage.getItem('admin_name')
        } else this.admin_name = '';
    },
    methods:{
        scrollToTop() {
            window.scrollTo(0,0);
        },
        updateHeader(){
            if(localStorage.getItem('admin_name') != null){
                this.admin_name = localStorage.getItem('admin_name')
            } else this.admin_name = '';
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
    <ConnexionModal v-show="showModal" @close-modal="showModal = false" @updateHeader="updateHeader()" />
    <div class="container bg-dark rounded-3">
        <header class="d-flex justify-content-center py-3">
        <ul class="nav nav-pills">

            <router-link v-on:click="scrollToTop(), changeTxtColor('accueil')" to="/backoffice/listeAlbum" class="nav-link text-white px-5 fw-bold" v-bind:class="{ 'selected': clickedAccueil, 'text-white': !clickedAccueil }" aria-current="page" >Liste Albums</router-link>
        
            <div  v-if="admin_name == ''">
                <router-link  to="/backoffice" class="nav-link text-white px-5 fw-bold">Connexion</router-link>
            </div>
            <div v-if="admin_name != ''">
                <router-link v-on:click="(disconnect(), updateHeader())" to="/backoffice" class="nav-link text-white px-5 fw-bold">Déconnexion</router-link>
            </div>
            
            <router-link v-if="admin_name != ''" to="/backoffice/commandes/listeUtilisateurs" class="nav-link text-white px-5 fw-bold" v-bind:class="{ 'selected': clickedCommandes, 'text-white': !clickedCommandes }" v-on:click="changeTxtColor('commandes')" aria-current="page" >Liste Commandes</router-link>
            <router-link to="/" class="nav-link text-white px-5 fw-bold" v-bind:class="{ 'selected': clickedCommandes, 'text-white': !clickedCommandes }" v-on:click="changeTxtColor('commandes')" aria-current="page" >Retour</router-link>

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