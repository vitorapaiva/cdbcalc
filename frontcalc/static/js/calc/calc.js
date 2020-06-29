function getCalculatedAmount(investmentDate, currentDate, cdbRate, investedAmount){
    return new Promise ((resolve,reject) => {
        $.post('/api/v1/calc/', JSON.stringify({
            investmentDate: investmentDate,
            currentDate: currentDate,
            cdbRate: cdbRate.replace(",",".").replace("%",""),
            investedAmount    : investedAmount.replace(".","").replace(",",".")
        }), function (result) {
            resolve(result);
        }, "json").fail(function( jqXHR, textStatus, errorThrown ) {
            parsed=$.parseJSON(jqXHR.responseText);
            if(parsed.error){
                reject(new Error(parsed.error));
            }
        });
    });
}

async function returnCalculatedAmount() {
    try{
        let investmentDate = $("input[name='investmentDate']").val();
        let currentDate = $("input[name='currentDate']").val();
        let cdbRate = $("input[name='cdbRate']").val();
        let investedAmount = $("input[name='investedAmount']").val();
        let divCalculatedData = $("#calculated_data");
        let calculatedData = await getCalculatedAmount(investmentDate, currentDate, cdbRate, investedAmount);
        var data = new Date(calculatedData.data[0].date);
        let result="<div class='col alert alert-success'><b>Data:</b> <span>"+data.toLocaleDateString()+"</span> <b>Valor Calculado:</b> <span>R$"+calculatedData.data[0].unitPrice.toLocaleString()+"</span></div>";
        divCalculatedData.append(result);
    }
    catch(error){
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: error
        })
    }
}