
const mustache = require('Mustache');


var fs = require('fs');
function sumar(a, b){
    return a + b
}

  try {
    const json1 = fs.readFileSync('data1.json', 'utf8')
    var viewjson = JSON.parse(json1)

    var partial = {}

    const funcionesRelacion = fs.readFileSync('funcionesRelacion.mustache', 'utf8')
    partial.funcionesRelacion = funcionesRelacion

    console.log(viewjson)

    fs.readFile('template1.php', 'utf8', function(err, data) {
        if (err) console.log(err)
        var output = mustache.render(data, viewjson, partial);
        fs.writeFile('output.php', output, {options:'utf8'}, function(error){

        })
    });
  
  } catch (err) {
    console.error(err)
  }



