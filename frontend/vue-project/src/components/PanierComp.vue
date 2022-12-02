<script>
import axios from 'axios'
import {getCurrentInstance, defineComponent} from 'vue'
export default{
    data(){
        return {
            listAlbums:[],
        }
    },
    async created(){
        this.initPanier()
    },
    methods:{
        async initPanier(){
            const token = localStorage.getItem('user_token')
            const urlPanier = "http://host.docker.internal:8000/get/items"

            const responsePanier = await axios.get(urlPanier, {
                headers: {
                    'Accept': 'application/json',
                    'Authorization': 'Bearer ' + token
                }});
            
            console.log(responsePanier.data.items)
            // Récupère info des albums du panier
            if(responsePanier.data != null){
                for(const albumPanier of responsePanier.data.items){
                    
                    const responseArtists = await axios.get("http://host.docker.internal:8000/get/artists")
                    
                    for(const artist of responseArtists.data.artists){
                        const responseAlbum = await axios.get("http://host.docker.internal:8000/get/albums?artist_id="+artist.artist_id)

                        for(const album of responseAlbum.data.albums){
                            if(albumPanier.album_id == album.album_id && albumPanier.paid == false){
                                this.listAlbums.push({itemId:albumPanier.item_id,nomAlbum:album.album_title, imageAlbum:album.album_image_url})
                            }
                        }
                    }
                }
            }
            console.log(this.listAlbums)
        },
        async enleverPanier(item_id){
            
            const token = localStorage.getItem('user_token')
            const urlEnleverPanier = "http://host.docker.internal:8000/remove/item"
            const paramEnleverPanier = "?item_id="+ item_id
            const responseEnleverPanier = await axios.get(urlEnleverPanier + paramEnleverPanier, {
                headers: {
                    'Accept': 'application/json',
                    'Authorization': 'Bearer ' + token
                }});
            console.log(responseEnleverPanier.data)
        },
        async acheterPanier(){
            const token = localStorage.getItem('user_token')
            const urlAcheterPanier = "http://host.docker.internal:8000/buy/items"
            
            for(const album of this.listAlbums){
                const paramAcheterPanier = "?item_id="+ album.itemId
                const responseAcheterPanier = await axios.get(urlAcheterPanier + paramAcheterPanier, {
                    headers: {
                        'Accept': 'application/json',
                        'Authorization': 'Bearer ' + token
                    }});
                
                console.log(responseAcheterPanier.data)
            }
            this.listAlbums.splice(0)
        }
    }
}
</script>

<template>
   
    <div class="container">
        <div class="row">
            <div class="col-lg-7">
                
                <div v-for="(album,index) in listAlbums" :key="index" >
                    <div class = p-4>
                        <div class="row p-2 rounded-2 bg-dark">
                            <div class="col-lg-4">
                                <img v-bind:src=album.imageAlbum class="img-fluid">
                            </div>
                            <div class="col-lg-8 ">
                                <div class="text-white">{{album.nomAlbum}}</div>
                                <a v-on:click="enleverPanier(album.itemId); listAlbums.splice(index, 1)" href="#" class="">Supprimer du panier</a>
                            </div>
                        </div>
                    </div>
                </div>
             
            </div>
            
            <div class="col-lg-4 p-4 text-center">
                <button v-on:click="acheterPanier()" type="submit" class="btn buttonPayer">Acheter les articles</button>
            </div>
        </div>
    </div>
   
</template>

<style scoped>
img {
    width: 200px; 
    height: 200px;
    /* margin: auto;     */
    /* display: block; */
}
.card-img-top {
    width: 100%;
    
    object-fit: cover;
}

.buttonPayer {
  background-color: #dc6e00;
  width: 150px;
  height: 40px;
  color: white;
  font-size: 14px;
  border-radius: 16px;
}
</style>