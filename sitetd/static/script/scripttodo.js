console.log('privet')
const all = document.getElementById('ex1-tab-1');
const active = document.getElementById('ex1-tab-2');
const complite = document.getElementById('ex1-tab-3');
const allc = document.getElementById('ex1-tabs-1');
const activec = document.getElementById('ex1-tabs-2');
const complitec = document.getElementById('ex1-tabs-3');
const allnav = [all,active,complite];
const allnavc = [allc,activec,complitec];


function removeActive() {
    for (let i of allnav) {
        if (i.classList.contains('active')) {
            i.classList.remove('active')
        }
    }
    for (let i of allnavc) {
        if (i.classList.contains('active')) {
            i.classList.remove('active');
            i.classList.remove('show');
        }
    }
}


function activedBut(button) {
    if (!button.getAttribute('class').includes('active')) {
        removeActive();
        let show = allnavc[+button.getAttribute('id').slice(-1)-1];

        show.classList.add('show');
        show.classList.add('active');
        console.log(show);
        button.classList.add('active');

    }
}

all.addEventListener('click', ()=>activedBut(all));
active.addEventListener('click',()=>activedBut(active));
complite.addEventListener('click',()=>activedBut(complite));