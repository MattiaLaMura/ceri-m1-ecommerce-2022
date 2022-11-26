<script>
export default {
}
</script>

<template>
    
  <h2 class="text-center text-white">Inscription</h2>
  <form >
      <div class="form-group p-2 text-white">
          <label for="exampleInputEmail1">Nom d'utilisateur</label>
          <input type="username" class="form-control" id="InputUsername" placeholder="Entrez votre nom d'utilisateur">
      </div>
      <div class="form-group p-2 text-white">
          <label for="exampleInputPassword1">Mot de passe</label>
          <input type="password" class="form-control" id="InputPassword" placeholder="Entrez votre mot de passe">
      </div>
      <div class="form-group p-2 text-white">
          <label for="exampleInputPassword1">Confirmation mot de passe</label>
          <input type="password" class="form-control" id="InputPassword" placeholder="Confirmation mot de passe">
      </div>
      <div class="p-4 d-flex justify-content-center">
          <!-- <button type="submit" class="btn btn-primary buttonInscription text-center ">Créé mon compte</button> -->
          <router-link type="submit" to="/" class="btn btn-primary buttonInscription text-white" aria-current="page">Créé mon compte</router-link>
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