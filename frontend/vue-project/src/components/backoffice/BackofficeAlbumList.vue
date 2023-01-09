<script>
import Album from '../Album.vue'
export default{
    
    components: {
        Album
    },
    data(){
        return {
            listAlbums:[],
            plusImg :'https://p.kindpng.com/picc/s/712-7123671_plus-sign-circle-png-clipart-png-download-black.png',
            backendUrl :"https://purplepig-backend-mwjszocsqa-ew.a.run.app"
        }
    },
    async created() {
        // Récupère la liste des albums
        const responseArtist = await fetch("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/artists");
        const dataArtist = await responseArtist.json();
  
        for(const artist of dataArtist.artists){
            const responseAlbum = await fetch("https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/get/albums?artist_id="+artist.artist_id);
            const dataAlbum = await responseAlbum.json();
            for(const album of dataAlbum.albums){
                this.listAlbums.push({nomAlbum:album.album_title, idAlbum:album.album_id, artist:artist.artist_name, imageAlbum:album.album_image_url})
            }
        }
    }

}
</script>

<template>
    <div class="container pt-3">
        <div class="row">
            <div class="col-2"></div>
            <div class="col-8">
                <div class="row">
                    <div class="p-4 col-lg-4">
                        <router-link :to="{name : 'ajoutAlbum' }">
                            <div class="card bg-dark">
                                <img v-bind:src=plusImg class=" img-fluid card-img-top">
                                <div class="card-title">
                                    <h5 class="card-text text-center text-white py-3">Ajouter Album</h5>
                                </div>
                            </div>
                        </router-link>
                    </div>
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
