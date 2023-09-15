
const mustache = require('Mustache');


var fs = require('fs');
function sumar(a, b){
    return a + b
}

  try {
    const json1 = fs.readFileSync('data1.json', 'utf8')
    var viewjson = JSON.parse(json1)


    const formTemplate = fs.readFileSync('form.mustache', 'utf8')
    var partial = {}
    partial.form = formTemplate

    
    const formTemplate1 = fs.readFileSync('funcionesRelacion.mustache', 'utf8')
    partial.funcionesRelacion = formTemplate1

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



