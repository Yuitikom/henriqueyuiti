// Pre Loader //

const loader = document.getElementById("pre-loader");
window.addEventListener("load", function(){
     loader.style.display = "none";
})

// Swiper Projects //

const swiper = new Swiper(".projectbox", {
               slidesPerView: 3,
               spaceBetween: 30,
               slidesPerGroup: 3,
               loopFillGroupWithBlank: false,
               centerSlide: 'true',
               fade: 'true',
               loop: false,
               gragCursor: 'true',
               pagination: {
                    el: ".swiper-pagination",
                    clickable: true,
               },
               navigation: {
                    nextEl: ".swiper-button-next",
                    prevEl: ".swiper-button-prev",
               },

               breakpoints: {
                    0 : {
                         slidesPerView: 1,
                    },
                    520 : {
                         slidesPerView: 2,
                    }

               }


          });


// Scroll into section //

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
     anchor.addEventListener("click", function(e) {
          e.preventDefault();
          document.querySelector(this.getAttribute("href")).scrollIntoView({
               behavior : "smooth"
          })
     })

})