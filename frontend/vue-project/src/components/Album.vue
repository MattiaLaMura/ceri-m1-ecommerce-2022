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
        
    }

}
</script>

<template>

    <div class="p-4 bg-dark rounded-3">
        <img v-bind:src="imageUrl+imageIndex+'.jpg'" class="img img-fluid">
        <div class="text-center text-white">
            {{nom}} {{imageIndex}}
        </div>
        <div class="text-center text-white">
            {{artist}} {{imageIndex}}
        </div>
        
    </div>

</template>

<style scoped>
img {
    width: 150px; 
    height: 150px;
    margin: auto;    
    display: block;
}
</style>