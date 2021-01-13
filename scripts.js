
//select th element like home
const selectElement = (s) => document.querySelector(s);
//open the menu on onclick
selectElement('.open').addEventListener('click', () => {
  selectElement('.nav-list').classList.add('active');
});
//close the menu on onclick
selectElement('.close').addEventListener('click', () => {
  selectElement('.nav-list').classList.remove('active');
});

('.navbar a').on('click', function (e) {
   if (this.hash !== '') {
     e.preventDefault();

     const hash = this.hash;

     ('html, body')
       .animate({
         scrollTop: (hash).offset().top
       },800);
   }
 });
