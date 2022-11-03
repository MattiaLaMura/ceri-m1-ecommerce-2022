<script>
export default{
    data() {
        return {
            isSticky: false,
            stickyClass: 'is_sticky',
            scrollPosition:0,
            title: 'fds'
        }
    },
    created () {
            window.addEventListener('scroll', this.handleScroll);
    },
    destroyed () {
            window.removeEventListener('scroll', this.handleScroll);
    },
    methods:{
        handleScroll(event){
            this.scrollPosition = window.scrollY
            if(this.scrollPosition>=300){
                this.title = "Jean Cloud Vinyl"
                this.isSticky=true
                console.log(this.isSticky)
            }else{
                this.isSticky=false
                this.title = ""
            }
        },
        scrollToTop() {
            window.scrollTo(0,0);
        }
    }
}
</script>

<template>
    <div class="container bg-dark rounded-3">
        
        <header class="d-flex justify-content-center py-3">
        <ul class="nav nav-pills">

            <router-link v-on:click="scrollToTop()" to="/" class="nav-link text-white" aria-current="page" >Home</router-link>
        
            <li class="nav-item"><a href="#" class="nav-link text-white">Features</a></li>
            <li class="nav-item"><a href="#" class="nav-link text-white">Pricing</a></li>
            <li class="nav-item"><a href="#" class="nav-link text-white">FAQs</a></li>
            <li class="nav-item"><a href="#" class="nav-link text-white">About</a></li>
        </ul>
        </header>
    </div>

</template>

<style scoped>
.container{
    position: sticky;
    top: 0px;
    z-index:100;
}
</style>