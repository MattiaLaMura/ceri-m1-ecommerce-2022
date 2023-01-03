<script>
import 'vue3-carousel/dist/carousel.css'

import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'

export default {
  name: 'App',
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  data() {
    return {
      images: [{id: 1,url:'https://cdn.pixabay.com/photo/2019/12/18/04/11/dj-4702977_960_720.jpg'}, {id: 2,url:'https://media.lesechos.com/api/v1/images/view/61279e30d286c209fa5eb266/1280x720/0611565575659-web-tete.jpg'}, {id: 3,url:'https://parissecret.com/wp-content/uploads/2022/10/COUV-ARTICLES-1920x1080-63-1024x576.jpg'}]
    }
  },
}
</script>

<template>
    <carousel :items-to-show="1.5" :modelValue="1" :wrapAround="true">
      <slide v-for="(image, index) in images" :key="image.id">
        <img class="carousel__item rounded-2" :src="image.url" />
      </slide>
  
      <template #addons>
        <navigation />
        <pagination />
      </template>
    </carousel>
</template>

<style>
.carousel__item {
    width: 100%; 
    height: 600px;
    margin: auto;    
    display: block;
}

.carousel__slide {
    padding: 20px;
}

.carousel__prev,
.carousel__next {
    border-radius: 50%;
    margin: 0 16px;
    width: 40px;
    height: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #ffffff !important;
    color:#dc6e00;
    box-sizing: content-box;
}
.carousel__pagination{
    
    color:#dc6e00;
    

}
</style>