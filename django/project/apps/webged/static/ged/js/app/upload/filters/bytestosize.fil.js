angular.module('my-ged.upload').filter('bytesToSize', function() {

  // In the return function, we must pass in a single parameter which will be the data we will work on.
  // We have the ability to support multiple other parameters that can be passed into the filter optionally
  return function(input, optional1, optional2) {


 	var sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    if (input === 0) return 'n/a';
    var i = parseInt(Math.floor(Math.log(input) / Math.log(1024)));
    if (i === 0) return input + ' ' + sizes[i];
    var output= (input / Math.pow(1024, i)).toFixed(1) + ' ' + sizes[i];
    // Do filter work here
    return output;

  }

});
