<script>
import axios from 'axios'

export default {
  data() {
    return {
      name: "",
      password:"",
      backendUrl :"https://purplepig-backend-mwjszocsqa-ew.a.run.app"
    }
  },
  methods:{
        async connexion(submitEvent){
          // Récupère info formulaire
          this.name = submitEvent.target.elements.name.value;
          this.password = submitEvent.target.elements.password.value;

          this.name.replace('@', '%40')

          const url ="https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/token_backoffice"
          const headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
          };
        
          const param = 'grant_type=&username=' + this.name + '&password=' + this.password+ '&scope=&client_id=&client_secret=';
          const response = await axios.post(url ,param, {headers})
          
          if(response.data != null){
            const token = response.data.access_token
          
            console.log(token)

            // Recupere donnees de l'utilisateur
            const urlCurrentAdmin = "https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/current/admin"

            const responseCurrentAdmin = await axios.get(urlCurrentAdmin, {
              headers: {
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + token
              }});
            if(responseCurrentAdmin.data != null){
              localStorage.clear();
              localStorage.setItem('admin_name', responseCurrentAdmin.data.current_admin.admin_name)
              localStorage.setItem('admin_id', responseCurrentAdmin.data.current_admin.admin_id)
              localStorage.setItem('admin_token', response.data.access_token)
              // Connexion réussie
              this.$emit('updateHeader')
            }
            console.log(responseCurrentAdmin.data.current_admin.admin_name)
            this.$router.push('/backoffice/listeAlbum')
          } else console.log("error connexion")
        }
    }
}
</script>

<template>

    <h2 class="text-center text-white">Connexion Back office</h2>
    <form @submit.prevent="connexion">
      <div class="form-group p-2 text-white">
          <label for="InputEmail">Nom</label>
          <input  class="form-control" id="InputName" name="name" placeholder="Entrez votre nom d'utilisateur">
      </div>
      <div class="form-group p-2 text-white">
          <label for="InputPassword">Mot de passe</label>
          <input type="password" class="form-control" id="InputPassword" name="password" placeholder="Entrez votre mot de passe">
      </div>

      <div class="p-4 d-flex justify-content-center">
          <button type="submit" class="btn buttonConnexion text-center ">Connexion</button>
      </div>
    </form>
    
</template>
  


<style scoped>

.modal-overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  background-color: #000000da;
  z-index:200;
}

.modals {
  z-index:201;
  text-align: center;
  background-color: rgb(255, 255, 255);
  height: 500px; 
  width: 500px;
  margin-top: 10%;
  padding: 60px 0; 
  border-radius: 20px;
}
.closes {
  cursor: pointer;
}

h6 {
  font-weight: 500;
  font-size: 28px;
  margin: 20px 0;
}

p {
  font-size: 16px;
  margin: 20px 0;
}

.buttonConnexion {
  background-color: #dc6e00;
  width: 150px;
  height: 40px;
  color: white;
  font-size: 14px;
  border-radius: 16px;
  margin-top: 50px;
}

.buttonInscription {
  background-color: #000000;
  width: 150px;
  height: 40px;
  color: white;
  font-size: 14px;
  border-radius: 16px;
}
</style>