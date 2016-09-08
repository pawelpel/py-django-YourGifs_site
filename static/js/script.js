/**
 * Created by pawelpel on 08.09.2016.
 */


$(document).ready(function(){

    var gify = $('[data-toggle="tooltip"]');

    if(gify.title !== ''){
        gify.tooltip();
    }

});