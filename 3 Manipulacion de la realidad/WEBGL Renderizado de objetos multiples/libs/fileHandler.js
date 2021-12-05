(function(global) {
/*
  * fileHandler
  * mruizq@unah.hn
*/
    var fileHandler = {
        VERSION: '0.0.1',
        loadText: function(url, callback) {
            var request = new XMLHttpRequest();
	        request.open('GET', url + '?please-dont-cache=' + Math.random(), true);
	        request.onload = async function () {
            if (request.status < 200 || request.status > 299) {
                callback(null);
                
            } else {
                callback(request.responseText);
            }
            };
            request.send();
        },
        loadJSON: function(url, callback){
            this.loadText(url, (jsonResponse) => {
                if(jsonResponse){
                    callback(JSON.parse(jsonResponse));
                }else{
                    callback(null);
                }
            })
        }
    };
    global.fileHandler = fileHandler;
})(window || this);