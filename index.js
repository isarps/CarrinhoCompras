function Enviar(){
    const input = document.querySelector("input")
    let areaTexto = document.querySelector(".areaTexto")
    areaTexto.innerHTML+=`<div class="usuario">você:${input.value}</div>`
}