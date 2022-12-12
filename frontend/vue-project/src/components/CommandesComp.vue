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
        this.initCommandes()
    },
    methods:{
        async initCommandes(){
            const token = localStorage.getItem('user_token')
            const urlCommandes = "http://localhost:8000/get/items"

            const responseCommandes = await axios.get(urlCommandes, {
                headers: {
                    'Accept': 'application/json',
                    'Authorization': 'Bearer ' + token
                }});
            
            console.log(responseCommandes.data.items)
            // Récupère info des albums du Commandes
            if(responseCommandes.data != null){
                for(const albumCommandes of responseCommandes.data.items){
                    
                    const responseArtists = await axios.get("http://localhost:8000/get/artists")
                    
                    for(const artist of responseArtists.data.artists){
                        const responseAlbum = await axios.get("http://localhost:8000/get/albums?artist_id="+artist.artist_id)

                        for(const album of responseAlbum.data.albums){
                            if(albumCommandes.album_id == album.album_id && albumCommandes.paid == true){
                                this.listAlbums.push({itemId:albumCommandes.item_id,nomAlbum:album.album_title, imageAlbum:album.album_image_url})
                            }
                        }
                    }
                }
            }
            console.log(this.listAlbums)
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
                            </div>
                        </div>
                    </div>
                </div>
             
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