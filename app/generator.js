var page = require('webpage').create();
var system = require('system');

if (system.args.length === 2) {
  console.log('Usage: [some URL] [some username]');
  phantom.exit();
}

page.viewportSize = { width: 1680, height: 1680};

var address = system.args[1];
var output = system.args[2];

page.open(address, function (status) {
  if (status !== 'success') {
    console.log('Unable to load the address!');
    phantom.exit();
  } else {
    window.setTimeout(function () {
      page.render(output);
      phantom.exit();
    }, 5000); // Change timeout as required to allow sufficient time
  }
});