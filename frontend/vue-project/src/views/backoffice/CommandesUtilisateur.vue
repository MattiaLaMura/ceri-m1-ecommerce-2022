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
    
    <div class="container pt-3">
        <div class="row">
            <div class="col-2"></div>
            <div class="col-8">
                <CommandesUtilisateurComp :idUtilisateur = "idUtilisateur"/>
            </div>
            <div class="col-2"></div>
        </div>
    </div>
  
</template>

<style >

</style>
