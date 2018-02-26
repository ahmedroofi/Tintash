var my_laptops = "/devices/api/device/?type=1&assigned__assign_to="+user_id
var my_tabs = "/devices/api/device/?type=5&assigned__assign_to="+user_id
var my_phone = "/devices/api/device/?type=4&assigned__assign_to="+user_id
var my_internet ="/devices/api/device/?type=2&assigned__assign_to="+user_id
var my_lcd = "/devices/api/device/?type=3&assigned__assign_to="+user_id
var avl_laptops = "/devices/api/device/?type=1&assigned__assign_to__isnull=true";
var avl_tabs = "/devices/api/device/?type=5&assigned__assign_to__isnull=true";
var avl_phone = "/devices/api/device/?type=4&assigned__assign_to__isnull=true";
var avl_internet ="/devices/api/device/?type=2&assigned__assign_to__isnull=true";
var avl_lcd = "/devices/api/device/?type=3&assigned__assign_to__isnull=true";
var all_laptops = "/devices/api/device/?type=1";
var all_tabs = "/devices/api/device/?type=5";
var all_phone = "/devices/api/device/?type=4";
var all_internet ="/devices/api/device/?type=2";
var all_lcd = "/devices/api/device/?type=3";

var lapgrid = $('#laptopgrid').DataTable({
    "oLanguage": {
    "sEmptyTable": "No Device"
    },
    "columns": [
        { "data": "name" },
        { "data": "year" },
        { "data": "model" },
        { "data": "identifier" },
        { "data": "serial_number" },
        { "data": "specs" },
        {"data": "assigned.assign_to"},
        {"data": "assigned.issue_date"}
    ]
});
var phngrid = $('#phonegrid').DataTable({
    "oLanguage": {
    "sEmptyTable": "No Device"
    },
    "columns": [
        { "data": "name" },
        { "data": "year" },
        { "data": "model" },
        { "data": "identifier" },
        { "data": "serial_number" },
        { "data": "specs" },
        {"data": "assigned.assign_to"},
        {"data": "assigned.issue_date"}
    ]
});
var tabgrid = $('#tabletgrid').DataTable({
    "oLanguage": {
    "sEmptyTable": "No Device"
    },
    "columns": [
        { "data": "name" },
        { "data": "year" },
        { "data": "model" },
        { "data": "identifier" },
        { "data": "serial_number" },
        { "data": "specs" },
        {"data": "assigned.assign_to"},
        {"data": "assigned.issue_date"}
    ]
});
var lcdgrid = $('#lcdgrid').DataTable({
    "oLanguage": {
    "sEmptyTable": "No Device"
    },
    "columns": [
        { "data": "model" },
        { "data": "inchs" },
        {"data": "assigned.assign_to"},
        {"data": "assigned.issue_date"}
    ]
});
var intgrid = $('#internetgrid').DataTable({
    "oLanguage": {
    "sEmptyTable": "No Device"
    },
    "columns": [
        { "data": "sim_number" },
        { "data": "name" },
        { "data": "whose_name" },
        {"data": "assigned.assign_to"},
        {"data": "assigned.issue_date"}

    ]
});
$(document).ready(function() {
    lapgrid.ajax.url({"url": my_laptops, "dataSrc": ""}).load();
    phngrid.ajax.url({"url": my_phone, "dataSrc": ""}).load();
    tabgrid.ajax.url({"url": my_tabs, "dataSrc": ""}).load();
    lcdgrid.ajax.url({"url": my_lcd, "dataSrc": ""}).load();
    intgrid.ajax.url({"url": my_internet, "dataSrc": ""}).load();
});

$('.mydevices').on('click', function(){
    $('.devicelabel').html($(this).text());
    lapgrid.ajax.url(my_laptops).load();
    phngrid.ajax.url(my_phone).load();
    tabgrid.ajax.url(my_tabs).load();
    lcdgrid.ajax.url(my_lcd).load();
    intgrid.ajax.url(my_internet).load();
});

$('.available').on('click', function(){
    $('.devicelabel').html($(this).text());
    lapgrid.ajax.url(avl_laptops).load();
    phngrid.ajax.url(avl_phone).load();
    tabgrid.ajax.url(avl_tabs).load();
    lcdgrid.ajax.url(avl_lcd).load();
    intgrid.ajax.url(avl_internet).load();
});

$('.alldevices').on('click', function(){
    $('.devicelabel').html($(this).text());
    lapgrid.ajax.url(all_laptops).load();
    phngrid.ajax.url(all_phone).load();
    tabgrid.ajax.url(all_tabs).load();
    lcdgrid.ajax.url(all_lcd).load();
    intgrid.ajax.url(all_internet).load();
});
