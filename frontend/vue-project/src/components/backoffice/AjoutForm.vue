<script>
import axios from 'axios'
import {useToast} from 'vue-toast-notification';
export default {
  data() {
    return {
      nbMusiques : 0,
      listeMusiqueForm:[],
      musiqueKey:0,
      nomArtiste: "",
      titreAlbum: "",
      anneeAlbum:"",
      coverAlbum: "",
      listeMusique: "",
      idArtist: "",
      backendUrl :"https://purplepig-backend-mwjszocsqa-ew.a.run.app"
    }
  },
  methods:{

    async ajoutArtiste(){
      // Verifie si l'artise n'existe pas déja
      const responseArtist = await fetch("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/artists");
      const dataArtist = await responseArtist.json();
      this.idArtist = "";
      for(const artist of dataArtist.artists){
        if(artist.artist_name == this.nomArtiste){
          this.idArtist = artist.artist_id;
        }
      }
      if(this.idArtist == ""){
        // Ajout du nouvel artiste
        const tokenAdmin = localStorage.getItem('admin_token')
        const param = 'artist_name=' + this.nomArtiste + '&is_active=' + "true";
        const response = await axios.get("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/add/artist?"+param, {
                headers: {
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + tokenAdmin
                }});
        console.log(response.data);
      } else {
        console.log("artiste existant id : ", this.idArtist);
      }
    },

    async ajoutAlbum(){
      const responseArtist = await fetch("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/artists");
      const dataArtist = await responseArtist.json();
      this.idArtist = "";
      for(const artist of dataArtist.artists){
        if(artist.artist_name == this.nomArtiste){
          this.idArtist = artist.artist_id;
        }
      }
      
      const tokenAdmin = localStorage.getItem('admin_token')
      const param = 'artist_id=' + this.idArtist + '&album_title=' + this.titreAlbum + '&album_year=' + this.anneeAlbum + '&album_cover=' + this.coverAlbum;
      const response = await axios.get("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/add/album?"+param, {
                headers: {
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + tokenAdmin
                }});
      console.log(response.data)
    },

    async ajoutMusique(nomMusique){
      // Recupere id artiste
      const responseArtist = await fetch("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/artists");
      const dataArtist = await responseArtist.json();
      this.idArtist = "";
      for(const artist of dataArtist.artists){
        if(artist.artist_name == this.nomArtiste){
          this.idArtist = artist.artist_id;
        }
      }
      
      // Recupere l'album
      const responseAlbum = await fetch("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/albums?artist_id="+this.idArtist);
      const dataAlbum = await responseAlbum.json();
      let idAlbum = "";
      for(const album of dataAlbum.albums){
          console.log(album.album_title);
          if(album.album_title == this.titreAlbum){
            idAlbum = album.album_id;
          }
      }
      
      // Ajout de la musique
      const tokenAdmin = localStorage.getItem('admin_token')
      const param = 'album_id=' + idAlbum + '&song_title=' + nomMusique + '&song_length=' + '0';
      const response = await axios.get("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/add/song?"+param, {
                headers: {
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + tokenAdmin
                }});
      console.log(response.data)
    },

    async ajouter(submitEvent){
      // Récupère info du formulaire
      this.nomArtiste = submitEvent.target.elements.nomArtiste.value;
      this.titreAlbum = submitEvent.target.elements.titreAlbum.value;
      this.anneeAlbum = submitEvent.target.elements.anneeAlbum.value;
      this.coverAlbum = submitEvent.target.elements.coverAlbum.value;

      await this.ajoutArtiste()
      await this.ajoutAlbum()
      for(let i = 0; i < this.listeMusiqueForm.length; i++){
        await this.ajoutMusique(this.listeMusiqueForm[i].titreMusique)
      }
      useToast().success('Album ajouté', {
              position: 'top',
              dismissible:'true',
              duration:'5000'
          });
      this.$refs.formAjout.reset()
    },
    
    ajoutInputMusique(){
      this.listeMusiqueForm.push({key:this.musiqueKey++});
    },
    
    supprInputMusique(key){
      console.log(this.listeMusiqueForm)
      this.listeMusiqueForm.splice(key, 1);
    }

  }
}


</script>

<template>
    
  <h2 class="text-center text-white">Ajout Album</h2>
  <form ref="formAjout" @submit.prevent="ajouter">
      <div class="form-group p-2 text-white">
          <label>Artiste</label>
          <input class="form-control" name="nomArtiste" placeholder="Entrez le nom de l'artiste">
      </div>
      <div class="form-group p-2 text-white">
          <label>Titre de l'album</label>
          <input class="form-control" name="titreAlbum" placeholder="Entrez le titre de l'album">
      </div>
      <div class="form-group p-2 text-white">
          <label>Année de sortie</label>
          <input class="form-control" name="anneeAlbum" placeholder="Entrez l'année de sortie l'album">
      </div>
      <div class="form-group p-2 text-white">
          <label>Cover de l'album</label>
          <input class="form-control" name="coverAlbum" placeholder="Entrez la cover de l'album">
      </div>
      <div class="form-group p-2 text-white">
          <label>Liste des musiques</label> 
          
          <div class = "p-2" v-for="(musique,index) in listeMusiqueForm" :key="index">
            <div class="row">
              <div class="col-11">
                <input class="form-control" name="musique" placeholder="Entrez la musique" v-model="musique.titreMusique">
              </div>
              <div class="col-1 text-center">
                <button type="button" class="btn buttonMoins" v-on:click="supprInputMusique(index)" >-</button>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="col text-center">
              <button type="button" class="btn buttonPlus" v-on:click="listeMusiqueForm.push({key:this.musiqueKey++});">+</button> 
            </div>
          </div>
      </div>
      
      <div class="p-4 d-flex justify-content-center">
          <button type="submit" class="btn  buttonAjoutAlbum text-center ">Ajouter l'album</button>
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


.buttonAjoutAlbum {
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