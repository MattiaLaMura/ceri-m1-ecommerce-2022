<script setup>


import HeaderBackoffice from '/src/components/backoffice/HeaderBackoffice.vue';
import ListeUtilisateursComp from '/src/components/backoffice/ListeUtilisateursComp.vue';
</script>

<template>

    <HeaderBackoffice/>
    <div class="container pt-3">
        <div class="row">
            <div class="col-2"></div>
            <div class="col-8">
                <ListeUtilisateursComp/>
            </div>
            <div class="col-2"></div>
        </div>
    </div>
    
  
</template>

<style >

</style>
