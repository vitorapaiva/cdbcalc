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
                reject(parsed.error);
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
        let data = new Date(calculatedData.data[0].date);
        let data_adjusted = new Date( data.getTime() + Math.abs(data.getTimezoneOffset()*60000));
        let result="<div class='col alert alert-success'><b>Data:</b> <span>"+data_adjusted.toLocaleDateString()+"</span> <b>Valor Calculado:</b> <span>R$"+calculatedData.data[0].unitPrice.toLocaleString()+"</span></div>";
        divCalculatedData.append(result);
    }
    catch(error){
        Swal.fire({
          icon: 'warning',
          title: 'Atenção',
          text: error
        })
    }
}