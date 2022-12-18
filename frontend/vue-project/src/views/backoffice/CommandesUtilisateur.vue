<script>

import HeaderBackoffice from '/src/components/backoffice/HeaderBackoffice.vue';
import CommandesUtilisateurComp from '/src/components/backoffice/CommandesUtilisateurComp.vue';

export default {
    props: ["idUtilisateur"],
    components: { HeaderBackoffice, CommandesUtilisateurComp }
}


</script>

<template>
    <HeaderBackoffice/>
    <h3 class="text-white text-center">Commandes</h3>
    <CommandesUtilisateurComp :idUtilisateur = "idUtilisateur"/>
    
  
</template>

<style >

</style>
