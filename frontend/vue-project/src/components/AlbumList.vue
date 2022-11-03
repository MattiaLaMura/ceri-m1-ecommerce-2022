<script>
import Album from './Album.vue'
export default{
    
    components: {
        Album
    },
    data(){
        return {
            Album:[
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                {nom:'album',artist:'artist'},
                
            ]
        }
    },
    methods:{
        
    }

}
</script>

<template>
    <div class="container pt-3">
        <div class="row">
            <div class="col-2"></div>
            <div class="col-8">
                <div class="row">
                    <div class="p-4 col-lg-4" v-for="(album, index) in Album" :key="album.id">
                        <Album :nom="album.nom" :artist="album.artist" :imageIndex="index+1"></Album>
                    </div>
               </div>
            </div>
            <div class="col-2"></div>
        </div>
    </div>
</template>

<style scoped>

</style>
