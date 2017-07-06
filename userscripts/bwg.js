var base_url = 'https://www.biblegateway.com/passage/?';

function buildBgwQuery(userquery)
{
    var parts = userquery.split(/\s+/);
    if (parts.length == 2)
        return 'search=' + encodeURIComponent(parts.join(' '));

    var search = encodeURIComponent(parts.slice(0, 2).join(' '));
    var version = encodeURIComponent(parts[2]);
    return `search=${search}&version=${version}`;
}

var win = window.open(
    base_url + buildBgwQuery(prompt('Bible Query:')),
    '_self');

'read the bible, sinner';
