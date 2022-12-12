<script>
export default{
    setup() {
        // const imageUrl = new URL("images/albums/", import.meta.url).href;
        // return { imageUrl };
    },
    props: {
        idAlbum :{ required: true },
        imageIndex :{ required: false, type: Int32Array },
    },
    methods:{
        
    },
    data(){
        return {
            nomAlbum: " ",
            artist: "",
            imageAlbum: "",
            listeMusique:[
                // {titre:"Musique 1"},
                // {titre:"Musique 2"},
                // {titre:"Musique 3"},
                // {titre:"Musique 4"},
                // {titre:"Musique 5"}
            ]
        }
    },
    async created() {
        const responseSongs = await fetch("http://host.docker.internal:8000/get/songs?album_id="+this.idAlbum);
        const dataSongs = await responseSongs.json();
        
        for(const song of dataSongs.songs){
            this.listeMusique.push({titre:song.song_title})
        }

        const responseArtist = await fetch("http://host.docker.internal:8000/get/artists");
        const dataArtist = await responseArtist.json();
  
        for(const artist of dataArtist.artists){
            const responseAlbum = await fetch("http://host.docker.internal:8000/get/albums?artist_id="+artist.artist_id);
            const dataAlbum = await responseAlbum.json();
            for(const album of dataAlbum.albums){
                if(album.album_id == this.idAlbum){
                    this.nomAlbum = album.album_title;
                    this.artist = artist.artist_name; 
                    this.imageAlbum = album.album_image_url;
                }
            }
        }

    }

}
</script>

<template>
   
   <div class = "container">
        <div class="row text-white py-4"><h3>Albums</h3></div>
        <div class="row">

            <div class="col-lg-5">
                <img v-bind:src="imageAlbum" class="card-img-top">
            </div>

            <div class="col-lg-7">
                <h3 class="card-text text-white py-3">{{nomAlbum}}</h3>
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

</style>