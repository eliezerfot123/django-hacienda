function calcular(event)
{
    $("[name^='monto-']").each(function(index,val)
    {
        var impuesto=val.name.split("-")[1];
        var cancelado=$('[name=cancelado-'+impuesto+']')[0];
        var monto=parseFloat(val.value);
        var intereses=parseFloat($('[name=intereses-'+impuesto+']')[0].value||0);
        var trimestres=parseFloat($('[name=trimestres-'+impuesto+']')[0].value||0);
        var recargo=parseFloat($('[name=recargo-'+impuesto+']')[0].value)||0;
        var descuento=parseFloat($('[name=descuento-'+impuesto+']')[0].value/100);
        var subtotal=$('#subtotal-'+impuesto);
        var total=(monto+intereses+recargo);
        calculo=((total-(total*descuento))/4)*trimestres
        cancelado.value=calculo;
    subtotal.text(calculo)


    });
}

    $("[name^='trimestres-']").change(calcular);
    $(":input").bind("keyup change",calcular);
    calcular(null);
