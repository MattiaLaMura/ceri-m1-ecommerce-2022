<script>
export default{
    setup() {
        // const imageUrl = new URL("images/albums/", import.meta.url).href;
        // return { imageUrl };
    },
    props: {
        nomAlbum: { required: true, type: String },
        idAlbum : { required: true },
        imageIndex :{ required: true },
        artist: { required: true, type: String },
        imageAlbum: { required: true, type: String }
    },
    methods:{
        goToDetailItem(nom){
            console.log(nom)
        }
    }

}
</script>

<template>
    <router-link :to="{name : 'detailItem', params: {idAlbum: idAlbum} }">
        <div class="card bg-dark">
            <img v-bind:src=imageAlbum class=" img-fluid card-img-top">
            <div class="card-title">
                <h5 class="card-text text-center text-white py-3">{{nomAlbum}} </h5>
            </div>
            <div class="card-text">
                <div class="card-text text-center text-white">{{artist}}</div>
            </div>
        </div>
      
    </router-link>

</template>

<style scoped>
img {
    width: 150px; 
    height: 150px;
    margin: auto;    
    display: block;
}
a { 
    text-decoration: none; 
}

.card-img-top {
    width: 100%;
    
    object-fit: cover;
}
</style>