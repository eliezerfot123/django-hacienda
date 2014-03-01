function calcular(event)
{
    $("[name^='monto-']").each(function(index,val)
    {
        var impuesto=val.name.split("-")[1];
        var ano=val.name.split("-")[2];
        var cancelado=$('[name=cancelado-'+impuesto+'-'+ano+']')[0];
        var monto=parseFloat(val.value);
        var intereses=parseFloat($('[name=intereses-'+impuesto+'-'+ano+']')[0].value/100||0);
        var credito=parseFloat($('[name=credito-'+impuesto+'-'+ano+']')[0].value);
        var trimestres=parseFloat($('[name=trimestres-'+impuesto+'-'+ano+']')[0].value||0);
        var recargo=parseFloat($('[name=recargo-'+impuesto+'-'+ano+']')[0].value/100)||0;
        var descuento=parseFloat($('[name=descuento-'+impuesto+'-'+ano+']')[0].value/100);
        var subtotal=$('#subtotal-'+impuesto+'-'+ano);
        monto=monto-(monto*descuento);
        calculo=monto;
        calculo=(calculo/4)*trimestres
        calculo=calculo+(calculo*recargo)+(calculo*intereses);
        calculo=calculo-credito;
        cancelado.value=calculo;
    subtotal.text(calculo)


    });
}

    $("[name^='trimestres-']").change(calcular);
    $(":input").bind("keyup change",calcular);
    calcular(null);
