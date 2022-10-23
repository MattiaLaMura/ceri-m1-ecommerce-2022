<script>
export default{
    setup() {
        const imageUrl = new URL("../assets/images/albums/", import.meta.url).href;
        return { imageUrl };
    },
    props: {
     nom: { required: true, type: String },
     imageIndex :{ required: true, type: Int32Array }
    },
    methods:{
        
    }

}
</script>

<template>
 
    
        <div class="p-4 bg-dark rounded-3">
            <div class="row">
                <div class="col-md-3">
                    <img v-bind:src="imageUrl+imageIndex+'.jpg'" class="img-thumbnail">
                </div>
                <div class="col-md-9 text-white">
                  {{nom}} {{imageIndex}}
                </div>
            </div>
        </div>


</template>

<style scoped>
img {
    width: 150px; 
    height: 150px;
    
}
</style>