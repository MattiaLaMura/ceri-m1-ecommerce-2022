<script>
import axios from 'axios'
export default {
  data() {
    return {
      username: "",
      email: "",
      password:""
    }
  },
  methods:{


        async inscription(submitEvent){

          this.username = submitEvent.target.elements.username.value;
          this.email = submitEvent.target.elements.email.value;
          this.password = submitEvent.target.elements.password.value;
        
          const headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          };
          const param = 'user_name=' + this.username + '&user_email=' + this.email + '&user_password=' + this.password;
          const response = await axios.post("http://localhost:8000/signup?"+param);
          console.log(response.data)
          this.$router.push('/')
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
          <button type="submit" class="btn btn-primary buttonInscription text-center ">Créé mon compte</button>
          <!-- <router-link  type="submit" to="/" class="btn btn-primary buttonInscription text-white" aria-current="page">Créé mon compte</router-link> -->
          <!-- <router-link type="submit" to="/" class="btn btn-primary buttonInscription text-white" aria-current="page">Créé mon compte</router-link> -->
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