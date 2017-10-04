function validarLogin(){
    var username = document.getElementById("loginusuario").value;
    var password = document.getElementById("loginsenha").value;
    if ( username == "admin" && password == "admin"){
	localStorage.setItem('username', username);
	window.location.href = 'index.html?login=true';
    }
    else{
	alert("Usuário e/ou Senha incorretos.")
    }
}

function personalizarCadastroFornecedor(){
    var nomeFornecedor = document.getElementById("nomefornecedor").value;
    var razaoSocial = document.getElementById("razaosocial").value;
    var cpfFornecedor = document.getElementById("cpffornecedor").value;
    var cnpjFornecedor = document.getElementById("cnpjfornecedor").value;


    if(nomeFornecedor.length > 0 || cpfFornecedor.length > 0){
	document.getElementById("razaosocial").disabled = true;
	document.getElementById("cnpjfornecedor").disabled = true;
    }
    else if(nomeFornecedor.length == 0 || cpfFornecedor.length == 0){
	document.getElementById("razaosocial").disabled = false;
	document.getElementById("cnpjfornecedor").disabled = false;
    }
    if(razaoSocial.length > 0 || cnpjFornecedor.length > 0){
	document.getElementById("nomefornecedor").disabled = true;
	document.getElementById("cpffornecedor").disabled = true;
    }
    else if(razaoSocial.length == 0 || cnpjFornecedor.length == 0){
	document.getElementById("nomefornecedor").disabled = false;
	document.getElementById("cpffornecedor").disabled = false;
    }
}

function ValidaEmail(valor){
    exp_reg = /^([a-zA-Z0-9_.-])+@([a-zA-Z0-9_.-])+\.([a-zA-Z])+([a-zA-Z])+/;
    if (exp_reg.test(valor)==false){
	alert("Email invalido.");
    }
}

function validaForm() {
    var x = document.forms["form"]["cartaosus"].value;
    if (x == null || x == "") {
        alert("Numero do cartao SUS precisa ser preenchido.");
        return false;
    }
}

function validaRecuperarSenha(button) {
    var emailField = button.form.getElementsByTagName("input")[0];
    if (emailField.value == '') {
	alert('E-mail inválido');
    }
    else {
	alert('Um e-mail foi enviado para ' + emailField.value + ' com as instruções para recuperar a senha');
	emailField.value = '';
    }
    return false;
}

function feedbackMessageAndCleanForm(button) {
    var form = button.form;
    var feedbackMessage = button.getAttribute('data-feedbackMessage');
    alert(feedbackMessage);
    for (i in form.getElementsByTagName("input")) {
	if (form.getElementsByTagName("input")[i].type != 'button') {
	    form.getElementsByTagName("input")[i].value = '';
	}
    }
    return false;
}

function userActionChanged(select) {
    if (select.value == "Sair") {
        location.href = LOGOUT_URL;
    }
}
