<script>
import Album from './Album.vue'
export default{
    
    components: {
        Album
    },
    data(){
        return {
            listAlbums:[
                //  {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                // {nom:'album',artist:'artist'},
                
            ],
            // Album:[]

        }
    },
    async created() {
        const responseArtist = await fetch("http://localhost:8000/get/artists");
        const dataArtist = await responseArtist.json();
  
        for(const artist of dataArtist.artists){
            // console.log(artist)
            // console.log(artist.artist_id)
            const responseAlbum = await fetch("http://localhost:8000/get/albums?artist_id="+artist.artist_id);
            const dataAlbum = await responseAlbum.json();
            // console.log(dataAlbum);
            for(const album of dataAlbum.albums){
                // console.log(album);
                this.listAlbums.push({nomAlbum:album.album_title, idAlbum:album.album_id, artist:artist.artist_name, imageAlbum:album.album_image_url})
            }
        }

    },
    methods:{
      
    }

}
</script>

<template>
    <!-- {{fetchData()}} -->
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
