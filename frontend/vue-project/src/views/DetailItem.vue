<script>


import Header from '/src/components/Header.vue';
import AlbumDetails from '/src/components/AlbumDetails.vue';


export default {
    props: ["idAlbum"],
    components: { Header, AlbumDetails }
}


</script>

<template>
    <Header/>
    <AlbumDetails :idAlbum = "idAlbum"/>
    
  
</template>

<style >

</style>
