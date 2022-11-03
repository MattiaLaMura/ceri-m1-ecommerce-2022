<script>
export default{
    setup() {
        const imageUrl = new URL("../assets/images/albums/", import.meta.url).href;
        return { imageUrl };
    },
    props: {
     nom: { required: true, type: String },
     imageIndex :{ required: true, type: Int32Array },
     artist: { required: true, type: String }
    },
    methods:{
        goToDetailItem(nom){
            console.log(nom)
        }
    }

}
</script>

<template>
    <router-link :to="{name : 'detailItem', params: { nomAlbum: imageIndex } }">
        <!-- <router-link to="/item" v-slot="{navigate}">
        kk
        </router-link> -->
        <!-- <div v-on:click="goToDetailItem(imageIndex)" class="p-4 bg-dark rounded-3 cursor_hover">
            <img v-bind:src="imageUrl+imageIndex+'.jpg'" class="img img-fluid">
            <div class="text-center text-white">
                {{nom}} {{imageIndex}}
            </div>
            <div class="text-center text-white">
                {{artist}} {{imageIndex}}
            </div>
            
        </div> -->

       
        <div class="card bg-dark">
            <img v-bind:src="imageUrl+imageIndex+'.jpg'" class=" img-fluid card-img-top">
            <div class="card-title">
                <h5 class="card-text text-center text-white py-3">{{nom}} {{imageIndex}}</h5>
            </div>
            <div class="card-text">
                <div class="card-text text-center text-white">{{artist}} {{imageIndex}}</div>
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
.cursor_hover{
    cursor:pointer;
}

.card-img-top {
    width: 100%;
    
    object-fit: cover;
}
</style>