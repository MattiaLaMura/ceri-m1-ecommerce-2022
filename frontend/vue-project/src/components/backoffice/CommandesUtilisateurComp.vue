<script>
import axios from 'axios'
import {getCurrentInstance, defineComponent} from 'vue'
export default{
    data(){
        return {
            listAlbums:[],
            selectedStatus: "",
            statusCommande: ["En préparation","Envoyé","En cours","Livré"]
        }
    },
    props: {
        idUtilisateur :{ required: true }
    },
    async created(){
        this.initCommandes()
    },
    methods:{
        async initCommandes(){
            const token = localStorage.getItem('admin_token')
            const urlCommandes = "http://localhost:8000/get/orders?user_id=" + this.idUtilisateur;
            // console.log(urlCommandes)
            const responseCommandes = await axios.get(urlCommandes, {
                headers: {
                    'Accept': 'application/json',
                    'Authorization': 'Bearer ' + token
                }});
            
            // console.log(responseCommandes.data)
            // Récupère info des albums du Commandes
            if(responseCommandes.data != null){
                for(const albumCommandes of responseCommandes.data.orders){
                    
                    const responseArtists = await axios.get("http://localhost:8000/get/artists")
                    
                    for(const artist of responseArtists.data.artists){
                        const responseAlbum = await axios.get("http://localhost:8000/get/albums?artist_id="+artist.artist_id)

                        for(const album of responseAlbum.data.albums){
                            if(albumCommandes.album_id == album.album_id && albumCommandes.paid == true){
                                this.listAlbums.push({itemId:albumCommandes.item_id,nomAlbum:album.album_title, imageAlbum:album.album_image_url, itemStatus:albumCommandes.delivery})
                            }
                        }
                    }
                }
            }
            // console.log(this.listAlbums)
        },
        async changeStatus(idItem,status){
            const token = localStorage.getItem('admin_token')
            const urlCommandes = "http://localhost:8000/update/item?item_id="+ idItem +"&user_id=" + this.idUtilisateur + "&item_status=" + status;
            console.log(urlCommandes)
            const responseCommandes = await axios.get(urlCommandes, {
                headers: {
                    'Accept': 'application/json',
                    'Authorization': 'Bearer ' + token
                }});
            
            console.log(responseCommandes.data)
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
                                <h3 class="text-white">{{album.nomAlbum}}</h3>
                                <div  class="text-white">Status : {{album.itemStatus}}</div><br />
                                <v-select class="bg-white" 
                                v-model="album.itemStatus"
                                :options="statusCommande"
                                @update:modelValue="changeStatus(album.itemId,album.itemStatus)"
                                />
                               
                               
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