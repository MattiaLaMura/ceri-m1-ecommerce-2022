<script>
export default {
}
</script>

<template>
    <div class="modal-overlay" @click="$emit('close-modal')">
      <div class="modals" @click.stop>
        <h2>Connexion</h2>
        <form>
            <div class="form-group p-2">
                <label for="exampleInputEmail1">Nom d'utilisateur</label>
                <input type="username" class="form-control" id="InputUsername" placeholder="Entrez votre nom d'utilisateur">
            </div>
            <div class="form-group p-2">
                <label for="exampleInputPassword1">Mot de passe</label>
                <input type="password" class="form-control" id="InputPassword" placeholder="Entrez votre mot de passe">
            </div>
            <button type="submit" class="btn btn-primary p-2 buttonConnection">Se connecter</button>
            <div class="p-2">
                <p>Pas encore de compte?</p>
                <button type="submit" class="btn btn-primary buttonInscription">S'inscrire</button>
                <router-link to="/inscription" class="nav-link text-white" aria-current="page" >Accueil</router-link>
            
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