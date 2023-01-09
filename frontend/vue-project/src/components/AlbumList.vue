<script>
import { processExpression } from '@vue/compiler-core';
import Album from './Album.vue'
import SearchBar from './SearchBar.vue';

export default{
    
    components: {
        Album,
        SearchBar
    },
    data(){
        return {
            listAlbums:[],
            backendUrl :"https://purplepig-backend-mwjszocsqa-ew.a.run.app"
        }
    },
    async created() {
       
        this.setAlbumList()


        // this.$on('recherche_terminée', this.handleRecherche)

    },
    methods:{
        async setAlbumList(){
             // Récupère liste des albums
            const responseArtist = await fetch("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/artists");
            const dataArtist = await responseArtist.json();
    
            for(const artist of dataArtist.artists){
                const responseAlbum = await fetch("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/albums?artist_id="+artist.artist_id);
                const dataAlbum = await responseAlbum.json();
                for(const album of dataAlbum.albums){
                    this.listAlbums.push({nomAlbum:album.album_title, idAlbum:album.album_id, artist:artist.artist_name, imageAlbum:album.album_image_url})
                }
            }
        },
        async updateAlbumList(searchedAlbums){
            this.listAlbums = []
            if(searchedAlbums.length == 0){
                this.setAlbumList()
            } else {
                console.log(searchedAlbums)
                for(const album of searchedAlbums){
                    const responseAlbum = await fetch("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/album?album_id="+album.objectID);
                    const dataAlbum = await responseAlbum.json();
                    console.log(dataAlbum)
                    
                    this.listAlbums.push({nomAlbum:album.album_title, idAlbum:album.objectID, artist:album.artist_name, imageAlbum:dataAlbum.album.album_image_url})
                    
                    
                }
            }
            
        }
    }

}
</script>

<template>
    <SearchBar @recherche_terminée="updateAlbumList"/>
    <div class="container pt-3">
        <div class="row">
            <div class="col-2"></div>
            <div class="col-8">
                <div class="row">
                    <div class="p-4 col-lg-4" v-for="(album, index) in listAlbums" :key="album.id">
                        <Album :nomAlbum="album.nomAlbum" :idAlbum="album.idAlbum" :artist="album.artist" :imageIndex="index+1" :imageAlbum="album.imageAlbum"></Album>
                    </div>
               </div>
            </div>
            <div class="col-2"></div>
        </div>
    </div>
</template>

<style scoped>

</style>
