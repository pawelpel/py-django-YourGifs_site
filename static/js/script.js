/**
 * Created by pawelpel on 08.09.2016.
 */


$(document).ready(function(){

    var gif_z_tooltipem = $('[data-toggle="tooltip"]');

    if(gif_z_tooltipem.title !== ''){
        gif_z_tooltipem.tooltip();
    }
});