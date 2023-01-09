<script>
import axios from 'axios'
import {useToast} from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';
export default{
    
    setup() {
    },
    props: {
        idAlbum :{ required: true },
        imageIndex :{ required: false, type: Int32Array },
        
    },
    methods:{
        async ajoutPanier(){
            const token = localStorage.getItem('user_token')
            
            const urlAjoutPanier ="https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/add/item?"
            const paramAjourPanier = "album_id=" + this.idAlbum + "&paid=false"

            const responseAjoutPanier= await axios.get(urlAjoutPanier + paramAjourPanier, {
                headers: {
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + token
                }}).catch(function(error) {
                    useToast().error('Erreur serveur.', {
                        position: 'top',
                        dismissible:'true',
                        duration:'5000'
                    });
                });


            useToast().success('Album ajouté au panier', {
              position: 'top',
              dismissible:'true',
              duration:'5000'
            });
            console.log(responseAjoutPanier.data)
        }
    },
    data(){
        return {
            user_name:"",
            nomAlbum: "",
            artist: "",
            imageAlbum: "",
            anneeAlbum: "",
            listeMusique:[],
            backendUrl :"https://purplepig-backend-mwjszocsqa-ew.a.run.app"
        }
    },
    async created() {
        // Afficharge ou non du bouton ajout panier
        if(localStorage.getItem('user_name') != null){
            this.user_name = localStorage.getItem('user_name')
        } else this.user_name = '';

        // Récupère les données de l'album
        const responseSongs = await fetch("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/songs?album_id="+this.idAlbum);
        const dataSongs = await responseSongs.json();
        
        for(const song of dataSongs.songs){
            this.listeMusique.push({titre:song.song_title})
        }

        const responseArtist = await fetch("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/artists");
        const dataArtist = await responseArtist.json();
  
        for(const artist of dataArtist.artists){
            const responseAlbum = await fetch("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/albums?artist_id="+artist.artist_id);
            const dataAlbum = await responseAlbum.json();
            for(const album of dataAlbum.albums){
                if(album.album_id == this.idAlbum){
                    this.nomAlbum = album.album_title;
                    this.artist = artist.artist_name; 
                    this.imageAlbum = album.album_image_url;
                    this.anneeAlbum = album.album_year.slice(0,4);
                }
            }
        }
    },
    
    

}
</script>

<template>
   
   <div class = "container">
        <div class="row text-white py-4"><h3>{{nomAlbum}} - {{ artist }} - {{ anneeAlbum }}</h3></div>
        <div class="row">

            <div class="col-lg-5">
                <img v-bind:src="imageAlbum" class="card-img-top">
            </div>

            <div class="col-lg-5">
                <div v-if="user_name != ''" class="p-4 d-flex justify-content-center">
                    <button v-on:click="ajoutPanier()" type="submit" class="btn buttonPanier  ">Ajouter au panier</button>
                </div>

                <hr class="bg-danger border-2 border-top ">
                <h4 class="text-white text-center py-3">Contenu</h4>
                <div class="p-2 text-white " v-for="(musique, index) in listeMusique" :key="musique.id">
                    <div class="rounded-2 bg-dark">
                        <div class="p-2">
                            {{index+1}}&nbsp;&nbsp;    {{musique.titre}}
                        </div>
                    </div>
                </div>
            </div>
        </div>
   </div>
</template>

<style scoped>
img {
    width: 500px; 
    height: 500px;
    margin: auto;    
    display: block;
}
.card-img-top {
    width: 100%;
    
    object-fit: cover;
}

.buttonPanier {
  background-color: #dc6e00;
  width: 150px;
  height: 40px;
  color: white;
  font-size: 14px;
  border-radius: 16px;
}
</style>