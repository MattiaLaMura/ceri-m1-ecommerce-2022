<script>
export default{
    props: {
     nom: { required: true, type: String }
    },
    methods:{
        
    }

}
</script>

<template>
 
    <div class="row">
        <div class="p-4 bg-danger rounded-3">{{nom}}</div>
    </div>

</template>

<style scoped>

</style>