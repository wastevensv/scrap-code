var index = require('./distroindex.json');
var fs = require('fs');
var rmdir = require('rimraf');
var ejs = require('ejs');

var dirtemplate = fs.readFileSync("../layouts/directory.ejs", 'ascii');
var renderdir   = ejs.compile(dirtemplate);
var endtemplate = fs.readFileSync("../layouts/endpoint.ejs", 'ascii');
var renderend   = ejs.compile(endtemplate);

path = "./distros"
rmdir.sync(path)
fs.mkdirSync(path);

var t = renderdir({title: "Distros", items: index, root: true});
fs.writeFileSync(path+"/index.html", t);

for (var d in index) {
  if (index.hasOwnProperty(d)) {
    distro = index[d];

    console.log(distro.name);
    var dir = path+"/"+distro.name
    fs.mkdirSync(dir);
    
    var t = renderdir({title: distro.name, items: distro.flavors, root: false});
    fs.writeFileSync(dir+"/index.html", t);

    for (var f in distro.flavors) {
      if (distro.flavors.hasOwnProperty(f)) {
        flavor = distro.flavors[f];

        var dir = path+"/"+distro.name+"/"+flavor.name
        console.log("  "+flavor.name);
        fs.mkdirSync(dir);

        var t = renderend({title: distro.name+" "+flavor.name, releases: flavor.releases, root: false});
        fs.writeFileSync(dir+"/index.html", t);
      }
    }
  }
}
