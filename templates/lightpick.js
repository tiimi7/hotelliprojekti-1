var picker = new Lightpick({
    field: document.getElementById('demo'),
    secondField: document.getElementById(''),
    repick: true,
    startDate: moment().startOf('month').add(7, 'day'),
    endDate: moment().add(1, 'month').endOf('month').subtract(7, 'day'),
    onSelect: function(start, end){
        var str = '';
        str += start ? start.format('Do MMMM YYYY') + ' to ' : '';
        str += end ? end.format('Do MMMM YYYY') : '...';
        document.getElementById('demo').innerHTML = str;
    }
});