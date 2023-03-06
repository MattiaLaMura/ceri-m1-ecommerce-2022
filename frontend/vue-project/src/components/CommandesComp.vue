<script>
import axios from 'axios'
import {getCurrentInstance, defineComponent} from 'vue'

export default{
    data(){
        return {
            listAlbums:[],
            backendUrl :"https://purplepig-backend-mwjszocsqa-ew.a.run.app"
        }
    },
    async created(){
        this.initCommandes()
    },
    methods:{
        async initCommandes(){
            const token = localStorage.getItem('user_token')
            const urlCommandes = "https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/items"

            const responseCommandes = await axios.get(urlCommandes, {
                headers: {
                    'Accept': 'application/json',
                    'Authorization': 'Bearer ' + token
                }});
            
            console.log(responseCommandes.data.items)
            // Récupère info des albums du Commandes
            if(responseCommandes.data != null){
                for(const albumCommandes of responseCommandes.data.items){
                    
                    const responseArtists = await axios.get("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/artists")
                    
                    for(const artist of responseArtists.data.artists){
                        const responseAlbum = await axios.get("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/albums?artist_id="+artist.artist_id)

                        for(const album of responseAlbum.data.albums){
                            if(albumCommandes.album_id == album.album_id && albumCommandes.paid == true){
                                this.listAlbums.push({itemId:albumCommandes.item_id,nomAlbum:album.album_title, artist:artist.artist_name, imageAlbum:album.album_image_url, itemStatus:albumCommandes.delivery})
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
                <div v-for="(album,index) in listAlbums" :key="index" >
                    <div class = p-4>
                        <div class="row p-2 rounded-2 bg-dark">
                            <div class="col-lg-4 text-center">
                                <img v-bind:src=album.imageAlbum class="img-fluid">
                            </div>
                            <div class="col-lg-8 ">
                                <h3 class="text-white">{{album.nomAlbum}} - {{album.artist}}</h3>
                                <div class="text-white">Status : {{album.itemStatus}}</div>
                                
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