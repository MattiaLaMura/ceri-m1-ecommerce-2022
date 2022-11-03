<script>
export default{
    setup() {
        const imageUrl = new URL("../assets/images/albums/", import.meta.url).href;
        return { imageUrl };
    },
    props: {
     nomAlbum: { required: true, type: String },
     imageIndex :{ required: true, type: Int32Array },
     artist: { required: true, type: String }
    },
    methods:{
        
    },
    data(){
        return {
            listeMusique:[
                {titre:"Musique 1"},
                {titre:"Musique 2"},
                {titre:"Musique 3"},
                {titre:"Musique 4"},
                {titre:"Musique 5"},
                {titre:"Musique 6"},
                 
            ]
        }
    },

}
</script>

<template>
   
   <div class = "container">
        <div class="row text-white py-4"><h3>Albums</h3></div>
        <div class="row">

            <div class="col-lg-5">
                
                <img v-bind:src="imageUrl+nomAlbum+'.jpg'" class=" card-img-top">
              
            </div>

            <!-- <div class="col-lg-5">
                <div class="card bg-dark">
                    <img v-bind:src="imageUrl+nomAlbum+'.jpg'" class=" card-img-top">
                    <div class="card-title">
                        <h5 class="card-text text-center text-white py-3">Album {{nomAlbum}}</h5>
                    </div>
                </div>
            </div> -->

            <div class="col-lg-7">
                <h3 class="card-text text-white py-3">Album {{nomAlbum}}</h3>
                <div class="p-2 text-white " v-for="musique in listeMusique">
                            <div>{{musique.titre}}</div>
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