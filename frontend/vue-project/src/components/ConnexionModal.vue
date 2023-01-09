<script>
import axios from 'axios'
import {useToast} from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';
export default {
  data() {
    return {
      email: "",
      password:"",
      backendUrl :"https://purplepig-backend-mwjszocsqa-ew.a.run.app"
    }
  },
  methods:{
        async connexion(submitEvent){

          this.email = submitEvent.target.elements.email.value;
          this.password = submitEvent.target.elements.password.value;

          this.email.replace('@', '%40')

          const url = "https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/token"
          const headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
          };
        
          const param = 'grant_type=&username=' + this.email.replace('@', '%40') + '&password=' + this.password+ '&scope=&client_id=&client_secret=';
          const response = await axios.post(url ,param, {headers}).catch(function (error) {
            console.log("error connexion")
            useToast().error('Connection échouée.', {
              position: 'top',
              dismissible:'true',
              duration:'5000'
            });
          })
          
          if(response.data != null){
            const token = response.data.access_token
          
            console.log(token)

            // Recupere donnees de l'utilisateur
            const urlCurrentUser = "https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/current/user"

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
            
            useToast().success('Connection réussie. Bonjour '+ responseCurrentUser.data.current_user.user_name, {
              position: 'top',
              dismissible:'true',
              duration:'5000'
            });
          }
        }
    }
}
</script>

<template>
    <div class="modal-overlay" @click="$emit('close-modal')">
      <div class="modals" @click.stop>
        <h2>Connexion</h2>
        <form @submit.prevent="connexion">
            <div class="form-group p-2">
                <label for="exampleInputEmail1">Adresse email</label>
                <input type="username" class="form-control" id="InputUsername" name="email" placeholder="Entrez votre adresse email">
            </div>
            <div class="form-group p-2">
                <label for="exampleInputPassword1">Mot de passe</label>
                <input type="password" class="form-control" id="InputPassword" name="password" placeholder="Entrez votre mot de passe">
            </div>
            <button type="submit" class="btn p-2 buttonConnection">Se connecter</button>
            <div class="p-2">
                <p>Pas encore de compte?</p>
                <router-link  to="/inscription" class="btn buttonInscription text-white" aria-current="page"  @click="$emit('close-modal')">S'inscrire</router-link>
            </div>
        </form>
      </div>
      <div class="closes" @click="$emit('close-modal')">
        <i class="fa-solid fa-xmark"></i>
      </div>
    </div>
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
  background-color: #000000;
  width: 150px;
  height: 40px;
  color: white;
  font-size: 14px;
  border-radius: 16px;
}
</style>