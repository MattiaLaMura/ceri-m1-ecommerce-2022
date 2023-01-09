<script>
import axios from 'axios'
import {useToast} from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';
export default {
  data() {
    return {
      username: "",
      email: "",
      password:"",
      backendUrl :"https://purplepig-backend-mwjszocsqa-ew.a.run.app"
    }
  },
  methods:{
        async inscription(submitEvent){

          this.username = submitEvent.target.elements.username.value;
          this.email = submitEvent.target.elements.email.value;
          this.password = submitEvent.target.elements.password.value;

          const url = "https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/signup?"
          const param = 'user_name=' + this.username + '&user_email=' + this.email + '&user_password=' + this.password;
          const response = await axios.post(url+param).catch(function(error){
            console.log("error inscription")
            useToast().error('Inscription échouée.', {
              position: 'top',
              dismissible:'true',
              duration:'5000'
            });
          })

          useToast().success('Inscription réussie', {
              position: 'top',
              dismissible:'true',
              duration:'5000'
          });
          console.log(response.data)
          if(response.data != null){
            this.$router.push('/');
          } else console.log("Erreur inscription");
        }
    }
}


</script>

<template>
    
  <h2 class="text-center text-white">Inscription</h2>
  <form @submit.prevent="inscription">
      <div class="form-group p-2 text-white">
          <label for="InputUsername">Nom d'utilisateur</label>
          <input type="username" class="form-control" id="InputUsername" name="username" placeholder="Entrez votre nom d'utilisateur">
      </div>
      <div class="form-group p-2 text-white">
          <label for="InputEmail">Email</label>
          <input type="email" class="form-control" id="InputEmail" name="email" placeholder="Entrez votre Email">
      </div>
      <div class="form-group p-2 text-white">
          <label for="InputPassword">Mot de passe</label>
          <input type="password" class="form-control" id="InputPassword" name="password" placeholder="Entrez votre mot de passe">
      </div>
      <div class="form-group p-2 text-white">
          <label for="InputPassword1">Confirmation mot de passe</label>
          <input type="password" class="form-control" id="InputPassword" placeholder="Confirmation mot de passe">
      </div>
      <div class="p-4 d-flex justify-content-center">
          <button type="submit" class="btn buttonInscription text-center ">Créé mon compte</button>
      </div>
  </form>
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
</style>