<script>
export default{
    setup() {
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
            <img v-bind:src=imageAlbum class=" img-fluid card-img-top align-items-stretch">
            <div class="card-title">
                <div class="card-text text-center text-white py-3 fw-bold">{{nomAlbum}} </div>
                <div class="card-text text-center text-white">{{artist}}</div>
            </div>
        </div>
      
    </router-link>

</template>

<style scoped>
img {
    height: auto;
    width: 100%;
    margin: auto;    
    display: block;
}
a { 
    text-decoration: none; 
}

</style>