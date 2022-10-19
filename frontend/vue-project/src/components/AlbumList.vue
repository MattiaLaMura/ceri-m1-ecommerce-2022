<script>
import Album from './Album.vue'
export default{
    
    components: {
        Album
    },
    data(){
        return {
            Album:[
                {nom:'album1'},
                {nom:'album2'},
                {nom:'album3'},
                {nom:'album1'},
                {nom:'album2'},
                {nom:'album3'},
                {nom:'album1'},
                {nom:'album2'},
                {nom:'album3'},
            ]
        }
    },
    methods:{
        
    }

}
</script>

<template>
    <div class="container mt-3">
        <div class="p-2" v-for="album in Album" :key="album.id">
            <Album :nom="album.nom"></Album>
        </div>
    </div>
</template>

<style scoped>

</style>
