<script>
export default {
}
</script>

<template>
    
  <h2>Inscription</h2>
  <form>
      <div class="form-group p-2">
          <label for="exampleInputEmail1">Nom d'utilisateur</label>
          <input type="username" class="form-control" id="InputUsername" placeholder="Entrez votre nom d'utilisateur">
      </div>
      <div class="form-group p-2">
          <label for="exampleInputPassword1">Mot de passe</label>
          <input type="password" class="form-control" id="InputPassword" placeholder="Entrez votre mot de passe">
      </div>
      <div class="form-group p-2">
          <label for="exampleInputPassword1">Mot de passe</label>
          <input type="password" class="form-control" id="InputPassword" placeholder="Entrez votre mot de passe">
      </div>
      <div class="p-2">
          <p>Pas encore de compte?</p>
          <button type="submit" class="btn btn-primary buttonInscription">S'inscrire</button>
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
  background-color: #000000;
  width: 150px;
  height: 40px;
  color: white;
  font-size: 14px;
  border-radius: 16px;
}
</style>