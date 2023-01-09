<script>
import axios from 'axios'
export default {
  data() {
    return {
      listeUtilisateurs:[],
      backendUrl :"https://purplepig-backend-mwjszocsqa-ew.a.run.app"
    }
  },
  async created() {
    // Récupère liste des utilisateurs
    const tokenAdmin = localStorage.getItem('admin_token')
    const response = await axios.get("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/users", {
            headers: {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + tokenAdmin
            }});

    for(let i = 0 ; i < response.data.users.length; i++){
      this.listeUtilisateurs.push({idUtilisateur:response.data.users[i].user_id, nomUtilisateur:response.data.users[i].user_name});
    }
  },
  
}


</script>

<template>
    
  <h2 class="text-center text-white">Liste des utilisateurs</h2>
  <div class="p-2" v-for="utilisateur in listeUtilisateurs">
    <router-link :to="{name : 'commandesUtilisateur', params: {idUtilisateur: utilisateur.idUtilisateur} }">
      <div class="rounded-2 bg-dark text-white text-center">
        <div class="p-2">
          {{utilisateur.idUtilisateur}} {{utilisateur.nomUtilisateur}}
        </div>
      </div>
    </router-link>
  </div>
 
</template>
  


<style scoped>

a { 
    text-decoration: none; 
}

</style>