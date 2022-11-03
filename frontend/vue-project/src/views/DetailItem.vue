<script>


import Header from '@/components/Header.vue';
import AlbumDetails from '@/components/AlbumDetails.vue';


export default {
    props: ["nomAlbum"],
    components: { Header, AlbumDetails }
}


</script>

<template>
    <Header/>
    <AlbumDetails :nomAlbum = "nomAlbum"/>
    <div>{{nomAlbum}}</div>
  
</template>

<style >

</style>
