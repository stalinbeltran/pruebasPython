


const mustache = require('Mustache');

var view = {
    title: "Joe",
    calc: function () {
      return 2 + 4;
    }
  };
  
  var output = mustache.render("{{title}} spends {{calc}}", view);
console.log(output)


var fs = require('fs');
function sumar(a, b){
    return a + b
}

var view1 = {
    name: "Joe",
    calc: function () {
      //return 2 + 4;
      return sumar(3,7)
    }
  };


  try {
    const json1 = fs.readFileSync('data1.json', 'utf8')
    var viewjson = JSON.parse(json1)


    const formTemplate = fs.readFileSync('form.mustache', 'utf8')
    var partial = {}
    partial.form = formTemplate

    
    const formTemplate1 = fs.readFileSync('funcionesRelacion.mustache', 'utf8')
    partial.funcionesRelacion = formTemplate1

    console.log(viewjson)
    var json = {
        "name": "de todo ",
        "valor": "contenido de form"
      }
    fs.readFile('template1.php', 'utf8', function(err, data) {
        console.log(err)
        var output = mustache.render(data, viewjson, partial);
        fs.writeFile('output.php', output, {options:'utf8'}, function(error){

        })
        //console.log(output)
    });
  
  } catch (err) {
    console.error(err)
  }



