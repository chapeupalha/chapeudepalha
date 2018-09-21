$(document).ready(function () {

    // CSRF TOKEN para a requisição AJAX
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
         }
    });
    // FIM DO CSRF TOKEN

    $.ajax({
        type: "POST",
        url: 'ajax_chart_sexo',
        // data: {'csrfmiddlewaretoken': '{{ csrf_token }}'},
        success: function(data){
            JSON.stringify(data)
            var sexo = data.sexo;
            var qtd = data.qtd;
            grafico(sexo, qtd);
        }
    });
    $.ajax({
        type: "POST",
        url: 'ajax_chart_municipio',
        // data: {'csrfmiddlewaretoken': '{{ csrf_token }}'},
        success: function(data){
            JSON.stringify(data);
            // console.log(data);
            var municipio = data.municipio;
            var qtdMunicipio = data.qtd;
            graficoMunicipio(municipio, qtdMunicipio);
        }
    });
    $.ajax({
        type: "POST",
        url: 'ajax_chart_dt_cadastro',
        // data: {'csrfmiddlewaretoken': '{{ csrf_token }}'},
        success: function(data){
            // JSON.stringify(data);
            console.log(data);
            var dt_cadastro = data.dt_cadastro;
            var qtd = data.qtd;
            graficoDtCadastro(dt_cadastro, qtd);
        }
    });

    var ctx = document.getElementById("productsChart");

    function grafico(sexo, qtd) {

        var productsChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: sexo,
                datasets: [{
                    label: 'Produtos',
                    data: qtd,
                    backgroundColor: [
                        "rgb(0, 188, 212)",
                        "rgb(233, 30, 99)",
                        "rgb(255, 193, 7)",
                    ],
                }]
            },
            options: {
                options: {
                    responsive: true,
                    legend: true
                }
            }
        });
    }

    var ctxMunicipio = document.getElementById("municipioChart");
    function graficoMunicipio(municipio, qtdMunicipio) {

        var municipioChart = new Chart(ctxMunicipio, {
            type: 'bar',
            data: {
                labels: municipio,
                datasets: [{
                    label: 'Municípios mais cadastrados',
                    data: qtdMunicipio,
                    backgroundColor: [
                        "rgb(0, 188, 212)",
                        "rgb(233, 30, 99)",
                        "rgb(255, 193, 7)",
                        "rgb(30, 99, 132)",
                        "rgb(255, 34, 0)",
                        "rgba(75, 192, 192)",
                        "rgba(153, 102, 255)",
                        "rgba(255, 159, 64)"

                    ]
                }]
            },
            options: {
                options: {
                    responsive: true,
                    legend: true
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true
                        }
                    }]
                }
            }
        });
    }

    var ctxDtCadastro = document.getElementById("dtCadastroChart");
    function graficoDtCadastro(dt_cadastro, qtd) {

        console.log(dt_cadastro)
        console.log(qtd)

        var dtCadastroChart = new Chart(ctxDtCadastro, {
            type: 'line',
            data: {
                labels: dt_cadastro,
                datasets: [{
                    label: 'Quantidade de cadastros por dia',
                    data: qtd,
                    borderColor: 'rgba(0, 188, 212, 0.75)',
                    backgroundColor: 'rgba(0, 188, 212, 0.3)',
                    pointBorderColor: 'rgba(0, 188, 212, 0)',
                    pointBackgroundColor: 'rgba(0, 188, 212, 0.9)',
                    pointBorderWidth: 1
                }]
            },
            options: {
                options: {
                    responsive: true,
                    legend: true
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true
                        }
                    }]
                }
            }
        });
    }

});