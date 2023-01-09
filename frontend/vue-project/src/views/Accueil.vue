<script setup>

import AlbumList from '/src/components/AlbumList.vue';
import Header from '/src/components/Header.vue';
import Carousel from '/src/components/Carousel.vue';
import SearchBar from '/src/components/SearchBar.vue';


</script>

<template>

    <Header/>
    <Carousel/>
    <h2 class="text-white text-center">Liste des albums</h2>
    <!-- <SearchBar/> -->
    <AlbumList/>
  
</template>

<style >

</style>
