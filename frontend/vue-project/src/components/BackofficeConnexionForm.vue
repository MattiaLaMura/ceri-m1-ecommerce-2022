<script>
import axios from 'axios'

export default {
  data() {
    return {
      email: "",
      password:""
    }
  },
  methods:{

        async connexion(submitEvent){

          this.email = submitEvent.target.elements.email.value;
          this.password = submitEvent.target.elements.password.value;

          this.email.replace('@', '%40')

          const url = 'http://localhost:8000/token'
          const headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
          };
        
          const param = 'grant_type=&username=' + this.email.replace('@', '%40') + '&password=' + this.password+ '&scope=&client_id=&client_secret=';
          const response = await axios.post(url ,param, {headers})
          
          if(response.data != null){
            const token = response.data.access_token
          
            console.log(token)

            // Recupere donnees de l'utilisateur
            const urlCurrentUser = "http://localhost:8000/get/current/user"
            const headersCurrentUser = { 
              'Accept': 'application/json',
              'Authorization': 'Bearer ' + token
            };
            const responseCurrentUser = await axios.get(urlCurrentUser, {
              headers: {
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + token
              }});
            if(responseCurrentUser.data != null){
              localStorage.setItem('user_name', responseCurrentUser.data.current_user.user_name)
              localStorage.setItem('user_email', responseCurrentUser.data.current_user.user_email)
              localStorage.setItem('user_id', responseCurrentUser.data.current_user.user_id)
              localStorage.setItem('user_token', response.data.access_token)
              // Connexion réussie, ferme le formulaire
              this.$emit('close-modal')
              this.$emit('updateHeader')
            }
            console.log(responseCurrentUser.data.current_user.user_name)
          } else console.log("error connexion")
        }
    }
}
</script>

<template>
    
      
    <h2 class="text-center text-white">Connexion Back office</h2>
    <form @submit.prevent="connexion">
      <div class="form-group p-2 text-white">
          <label for="InputEmail">Email</label>
          <input type="email" class="form-control" id="InputEmail" name="email" placeholder="Entrez votre Email">
      </div>
      <div class="form-group p-2 text-white">
          <label for="InputPassword">Mot de passe</label>
          <input type="password" class="form-control" id="InputPassword" name="password" placeholder="Entrez votre mot de passe">
      </div>

      <div class="p-4 d-flex justify-content-center">
          <button type="submit" class="btn buttonConnexion text-center ">Connexion</button>
          <!-- <router-link  type="submit" to="/" class="btn btn-primary buttonInscription text-white" aria-current="page">Créé mon compte</router-link> -->
          <!-- <router-link type="submit" to="/" class="btn btn-primary buttonInscription text-white" aria-current="page">Créé mon compte</router-link> -->
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
  /* margin: 10% 0 0 px; */
  cursor: pointer;
}
/* 
.close-img {
  width: 25px;
}

.check {
  width: 150px;
} */

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