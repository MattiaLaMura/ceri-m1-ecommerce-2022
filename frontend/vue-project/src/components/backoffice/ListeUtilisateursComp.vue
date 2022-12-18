<script>
import axios from 'axios'
export default {
  data() {
    return {
      listeUtilisateurs:[],
    }
  },
  async created() {
    const tokenAdmin = localStorage.getItem('admin_token')
    const response = await axios.get("http://host.docker.internal:8000/get/users", {
            headers: {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + tokenAdmin
            }});
    
    

    for(let i = 0 ; i < response.data.users.length; i++){
      // console.log("user ",utilisateur)
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

h6 {
  font-weight: 500;
  font-size: 28px;
  margin: 20px 0;
}

p {
  font-size: 16px;
  margin: 20px 0;
}
a { 
    text-decoration: none; 
}
.buttonConnection {
  background-color: #dc6e00;
  width: 150px;
  height: 40px;
  color: white;
  font-size: 14px;
  border-radius: 16px;
  margin-top: 50px;
}

.buttonInscription {
  background-color: #dc6e00;
  width: 150px;
  height: 40px;
  color: white;
  font-size: 14px;
  border-radius: 16px;
}

.buttonPlus {
  background-color: #dc6e00;
  width: 40px;
  height: 40px;
  color: white;
  font-size: 14px;
  border-radius: 16px;
}
.buttonMoins {
  background-color: #bfbdb6;
  width: 40px;
  height: 40px;
  color: white;
  font-size: 14px;
  border-radius: 16px;
}
</style>