<script>
import axios from 'axios'
export default{
    data(){
        return {
            listeAlbum:[],
            request:"",
            backendUrl :"https://purplepig-backend-mwjszocsqa-ew.a.run.app"
        }
    },
    async created(){

    },
    methods:{
        async submitSearch(submitEvent){
          this.request = submitEvent.target.elements.request.value;
          if(this.request == ""){
            this.$emit('recherche_terminée', [])
          } else {
            console.log(this.request)
            const url = "https://purplepig-backend-mwjszocsqa-ew.a.run.app"+"/search_engine?"
            const param = 'word_searched=' + this.request;
            const response = await axios.get(url+param).catch(function(error){
                console.log("error search")
            })
            console.log(response.data.result.hits)
            this.$emit('recherche_terminée', response.data.result.hits)
          }
        }
    }
}
</script>

<template>
    <div class="container">
        <div class="row d-flex p-4 justify-content-center align-items-center">
            <div class="col-md-8">
                <div class="search">
                    <i class="fa fa-search"></i>
                    <form id="search-form" @submit.prevent="submitSearch">
                        <input type="text" class="form-control" name="request" placeholder="Rechercher un album/artiste/musique">
                        <button type="submit" class="btn text-white">Rechercher</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>

img {
    width: 200px; 
    height: 200px;
}
.card-img-top {
    /* width: 100%; */
    
    object-fit: cover;
}

.buttonRecherche {
  background-color: #dc6e00;
  
  color: white;
  /* font-size: 14px; */
  /* border-radius: 16px; */
}

@import url("https://fonts.googleapis.com/css2?family=Poppins:weight@100;200;300;400;500;600;700;800&display=swap");


       body{
        background-color:#eee;
        font-family: "Poppins", sans-serif;
        font-weight: 300;
       }

       .search{
       position: relative;
       box-shadow: 0 0 40px rgba(51, 51, 51, .1);
         
       }

       .search input{

        height: 60px;
        text-indent: 25px;
        border: 2px solid #d6d4d4;


       }


       .search input:focus{

        box-shadow: none;
        border: 2px solid #dc6e00;


       }

       .search .fa-search{

        position: absolute;
        top: 20px;
        left: 16px;

       }

       .search button{

        position: absolute;
        top: 5px;
        right: 5px;
        height: 50px;
        width: 110px;
        background: #dc6e00;

       }

</style>