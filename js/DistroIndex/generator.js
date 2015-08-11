var index = require('./distroindex.json');
var fs = require('fs');
var rmdir = require('rimraf');

path = "./index"
rmdir.sync(path)
fs.mkdirSync(path);
for (var d in index) {
  if (index.hasOwnProperty(d)) {
    distro = index[d];

    //console.log(distro.name);
    fs.mkdirSync(path+"/"+distro.name);

    for (var f in distro.flavors) {
      if (distro.flavors.hasOwnProperty(f)) {
        flavor = distro.flavors[f];

        //console.log("  "+flavor.name);
        fs.mkdirSync(path+"/"+distro.name+"/"+flavor.name);

        for (var r in flavor.releases) {
          if (flavor.releases.hasOwnProperty(r)) {
            release = flavor.releases[r];
            fs.mkdirSync(path+"/"+distro.name+"/"+flavor.name+"/"+"v"+release.version+"-"+release.arch);
            //console.log("    "+"v"+release.version+"-"+release.arch);
          }
        }
      }
    }
  }
}
